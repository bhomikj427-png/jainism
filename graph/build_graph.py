#!/usr/bin/env python3
"""
build_graph.py — Deterministic graph builder for the ancient-texts repo.
Scans concepts/*.md, parses front-matter + ## Links blocks.
Renders graph/graph.svg via Graphviz (force-directed, Obsidian-like).
Emits graph/graph.html — an Obsidian-style force-graph (d3-force) view.
Idempotent: safe to re-run at any time.
"""

import os
import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = REPO_ROOT / "concepts"
GRAPH_DIR = REPO_ROOT / "graph"

# Edge style by link type (style used by SVG; HTML draws uniform Obsidian-grey links)
EDGE_STYLES = {
    # Structural / within-system  -> solid
    "is-a-type-of":                     ("solid",  "#333333"),
    "part-of":                          ("solid",  "#333333"),
    "expressed-by":                     ("solid",  "#555555"),
    "formalizes":                       ("solid",  "#555555"),
    "aggregates-into":                  ("solid",  "#555555"),
    "aggregates-from":                  ("solid",  "#555555"),
    # Cross-tradition / cross-text -> dashed
    "shares-vocabulary-with":           ("dashed", "#0066cc"),
    "structurally-parallel-to":         ("dashed", "#009933"),
    "historically-influenced-by":       ("dashed", "#cc6600"),
    # False equivalence -> dotted red
    "often-conflated-with-NOT-equivalent": ("dotted", "#cc0000"),
}

# Canonical tradition-family -> node colour.
# Two palettes: pastel for the (white) SVG legend math, vivid for the dark graph.
FAMILY_COLOURS = {
    "Jain":               "#f5c518",
    "Buddhist":           "#ffa07a",
    "Nyaya-Vaisheshika":  "#82b4ff",
    "Vedanta":            "#b0e0b0",
    "Samkhya-Yoga":       "#d8b4fe",
    "Mimamsa":            "#7fd4c0",
    "Carvaka":            "#c8a06a",
    "Greek":              "#c0c0c0",
    "Modern/Western":     "#e0e0e0",
    "cross-tradition":    "#f4a6c6",
    "unwritten":          "#888888",
}
# vivid, saturated colours that pop on a dark background (Obsidian group colours)
FAMILY_COLOURS_DARK = {
    "Jain":               "#ffd23f",
    "Buddhist":           "#ff8c5a",
    "Nyaya-Vaisheshika":  "#5b9bff",
    "Vedanta":            "#4fd16b",
    "Samkhya-Yoga":       "#c77dff",
    "Mimamsa":            "#2dd4bf",
    "Carvaka":            "#d9a066",
    "Greek":              "#b8b8b8",
    "Modern/Western":     "#dcdcdc",
    "cross-tradition":    "#ff6fa5",
    "unwritten":          "#777777",
}
DEFAULT_COLOUR = "#ffffff"
DEFAULT_COLOUR_DARK = "#9aa0a6"

FAMILY_ORDER = [
    "Jain", "Buddhist", "Nyaya-Vaisheshika", "Vedanta", "Samkhya-Yoga",
    "Mimamsa", "Carvaka", "Greek", "Modern/Western", "cross-tradition",
    "unwritten", "unknown",
]


def _ascii_fold(s: str) -> str:
    """Lowercase + strip diacritics so 'Nyāya-Vaiśeṣika' matches 'nyaya-vaisesika'."""
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii").lower()


def tradition_family(raw: str) -> str:
    """Map a free-form front-matter `tradition:` value to a canonical family.
    Deterministic keyword matching, checked in priority order to disambiguate
    overlaps (e.g. 'Hindu (Vedic-...-Yoga)' is Vedanta, not Samkhya-Yoga)."""
    t = _ascii_fold(raw)
    if "unwritten" in t:
        return "unwritten"
    if "cross-tradition" in t:
        return "cross-tradition"
    if "jain" in t:
        return "Jain"
    if "carvaka" in t or "lokayata" in t:
        return "Carvaka"
    if "mimamsa" in t:
        return "Mimamsa"
    if "nyaya" in t or "vaisesika" in t or "vaiseshika" in t:
        return "Nyaya-Vaisheshika"
    if "buddhist" in t or "madhyamaka" in t or "yogacara" in t or "abhidharma" in t:
        return "Buddhist"
    if "vedanta" in t or "advaita" in t or "vedic" in t:
        return "Vedanta"
    if "samkhya" in t or "sankhya" in t:
        return "Samkhya-Yoga"
    if "yoga" in t:
        return "Samkhya-Yoga"
    if "hindu" in t:
        return "Vedanta"
    if "greek" in t or "stoic" in t or "platon" in t or "aristotel" in t or "neoplaton" in t:
        return "Greek"
    if "western" in t or "modern" in t or "physics" in t or "logic" in t or "mathematical" in t:
        return "Modern/Western"
    return "unknown"


def tradition_colour(raw: str) -> str:
    return FAMILY_COLOURS.get(tradition_family(raw), DEFAULT_COLOUR)


def tradition_colour_dark(raw: str) -> str:
    return FAMILY_COLOURS_DARK.get(tradition_family(raw), DEFAULT_COLOUR_DARK)


FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
LINKS_SECTION_RE = re.compile(r"## Links\s*\n(.*?)(?:\n## |\Z)", re.DOTALL)
LINK_LINE_RE = re.compile(r"^\s*-\s+([\w-]+):\s+([\w./-]+)\s*\|", re.MULTILINE)
# NB: use [ \t]* not \s* — \s matches newlines, so an empty field (e.g. a blank
# `term_devanagari:`) would otherwise swallow the next line's value (e.g. tradition).
YAML_FIELD_RE = re.compile(r"^(\w[\w_]*):[ \t]*(.+)$", re.MULTILINE)


def parse_concept(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    node = {
        "id": path.stem,
        "term_iast": path.stem,
        "tradition": "unknown",
        "status": "unknown",
        "confidence": "low",
        "links": [],
        "written": True,
    }
    fm_match = FRONT_MATTER_RE.search(text)
    if fm_match:
        for m in YAML_FIELD_RE.finditer(fm_match.group(1)):
            node[m.group(1)] = m.group(2).strip()
    links_match = LINKS_SECTION_RE.search(text)
    if links_match:
        for m in LINK_LINE_RE.finditer(links_match.group(1)):
            node["links"].append({"type": m.group(1), "target": m.group(2).strip()})
    return node


def collect_nodes_and_edges():
    nodes = {}
    for md in sorted(CONCEPTS_DIR.glob("*.md")):
        n = parse_concept(md)
        nodes[n["id"]] = n

    # Add unwritten forward-link targets
    edges = []
    for node in list(nodes.values()):
        for link in node["links"]:
            target_id = link["target"]
            if target_id not in nodes:
                nodes[target_id] = {
                    "id": target_id,
                    "term_iast": target_id,
                    "tradition": "unwritten",
                    "status": "unwritten",
                    "confidence": "—",
                    "links": [],
                    "written": False,
                }
            edges.append({
                "source": node["id"],
                "target": target_id,
                "type": link["type"],
            })

    # Node size = total link count (forward + backward)
    link_counts = defaultdict(int)
    for e in edges:
        link_counts[e["source"]] += 1
        link_counts[e["target"]] += 1

    return nodes, edges, link_counts


def _group_by_family(nodes):
    """Deterministic {family: [(nid, node), ...]}."""
    fam_nodes = defaultdict(list)
    for nid in sorted(nodes):
        fam_nodes[tradition_family(nodes[nid]["tradition"])].append((nid, nodes[nid]))
    return fam_nodes


def render_graphviz(nodes, edges, link_counts, out_path: Path):
    """Static SVG: force-directed (fdp) with one *invisible* cluster per tradition,
    so same-tradition dots pack into their own neat region (grouped, but no boxes).
    Dark background, vivid dots, thin grey links — the static cousin of the HTML."""
    try:
        import graphviz  # type: ignore
    except ImportError:
        dot_path = out_path.with_suffix(".dot")
        _write_dot(nodes, edges, link_counts, dot_path)
        print(f"graphviz Python package not found; wrote {dot_path}")
        print("Install with: pip install graphviz  (and Graphviz system package)")
        return

    g = graphviz.Digraph(
        name="ancient_texts",
        engine="fdp",
        graph_attr={
            "overlap": "prism", "splines": "false", "bgcolor": "#1a1a1a",
            "outputorder": "edgesfirst", "K": "0.65", "sep": "+18",
            "fontname": "Helvetica",
        },
        node_attr={"fontname": "Helvetica", "fontcolor": "#e6e6e6",
                   "color": "#1a1a1a", "penwidth": "0.5", "shape": "ellipse"},
        edge_attr={"penwidth": "0.4", "arrowsize": "0.35", "color": "#cccccc22"},
    )
    fam_nodes = _group_by_family(nodes)
    for fam in [f for f in FAMILY_ORDER if f in fam_nodes]:
        with g.subgraph(name=f"cluster_{fam}") as c:
            c.attr(style="invis", label="", peripheries="0")  # group, but no visible box
            for nid, node in fam_nodes[fam]:
                colour = tradition_colour_dark(node["tradition"])
                deg = link_counts.get(nid, 0)
                size = max(0.18, min(1.5, 0.18 + 0.10 * deg))
                fs = str(max(7, min(16, 7 + deg)))
                shape = "ellipse" if node.get("written") else "box"
                c.node(nid, label=node["term_iast"], style="filled", fillcolor=colour,
                       width=str(size), height=str(size),
                       fixedsize="true" if size < 0.5 else "false",
                       fontsize=fs, shape=shape)
    for e in edges:
        g.edge(e["source"], e["target"], color="#cccccc22")
    try:
        g.render(str(out_path.with_suffix("")), format="svg", cleanup=True)
        print(f"Wrote {out_path}")
    except Exception as ex:
        dot_path = out_path.with_suffix(".dot")
        _write_dot(nodes, edges, link_counts, dot_path)
        print(f"Graphviz render failed ({ex}); wrote {dot_path}")


def _write_dot(nodes, edges, link_counts, dot_path: Path):
    """Deterministic .dot intermediate: fdp + invisible per-tradition clusters."""
    lines = ["digraph ancient_texts {", "  layout=fdp;", '  overlap="prism";',
             '  bgcolor="#1a1a1a";', '  sep="+18";',
             '  node [fontname=Helvetica fontcolor="#e6e6e6" style=filled];']
    fam_nodes = _group_by_family(nodes)
    for fam in [f for f in FAMILY_ORDER if f in fam_nodes]:
        lines.append(f'  subgraph "cluster_{fam}" {{ style=invis; peripheries=0;')
        for nid, node in fam_nodes[fam]:
            colour = tradition_colour_dark(node["tradition"])
            shape = "ellipse" if node.get("written") else "box"
            lines.append(f'    "{nid}" [label="{node["term_iast"]}" fillcolor="{colour}" shape={shape}];')
        lines.append("  }")
    for e in edges:
        lines.append(f'  "{e["source"]}" -> "{e["target"]}" [color="#cccccc22"];')
    lines.append("}")
    dot_path.write_text("\n".join(lines), encoding="utf-8")


def render_force_graph(nodes, edges, out_path: Path):
    """Obsidian-style interactive view (vasturiano/force-graph, d3-force on canvas):
    small dots that cluster organically by link density, colour = tradition,
    size = degree, labels under nodes that fade with zoom, thin grey links,
    dark background, hover to highlight a node's neighbourhood."""
    import json

    deg = defaultdict(int)
    for e in edges:
        deg[e["source"]] += 1
        deg[e["target"]] += 1

    data = {
        "nodes": [
            {
                "id": nid,
                "name": node["term_iast"],
                "val": 1 + deg.get(nid, 0),
                "color": tradition_colour_dark(node["tradition"]),
                "fam": tradition_family(node["tradition"]),
                "written": node.get("written", True),
            }
            for nid, node in nodes.items()
        ],
        "links": [{"source": e["source"], "target": e["target"]} for e in edges],
    }
    present = [f for f in FAMILY_ORDER if any(n["fam"] == f for n in data["nodes"])]
    data_json = json.dumps(data)
    present_json = json.dumps(present)
    legend = "".join(
        f'<div><span class="sw" style="background:{FAMILY_COLOURS_DARK.get(f, DEFAULT_COLOUR_DARK)}"></span>{f}</div>'
        for f in present)

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Ancient Texts — Graph</title>
<script src="./vendor/force-graph.min.js"></script>
<style>
  html,body{{margin:0;height:100%;background:#1a1a1a;font-family:Helvetica,Arial,sans-serif;}}
  #graph{{width:100vw;height:100vh;}}
  #legend{{position:fixed;top:12px;left:12px;z-index:10;background:rgba(30,30,30,.82);
    border:1px solid #333;border-radius:8px;padding:9px 11px;color:#ccc;font-size:12px;}}
  #legend .t{{font-size:10px;text-transform:uppercase;letter-spacing:.05em;color:#888;margin-bottom:5px;}}
  #legend div{{display:flex;align-items:center;gap:7px;margin:3px 0;cursor:default;}}
  .sw{{width:11px;height:11px;border-radius:50%;display:inline-block;}}
  #hint{{position:fixed;bottom:10px;left:12px;z-index:10;color:#666;font-size:11px;}}
</style></head><body>
<div id="legend"><div class="t">Tradition</div>{legend}</div>
<div id="hint">scroll to <b>zoom in</b> and read labels · drag = pan · hover = highlight · same-colour dots cluster by tradition</div>
<div id="graph"></div>
<script>
const DATA = {data_json};
const PRESENT = {present_json};
const NREL = 5;

if (typeof ForceGraph === 'undefined') {{
  document.body.innerHTML = '<div style="color:#ccc;padding:24px;font-family:sans-serif">'
    + 'Could not load the force-graph library (graph/vendor/force-graph.min.js). '
    + 'Re-run <code>python graph/build_graph.py</code> from a machine with internet to re-vendor it.</div>';
  throw new Error('force-graph not loaded');
}}

// Per-tradition foci arranged on a ring -> each tradition forms its own neat cluster
const RING = 320 + 78 * PRESENT.length;
const FOCUS = {{}};
PRESENT.forEach((f, i) => {{
  const a = (2 * Math.PI * i) / PRESENT.length - Math.PI / 2;
  FOCUS[f] = {{ x: RING * Math.cos(a), y: RING * Math.sin(a) }};
}});
// seed each node near its focus so clusters converge quickly and neatly
DATA.nodes.forEach(n => {{
  const c = FOCUS[n.fam] || {{ x: 0, y: 0 }};
  n.x = c.x + (Math.random() - 0.5) * 80;
  n.y = c.y + (Math.random() - 0.5) * 80;
}});

const neighbors = new Map();
DATA.nodes.forEach(n => neighbors.set(n.id, new Set()));
DATA.links.forEach(l => {{ neighbors.get(l.source).add(l.target); neighbors.get(l.target).add(l.source); }});
let hover = null;
const el = document.getElementById('graph');
const radius = n => Math.sqrt(n.val) * NREL;
const isNear = (a, b) => a === b || (neighbors.get(a.id) && neighbors.get(a.id).has(b.id));

const Graph = ForceGraph()(el)
  .backgroundColor('#1a1a1a')
  .graphData(DATA)
  .nodeRelSize(NREL)
  .nodeVal('val')
  .nodeColor(n => (!hover || isNear(hover, n)) ? n.color : 'rgba(120,120,120,0.13)')
  .nodeLabel(() => '')
  .linkColor(l => (hover && (l.source.id === hover.id || l.target.id === hover.id))
      ? 'rgba(255,255,255,0.55)' : 'rgba(200,200,200,0.09)')
  .linkWidth(l => (hover && (l.source.id === hover.id || l.target.id === hover.id)) ? 1.4 : 0.5)
  .nodeCanvasObjectMode(() => 'after')
  .nodeCanvasObject((n, ctx, scale) => {{
    const near = !hover || isNear(hover, n);
    const r = radius(n);
    if (n === hover) {{
      ctx.beginPath(); ctx.arc(n.x, n.y, r + 2 / scale, 0, 2 * Math.PI);
      ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 1.5 / scale; ctx.stroke();
    }}
    // Obsidian-style labels: hubs always; everything else once you zoom in (or on
    // hover). Keeps the zoomed-out overview clean instead of an unreadable pile.
    const show = scale > 1.15 || n.val > 12 || (hover && near);
    if (show) {{
      const fs = Math.max(3.5, 10 / scale);
      ctx.font = fs + 'px Helvetica, Arial, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      const ly = n.y + r + 1.5 / scale;
      ctx.lineWidth = 2.8 / scale; ctx.strokeStyle = 'rgba(20,20,20,0.95)';  // halo
      ctx.strokeText(n.name, n.x, ly);
      ctx.fillStyle = near ? 'rgba(242,242,242,0.98)' : 'rgba(150,150,150,0.30)';
      ctx.fillText(n.name, n.x, ly);
    }}
  }})
  .onNodeHover(n => {{ hover = n || null; el.style.cursor = n ? 'pointer' : null; }})
  .onNodeDragEnd(n => {{ n.fx = n.x; n.fy = n.y; }});

// Spacing radius for each node = its dot radius OR (roughly) half its label width,
// whichever is larger — so dots never sit closer than their labels are wide.
const SPACE = n => Math.max(radius(n) + 6, 7 + n.name.length * 3.4);

// Clustering + collision via plain-JS custom forces (no external d3 -> fully
// self-contained / offline-safe). force-graph's bundled link force still runs.
function clusterForce(strength) {{
  let ns;
  function f(alpha) {{
    for (const n of ns) {{
      const c = FOCUS[n.fam]; if (!c) continue;
      n.vx += (c.x - n.x) * strength * alpha;
      n.vy += (c.y - n.y) * strength * alpha;
    }}
  }}
  f.initialize = a => {{ ns = a; }};
  return f;
}}
// O(n^2) collision (trivial at this size): push apart any two nodes closer than
// the sum of their label-aware spacing radii. Runs a couple of iterations/tick.
function collideForce(strength, iters) {{
  let ns;
  function f() {{
    for (let it = 0; it < iters; it++) {{
      for (let i = 0; i < ns.length; i++) {{
        const a = ns[i], ra = SPACE(a);
        for (let j = i + 1; j < ns.length; j++) {{
          const b = ns[j];
          let dx = b.x - a.x, dy = b.y - a.y;
          const min = ra + SPACE(b);
          let d2 = dx * dx + dy * dy;
          if (d2 > 0 && d2 < min * min) {{
            const d = Math.sqrt(d2);
            const l = ((min - d) / d) * strength * 0.5;
            dx *= l; dy *= l;
            a.vx -= dx; a.vy -= dy; b.vx += dx; b.vy += dy;
          }}
        }}
      }}
    }}
  }}
  f.initialize = a => {{ ns = a; }};
  return f;
}}
Graph.d3Force('cluster', clusterForce(0.32));
Graph.d3Force('collide', collideForce(0.85, 2));
Graph.d3Force('charge').strength(-18);
Graph.d3Force('link').distance(16).strength(0.03);
Graph.d3VelocityDecay(0.35);

let fitted = false;
Graph.onEngineStop(() => {{ if (!fitted) {{ fitted = true; Graph.zoomToFit(500, 70); }} }});
function resize() {{ Graph.width(window.innerWidth).height(window.innerHeight); }}
window.addEventListener('resize', resize); resize();
</script></body></html>"""
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path}")


# ---------------------------------------------------------------------------
# index.md generation (deterministic; one row per written concept file)
# ---------------------------------------------------------------------------
# Section/subsection scheme follows CLAUDE.md §6. Classification is keyword-based
# on the front-matter `tradition:` value, checked in priority order. Hindu deity/
# sectarian theology (Vaiṣṇava/Śaiva/Śākta/Purāṇic/Tantric/bhakti) is filed under
# the Vedānta sub-section; bare Vedic-ritual concepts under "Vedic".
INDEX_SECTIONS = [
    ("Vedic", None),
    ("Epics / Itihāsa", None),
    ("Dharma / Śāstra & Cross-tradition", None),
    ("Six Darśanas", "Nyāya-Vaiśeṣika"),
    ("Six Darśanas", "Sāṃkhya–Yoga"),
    ("Six Darśanas", "Mīmāṃsā"),
    ("Six Darśanas", "Vedānta"),
    ("Jain Āgamas & Darśana", None),
    ("Buddhist Canon", None),
    ("Greek / Western Philosophy & Logic", None),
    ("Modern Physics & Logic Comparanda", None),
]
_THEOLOGY_KW = ("vaisnava", "vaisnavism", "saiva", "saivism", "sakta",
                "tantric", "puranic", "smarta", "kashmir", "lingayat", "vira saiva")


def index_family(raw: str):
    """Map a front-matter `tradition:` value to (section, subsection) per §6."""
    t = _ascii_fold(raw)
    if t.startswith("cross-tradition") or "cross-astika" in t:
        return ("Dharma / Śāstra & Cross-tradition", None)
    if "ajivika" in t or "carvaka" in t or "lokayata" in t:
        return ("Dharma / Śāstra & Cross-tradition", None)
    if "jain" in t:
        return ("Jain Āgamas & Darśana", None)
    if "buddhist" in t or "madhyamaka" in t or "yogacara" in t or "abhidharma" in t:
        return ("Buddhist Canon", None)
    if "itihasa" in t:
        return ("Epics / Itihāsa", None)
    if any(k in t for k in ("greek", "platon", "aristotel", "stoic", "neoplaton",
                            "eleatic", "presocratic", "epicur", "peripatetic",
                            "academy", "pyrrhon", "socratic", "hellenistic")):
        return ("Greek / Western Philosophy & Logic", None)
    if "physics" in t or "western" in t or "mathematical" in t or "artificial intelligence" in t:
        return ("Modern Physics & Logic Comparanda", None)
    # Vedic ritual layer (guard: not Upaniṣadic-Vedānta, not deity-theology)
    if "vedic" in t and "vedanta" not in t and not any(k in t for k in _THEOLOGY_KW):
        return ("Vedic", None)
    if "nyaya" in t or "vaisesika" in t or "vaiseshika" in t:
        return ("Six Darśanas", "Nyāya-Vaiśeṣika")
    if any(k in t for k in ("vedanta", "advaita", "visistadvaita", "dvaita", "uttara mimamsa")):
        return ("Six Darśanas", "Vedānta")
    if any(k in t for k in _THEOLOGY_KW) or "bhakti" in t:
        return ("Six Darśanas", "Vedānta")
    if "samkhya" in t or "sankhya" in t or "yoga" in t:
        return ("Six Darśanas", "Sāṃkhya–Yoga")
    if "mimamsa" in t:
        return ("Six Darśanas", "Mīmāṃsā")
    if "hindu" in t:
        return ("Six Darśanas", "Vedānta")
    return ("Dharma / Śāstra & Cross-tradition", None)


def write_index(out_path: Path):
    """Regenerate index.md from concept front-matter. Deterministic & idempotent."""
    buckets = defaultdict(list)  # (section, subsection) -> [(id, status, confidence)]
    total = 0
    for md in sorted(CONCEPTS_DIR.glob("*.md")):
        n = parse_concept(md)
        buckets[index_family(n["tradition"])].append(
            (n["id"], n.get("status", "unknown"), n.get("confidence", "low")))
        total += 1

    lines = [
        "# Index — Source-Grounded Comparative Philosophy & Physics Repository",
        "",
        "Grouped by tradition-family (CLAUDE.md §6). Lists every written concept with its status/confidence.",
        "**Auto-generated by `graph/build_graph.py` from concept front-matter — do not hand-edit.**",
        f"Counts: {total} concept files total.",
        "",
        "---",
        "",
    ]
    last_section = None
    for key in INDEX_SECTIONS:
        section, subsection = key
        if section != last_section:
            lines.append(f"## {section}")
            lines.append("")
            if section == "Jain Āgamas & Darśana":
                lines.append("**Anchor text:** Tattvārtha Sūtra (Umāsvāti / Umāsvāmī) — "
                             "Vijay K. Jain (tr.), Motilal Banarsidass, 2018; "
                             "Nathmal Tatia (tr.), HarperCollins, 1994.")
                lines.append("")
            last_section = section
        if subsection:
            lines.append(f"### {subsection}")
            lines.append("")
        rows = sorted(buckets.get(key, []))
        if not rows:
            lines.append("*(none yet)*")
            lines.append("")
            continue
        lines.append("| concept | status | confidence |")
        lines.append("|---|---|---|")
        for cid, status, conf in rows:
            lines.append(f"| {cid} | {status} | {conf} |")
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {out_path} ({total} concepts)")


# ---------------------------------------------------------------------------
# Deterministic structural audit (CLAUDE.md §5/§8). Prints defects; does not fix.
# ---------------------------------------------------------------------------
# Directional types encode a real asymmetry -> storing both directions is a
# DEFECT. Symmetric types have no natural "forward" -> bidirectional is allowed.
DIRECTIONAL_TYPES = {
    "is-a-type-of", "part-of", "formalizes", "expressed-by",
    "aggregates-into", "aggregates-from", "historically-influenced-by",
}
SYMMETRIC_TYPES = {
    "shares-vocabulary-with", "structurally-parallel-to",
    "often-conflated-with-NOT-equivalent",
}
HIER_TYPES = {"is-a-type-of", "part-of"}
SIMILARITY_TYPES = {
    "shares-vocabulary-with", "structurally-parallel-to",
    "often-conflated-with-NOT-equivalent",
}


def audit_graph(nodes, edges):
    """Report (do not fix) structural defects. Returns True if clean."""
    written = {nid for nid, n in nodes.items() if n.get("written")}
    stubs = sorted(nid for nid, n in nodes.items() if not n.get("written"))
    targets = {e["target"] for e in edges}
    orphans = sorted(n for n in written if n not in targets)

    by_type = defaultdict(set)
    pair_types = defaultdict(set)
    for e in edges:
        by_type[e["type"]].add((e["source"], e["target"]))
        pair_types[(e["source"], e["target"])].add(e["type"])

    bidir_directional = []
    for t in DIRECTIONAL_TYPES:
        s = by_type.get(t, set())
        for (a, b) in s:
            if (b, a) in s and a < b:
                bidir_directional.append((t, a, b))
    bidir_directional.sort()

    forbidden_combo = []
    for pair, ts in pair_types.items():
        if (ts & HIER_TYPES) and (ts & SIMILARITY_TYPES):
            forbidden_combo.append((pair, sorted(ts)))
    forbidden_combo.sort()

    print("\n--- structural audit ---")
    print(f"dangling stubs : {stubs or 'NONE'}")
    print(f"orphans        : {orphans or 'NONE'}")
    print(f"bidirectional directional edges (DEFECT): "
          f"{bidir_directional or 'NONE'}")
    print(f"forbidden hier+similarity combos (DEFECT): "
          f"{forbidden_combo or 'NONE'}")
    clean = not (stubs or orphans or bidir_directional or forbidden_combo)
    print(f"=> {'CLEAN' if clean else 'DEFECTS PRESENT'}")
    return clean


# ---------------------------------------------------------------------------
# Token-efficiency at scale (CLAUDE.md §7). The per-concept loop is O(1); the
# costs that grow are (a) whole-graph lookups and (b) the always-loaded startup
# files. MANIFEST.tsv is the cheap whole-graph index; PROGRESS_SOFT_LIMIT nags
# when progress.md regrows past the point where it should be rotated to archive.
# ---------------------------------------------------------------------------
MANIFEST_PATH = REPO_ROOT / "MANIFEST.tsv"
PROGRESS_PATH = REPO_ROOT / "progress.md"
PROGRESS_SOFT_LIMIT = 60_000  # bytes; rotate run-logs to progress-archive.md past this


def _tsv_safe(s: str) -> str:
    """Strip characters that would break a TSV row."""
    return (s or "").replace("\t", " ").replace("\n", " ").replace("\r", " ").strip()


def write_manifest(nodes, link_counts, out_path: Path):
    """Emit MANIFEST.tsv — one row per *written* concept (file exists). A compact,
    grep-able whole-graph index so the dedup gate and 'does X exist / status of X /
    how many links' questions never need to open concept files. Regenerated each
    run; deterministic & idempotent. NOT a graph node source — build ignores it."""
    rows = []
    for nid in sorted(nodes):
        n = nodes[nid]
        if not n.get("written"):
            continue  # skip unwritten forward-link targets
        rows.append("\t".join((
            nid,
            _tsv_safe(n.get("tradition", "unknown")),
            _tsv_safe(n.get("status", "unknown")),
            _tsv_safe(n.get("confidence", "low")),
            str(link_counts.get(nid, 0)),
            _tsv_safe(n.get("term_devanagari", "")),
        )))
    header = "# key\ttradition\tstatus\tconfidence\tlinks\tdevanagari  (auto-generated by build_graph.py — do not hand-edit)"
    out_path.write_text(header + "\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} ({len(rows)} concepts)")


def check_progress_size():
    """Deterministic nag: warn if progress.md has regrown past the soft limit, so a
    future session rotates closed run-logs to progress-archive.md (CLAUDE.md §9)."""
    if PROGRESS_PATH.exists():
        size = PROGRESS_PATH.stat().st_size
        if size > PROGRESS_SOFT_LIMIT:
            print(f"\n⚠️  progress.md is {size:,} bytes (> {PROGRESS_SOFT_LIMIT:,} soft limit). "
                  f"Rotate closed run-logs into progress-archive.md per CLAUDE.md §9 — "
                  f"this file is loaded on EVERY startup.")


def main():
    GRAPH_DIR.mkdir(exist_ok=True)
    nodes, edges, link_counts = collect_nodes_and_edges()
    print(f"Nodes: {len(nodes)}  Edges: {len(edges)}")
    render_graphviz(nodes, edges, link_counts, GRAPH_DIR / "graph.svg")
    render_force_graph(nodes, edges, GRAPH_DIR / "graph.html")
    write_index(REPO_ROOT / "index.md")
    write_manifest(nodes, link_counts, MANIFEST_PATH)
    audit_graph(nodes, edges)
    check_progress_size()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
build_graph.py — Deterministic graph builder for the ancient-texts repo.
Scans concepts/*.md, parses front-matter + ## Links blocks.
Renders graph/graph.svg via Graphviz (always).
Emits graph/graph.html (Cytoscape self-contained) once node count > 30.
Idempotent: safe to re-run at any time.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = REPO_ROOT / "concepts"
GRAPH_DIR = REPO_ROOT / "graph"

# Edge style by link type (for Graphviz and Cytoscape)
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

import unicodedata

# Canonical tradition-family -> node colour
FAMILY_COLOURS = {
    "Jain":               "#f5c518",  # gold
    "Buddhist":           "#ffa07a",  # salmon
    "Nyaya-Vaisheshika":  "#82b4ff",  # blue
    "Vedanta":            "#b0e0b0",  # green
    "Samkhya-Yoga":       "#d8b4fe",  # purple
    "Mimamsa":            "#7fd4c0",  # teal
    "Carvaka":            "#c8a06a",  # tan/brown
    "Greek":              "#c0c0c0",  # grey
    "Modern/Western":     "#e0e0e0",  # light grey
    "cross-tradition":    "#f4a6c6",  # pink
    "unwritten":          "#dddddd",
}
DEFAULT_COLOUR = "#ffffff"


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


# Deterministic family order + light cluster-background tints (paired with FAMILY_COLOURS)
FAMILY_ORDER = [
    "Jain", "Buddhist", "Nyaya-Vaisheshika", "Vedanta", "Samkhya-Yoga",
    "Mimamsa", "Carvaka", "Greek", "Modern/Western", "cross-tradition",
    "unwritten", "unknown",
]
FAMILY_BG = {
    "Jain": "#fdf3cf", "Buddhist": "#ffe6da", "Nyaya-Vaisheshika": "#e0ecff",
    "Vedanta": "#e3f4e3", "Samkhya-Yoga": "#f0e6ff", "Mimamsa": "#dcf2ec",
    "Carvaka": "#f0e4d2", "Greek": "#eeeeee", "Modern/Western": "#f2f2f2",
    "cross-tradition": "#fde4ee", "unwritten": "#f4f4f4", "unknown": "#ffffff",
}


def _group_by_family(nodes):
    """Deterministic {family: [(nid, node), ...]} grouping for cluster rendering."""
    fam_nodes = defaultdict(list)
    for nid in sorted(nodes):
        fam_nodes[tradition_family(nodes[nid]["tradition"])].append((nid, nodes[nid]))
    return fam_nodes


def render_graphviz(nodes, edges, link_counts, out_path: Path):
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
        graph_attr={
            "layout": "dot", "rankdir": "LR", "compound": "true", "newrank": "true",
            "fontname": "Helvetica", "splines": "true", "overlap": "false",
            "ranksep": "1.1", "nodesep": "0.35", "pack": "true", "packmode": "cluster",
            "bgcolor": "#ffffff",
        },
        node_attr={"fontname": "Helvetica", "fontsize": "11", "penwidth": "0.6"},
        edge_attr={"fontname": "Helvetica", "fontsize": "9", "penwidth": "0.55",
                   "arrowsize": "0.55"},
    )
    # One Graphviz cluster per tradition family -> visible grouped boxes
    fam_nodes = _group_by_family(nodes)
    for fam in [f for f in FAMILY_ORDER if f in fam_nodes]:
        with g.subgraph(name=f"cluster_{fam}") as c:
            c.attr(label=fam, labelloc="t", labeljust="l", style="filled,rounded",
                   color="#bbbbbb", fillcolor=FAMILY_BG.get(fam, "#f4f4f4"),
                   fontsize="20", fontname="Helvetica-Bold", margin="14")
            for nid, node in fam_nodes[fam]:
                colour = tradition_colour(node["tradition"])
                size = max(0.5, min(2.0, 0.4 + 0.2 * link_counts.get(nid, 0)))
                shape = "ellipse" if node.get("written") else "box"
                c.node(nid, label=node["term_iast"], style="filled", fillcolor=colour,
                       width=str(size), height=str(size * 0.6), shape=shape)
    # Edges: style + colour encode the link type (§6); no text labels = far cleaner
    for e in edges:
        style, colour = EDGE_STYLES.get(e["type"], ("solid", "#999999"))
        g.edge(e["source"], e["target"], style=style, color=colour + "aa")
    try:
        g.render(str(out_path.with_suffix("")), format="svg", cleanup=True)
        print(f"Wrote {out_path}")
    except Exception as ex:
        dot_path = out_path.with_suffix(".dot")
        _write_dot(nodes, edges, link_counts, dot_path)
        print(f"Graphviz render failed ({ex}); wrote {dot_path}")


def _write_dot(nodes, edges, link_counts, dot_path: Path):
    lines = ["digraph ancient_texts {", "  layout=dot;", "  rankdir=LR;",
             "  compound=true;", "  node [fontname=Helvetica fontsize=11];"]
    fam_nodes = _group_by_family(nodes)
    for fam in [f for f in FAMILY_ORDER if f in fam_nodes]:
        lines.append(f'  subgraph "cluster_{fam}" {{')
        lines.append(f'    label="{fam}"; style="filled,rounded"; color="#bbbbbb"; '
                     f'fillcolor="{FAMILY_BG.get(fam, "#f4f4f4")}"; fontsize=20;')
        for nid, node in fam_nodes[fam]:
            colour = tradition_colour(node["tradition"])
            shape = "ellipse" if node.get("written") else "box"
            lines.append(f'    "{nid}" [label="{node["term_iast"]}" style=filled '
                         f'fillcolor="{colour}" shape={shape}];')
        lines.append("  }")
    for e in edges:
        style, colour = EDGE_STYLES.get(e["type"], ("solid", "#999999"))
        lines.append(f'  "{e["source"]}" -> "{e["target"]}" [style={style} color="{colour}"];')
    lines.append("}")
    dot_path.write_text("\n".join(lines), encoding="utf-8")


def render_cytoscape(nodes, edges, out_path: Path):
    """Interactive Cytoscape view: nodes grouped into tradition compound boxes,
    fcose force-directed layout, colour=tradition, edge style=link type, legend,
    tap-to-highlight neighbourhood."""
    import json
    fam_nodes = _group_by_family(nodes)
    present = [f for f in FAMILY_ORDER if f in fam_nodes]

    cy_nodes = []
    # parent compound node per family
    for fam in present:
        cy_nodes.append({"data": {"id": f"fam:{fam}", "label": fam, "isParent": True,
                                  "color": tradition_colour(fam) if fam in FAMILY_COLOURS else "#cccccc"}})
    for fam in present:
        for nid, node in fam_nodes[fam]:
            deg = 0  # filled below
            cy_nodes.append({"data": {
                "id": nid, "label": node["term_iast"], "parent": f"fam:{fam}",
                "tradition": node["tradition"], "status": node["status"],
                "written": node.get("written", False),
                "color": tradition_colour(node["tradition"]),
            }})
    # degree -> node size
    deg = defaultdict(int)
    for e in edges:
        deg[e["source"]] += 1
        deg[e["target"]] += 1
    for n in cy_nodes:
        if not n["data"].get("isParent"):
            n["data"]["size"] = 18 + min(46, 4 * deg.get(n["data"]["id"], 0))

    cy_edges = []
    for i, e in enumerate(edges):
        style, colour = EDGE_STYLES.get(e["type"], ("solid", "#999999"))
        cy_edges.append({"data": {"id": f"e{i}", "source": e["source"], "target": e["target"],
                                  "type": e["type"], "color": colour, "lstyle": style}})
    elements_json = json.dumps(cy_nodes + cy_edges)

    # legend rows
    fam_legend = "".join(
        f'<div><span class="sw" style="background:{FAMILY_COLOURS.get(f, "#fff")}"></span>{f}</div>'
        for f in present if f in FAMILY_COLOURS)
    edge_legend = (
        '<div><span class="ln solid"></span>structural</div>'
        '<div><span class="ln dashed"></span>cross-tradition / parallel</div>'
        '<div><span class="ln dotted"></span>conflated — NOT equivalent</div>')

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Ancient Texts — Concept Graph</title>
<script src="https://unpkg.com/cytoscape@3.28.1/dist/cytoscape.min.js"></script>
<script src="https://unpkg.com/layout-base@2.0.1/layout-base.js"></script>
<script src="https://unpkg.com/cose-base@2.2.0/cose-base.js"></script>
<script src="https://unpkg.com/cytoscape-fcose@2.2.0/cytoscape-fcose.js"></script>
<style>
  body{{margin:0;font-family:Helvetica,Arial,sans-serif;background:#fafafa;}}
  #cy{{width:100vw;height:100vh;position:absolute;top:0;left:0;}}
  #legend{{position:absolute;top:12px;left:12px;z-index:10;background:rgba(255,255,255,.94);
    border:1px solid #ddd;border-radius:8px;padding:10px 12px;font-size:12px;
    box-shadow:0 2px 8px rgba(0,0,0,.08);max-height:92vh;overflow:auto;}}
  #legend h4{{margin:6px 0 4px;font-size:11px;text-transform:uppercase;color:#666;letter-spacing:.04em;}}
  #legend div{{display:flex;align-items:center;gap:7px;margin:2px 0;}}
  .sw{{width:13px;height:13px;border-radius:3px;border:1px solid #999;display:inline-block;}}
  .ln{{width:22px;height:0;display:inline-block;}}
  .ln.solid{{border-top:2px solid #555;}}
  .ln.dashed{{border-top:2px dashed #0066cc;}}
  .ln.dotted{{border-top:2px dotted #cc0000;}}
  #hint{{position:absolute;bottom:10px;left:12px;z-index:10;font-size:11px;color:#888;
    background:rgba(255,255,255,.85);padding:4px 8px;border-radius:6px;}}
</style></head><body>
<div id="legend">
  <h4>Tradition</h4>{fam_legend}
  <h4>Link type</h4>{edge_legend}
</div>
<div id="hint">scroll = zoom · drag = pan · click a node to isolate its links · click empty space to reset</div>
<div id="cy"></div>
<script>
try {{ if (window.cytoscapeFcose) cytoscape.use(window.cytoscapeFcose); }} catch(e) {{}}
var elements = {elements_json};
var cy = cytoscape({{
  container: document.getElementById('cy'),
  elements: elements,
  wheelSensitivity: 0.25,
  style: [
    {{ selector: 'node[?isParent]', style: {{
      'label':'data(label)','background-color':'data(color)','background-opacity':0.10,
      'border-width':1.5,'border-color':'data(color)','shape':'round-rectangle',
      'text-valign':'top','text-halign':'center','font-size':'17px','font-weight':'bold',
      'color':'#444','padding':'14px' }} }},
    {{ selector: 'node[!isParent]', style: {{
      'label':'data(label)','background-color':'data(color)',
      'width':'data(size)','height':'data(size)','font-size':'9px',
      'text-valign':'center','text-halign':'center','text-wrap':'wrap','text-max-width':'70px',
      'border-width':0.5,'border-color':'#888','shape':'ellipse','color':'#222' }} }},
    {{ selector: 'node[written = false][!isParent]', style: {{ 'shape':'round-rectangle','border-style':'dashed' }} }},
    {{ selector: 'edge', style: {{
      'width':1,'line-color':'data(color)','line-style':'data(lstyle)','opacity':0.45,
      'target-arrow-color':'data(color)','target-arrow-shape':'triangle','arrow-scale':0.7,
      'curve-style':'bezier' }} }},
    {{ selector: '.faded', style: {{ 'opacity':0.06 }} }},
    {{ selector: '.hi', style: {{ 'opacity':1,'width':2.2,'z-index':99 }} }},
    {{ selector: 'node.hi', style: {{ 'border-width':2,'border-color':'#222' }} }}
  ],
  layout: {{
    name: (window.cytoscapeFcose ? 'fcose' : 'cose'),
    quality:'default', animate:false, randomize:true, packComponents:true,
    nodeSeparation:75, idealEdgeLength: 70, nodeRepulsion: 6000, gravity:0.25,
    nestingFactor:0.1, numIter:2500
  }}
}});
cy.on('tap','node[!isParent]', function(evt){{
  var n = evt.target; var nb = n.closedNeighborhood();
  cy.elements().addClass('faded');
  nb.removeClass('faded').addClass('hi');
}});
cy.on('tap', function(evt){{ if(evt.target===cy){{ cy.elements().removeClass('faded hi'); }} }});
</script></body></html>"""
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path}")


def main():
    GRAPH_DIR.mkdir(exist_ok=True)
    nodes, edges, link_counts = collect_nodes_and_edges()
    print(f"Nodes: {len(nodes)}  Edges: {len(edges)}")
    render_graphviz(nodes, edges, link_counts, GRAPH_DIR / "graph.svg")
    if len(nodes) > 30:
        render_cytoscape(nodes, edges, GRAPH_DIR / "graph.html")
    else:
        print(f"Node count {len(nodes)} <= 30; skipping Cytoscape HTML.")


if __name__ == "__main__":
    main()

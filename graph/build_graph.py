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

# Tradition -> node colour
TRADITION_COLOURS = {
    "Jain":                  "#f5c518",
    "Nyaya-Vaisheshika":     "#82b4ff",
    "Buddhist":              "#ffa07a",
    "Vedanta":               "#b0e0b0",
    "Samkhya":               "#d8b4fe",
    "Greek":                 "#c0c0c0",
    "Modern Physics":        "#e0e0e0",
    "unwritten":             "#dddddd",
}
DEFAULT_COLOUR = "#ffffff"

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
LINKS_SECTION_RE = re.compile(r"## Links\s*\n(.*?)(?:\n## |\Z)", re.DOTALL)
LINK_LINE_RE = re.compile(r"^\s*-\s+([\w-]+):\s+([\w./-]+)\s*\|", re.MULTILINE)
YAML_FIELD_RE = re.compile(r"^(\w[\w_]*):\s*(.+)$", re.MULTILINE)


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


def render_graphviz(nodes, edges, link_counts, out_path: Path):
    try:
        import graphviz  # type: ignore
    except ImportError:
        # Fallback: emit raw .dot file
        dot_path = out_path.with_suffix(".dot")
        _write_dot(nodes, edges, link_counts, dot_path)
        print(f"graphviz Python package not found; wrote {dot_path}")
        print("Install with: pip install graphviz  (and Graphviz system package)")
        return

    g = graphviz.Digraph(
        name="ancient_texts",
        graph_attr={"rankdir": "LR", "fontname": "Helvetica", "splines": "true"},
        node_attr={"fontname": "Helvetica", "fontsize": "11"},
        edge_attr={"fontname": "Helvetica", "fontsize": "9"},
    )
    for nid, node in nodes.items():
        colour = TRADITION_COLOURS.get(node["tradition"], DEFAULT_COLOUR)
        size = max(0.5, min(2.0, 0.4 + 0.2 * link_counts.get(nid, 0)))
        label = node["term_iast"]
        shape = "ellipse" if node.get("written") else "box"
        g.node(
            nid,
            label=label,
            style="filled",
            fillcolor=colour,
            width=str(size),
            height=str(size * 0.6),
            shape=shape,
        )
    for e in edges:
        style, colour = EDGE_STYLES.get(e["type"], ("solid", "#999999"))
        dot_style = "dashed" if style == "dashed" else ("dotted" if style == "dotted" else "solid")
        g.edge(
            e["source"],
            e["target"],
            label=e["type"],
            style=dot_style,
            color=colour,
            fontcolor=colour,
        )
    try:
        g.render(str(out_path.with_suffix("")), format="svg", cleanup=True)
        print(f"Wrote {out_path}")
    except Exception as ex:
        dot_path = out_path.with_suffix(".dot")
        _write_dot(nodes, edges, link_counts, dot_path)
        print(f"Graphviz render failed ({ex}); wrote {dot_path}")


def _write_dot(nodes, edges, link_counts, dot_path: Path):
    lines = ["digraph ancient_texts {", '  rankdir=LR;', '  node [fontname=Helvetica fontsize=11];']
    for nid, node in nodes.items():
        colour = TRADITION_COLOURS.get(node["tradition"], DEFAULT_COLOUR)
        shape = "ellipse" if node.get("written") else "box"
        lines.append(f'  "{nid}" [label="{node["term_iast"]}" style=filled fillcolor="{colour}" shape={shape}];')
    for e in edges:
        style, colour = EDGE_STYLES.get(e["type"], ("solid", "#999999"))
        dot_style = "dashed" if style == "dashed" else ("dotted" if style == "dotted" else "solid")
        lines.append(f'  "{e["source"]}" -> "{e["target"]}" [label="{e["type"]}" style={dot_style} color="{colour}"];')
    lines.append("}")
    dot_path.write_text("\n".join(lines), encoding="utf-8")


def render_cytoscape(nodes, edges, out_path: Path):
    import json
    cy_nodes = []
    for nid, node in nodes.items():
        colour = TRADITION_COLOURS.get(node["tradition"], DEFAULT_COLOUR)
        cy_nodes.append({
            "data": {
                "id": nid,
                "label": node["term_iast"],
                "tradition": node["tradition"],
                "status": node["status"],
                "written": node.get("written", False),
                "color": colour,
            }
        })
    cy_edges = []
    for i, e in enumerate(edges):
        _, colour = EDGE_STYLES.get(e["type"], ("solid", "#999999"))
        cy_edges.append({
            "data": {
                "id": f"e{i}",
                "source": e["source"],
                "target": e["target"],
                "type": e["type"],
                "color": colour,
            }
        })
    elements_json = json.dumps(cy_nodes + cy_edges, indent=2)
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Ancient Texts Graph</title>
<script src="https://unpkg.com/cytoscape@3.28.1/dist/cytoscape.min.js"></script>
<style>body{{margin:0;}} #cy{{width:100vw;height:100vh;}}</style>
</head><body>
<div id="cy"></div>
<script>
var elements = {elements_json};
var cy = cytoscape({{
  container: document.getElementById('cy'),
  elements: elements,
  style: [
    {{ selector: 'node', style: {{
      'label': 'data(label)', 'background-color': 'data(color)',
      'font-size': '11px', 'text-valign': 'center', 'text-halign': 'center',
      'width': 'label', 'height': 'label', 'padding': '6px',
      'shape': 'ellipse'
    }}}},
    {{ selector: 'node[written = false]', style: {{ 'shape': 'rectangle' }} }},
    {{ selector: 'edge', style: {{
      'label': 'data(type)', 'font-size': '9px',
      'line-color': 'data(color)', 'target-arrow-color': 'data(color)',
      'target-arrow-shape': 'triangle', 'curve-style': 'bezier',
      'color': 'data(color)'
    }}}}
  ],
  layout: {{ name: 'cose', animate: false }}
}});
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

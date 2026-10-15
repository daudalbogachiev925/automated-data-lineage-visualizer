import pathlib
import networkx as nx
from graphviz import Digraph

def visualize_lineage(graph: nx.DiGraph, output_path: str) -> pathlib.Path:
    """Render a NetworkX DiGraph to an image using Graphviz.

    Parameters
    ----------
    graph: nx.DiGraph
        The lineage graph.
    output_path: str
        Destination file path (extension determines format, e.g., .png, .svg).

    Returns
    -------
    pathlib.Path
        Path to the generated image file.
    """
    output_path = pathlib.Path(output_path)
    dot = Digraph(comment='Data Lineage', format=output_path.suffix.lstrip('.'))

    for node in graph.nodes:
        dot.node(str(node))
    for src, tgt, data in graph.edges(data=True):
        label = data.get('operation', '')
        dot.edge(str(src), str(tgt), label=label)
    dot.render(filename=output_path.stem, directory=output_path.parent, cleanup=True)
    return output_path

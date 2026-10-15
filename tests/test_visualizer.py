import pathlib
import networkx as nx
from src.visualizer import visualize_lineage

def test_visualize_creates_file(tmp_path):
    # Build a tiny graph
    G = nx.DiGraph()
    G.add_edge('A', 'B', operation='copy')
    G.add_edge('B', 'C', operation='transform')
    output_file = tmp_path / 'lineage_test.png'
    result_path = visualize_lineage(G, str(output_file))
    assert result_path == output_file
    assert result_path.is_file()
    # Basic sanity: file size > 0
    assert result_path.stat().st_size > 0

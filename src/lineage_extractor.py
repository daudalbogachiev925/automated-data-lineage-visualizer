import json
from typing import List, Dict
import networkx as nx

def load_metadata(path: str) -> List[Dict[str, str]]:
    """Load lineage metadata from a JSON file.

    Expected format:
    [
        {"source": "dataset_a", "target": "dataset_b", "operation": "copy"},
        ...
    ]
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_lineage(metadata: List[Dict[str, str]]) -> nx.DiGraph:
    """Convert metadata list into a directed graph.

    Nodes are dataset identifiers. Edges are directed from source to target.
    The edge attribute ``operation`` stores the transformation name.
    """
    graph = nx.DiGraph()
    for entry in metadata:
        src = entry['source']
        tgt = entry['target']
        op = entry.get('operation', '')
        graph.add_node(src)
        graph.add_node(tgt)
        graph.add_edge(src, tgt, operation=op)
    return graph

import pytest
import networkx as nx
from src.lineage_extractor import extract_lineage

@pytest.fixture
def sample_metadata():
    return [
        {"source": "raw/customers", "target": "staging/customers", "operation": "copy"},
        {"source": "staging/customers", "target": "dw/customers", "operation": "transform"},
        {"source": "raw/orders", "target": "staging/orders", "operation": "copy"},
        {"source": "staging/orders", "target": "dw/orders", "operation": "transform"},
        {"source": "dw/customers", "target": "dw/sales_report", "operation": "join"},
        {"source": "dw/orders", "target": "dw/sales_report", "operation": "join"}
    ]

def test_extract_lineage(sample_metadata):
    graph = extract_lineage(sample_metadata)
    assert isinstance(graph, nx.DiGraph)
    # Expected nodes count
    expected_nodes = {
        "raw/customers",
        "staging/customers",
        "dw/customers",
        "raw/orders",
        "staging/orders",
        "dw/orders",
        "dw/sales_report"
    }
    assert set(graph.nodes) == expected_nodes
    # Expected edges count
    assert graph.number_of_edges() == len(sample_metadata)
    # Verify an edge attribute
    op = graph["dw/customers"]["dw/sales_report"]["operation"]
    assert op == "join"

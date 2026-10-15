import argparse
import pathlib
from src.lineage_extractor import load_metadata, extract_lineage
from src.visualizer import visualize_lineage
from src.config import DEFAULT_OUTPUT_DIR

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate data lineage visualization from metadata.')
    parser.add_argument('--metadata', required=True, help='Path to JSON metadata file.')
    parser.add_argument('--output', help='Output image file (default: outputs/lineage.png).')
    return parser.parse_args()

def main():
    args = parse_args()
    metadata_path = pathlib.Path(args.metadata)
    if not metadata_path.is_file():
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}")

    metadata = load_metadata(str(metadata_path))
    graph = extract_lineage(metadata)

    output_path = pathlib.Path(args.output) if args.output else DEFAULT_OUTPUT_DIR / 'lineage.png'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    visualize_lineage(graph, str(output_path))
    print(f"Lineage visualization saved to {output_path}")

if __name__ == '__main__':
    main()

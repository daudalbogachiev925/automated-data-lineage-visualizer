# Automated Data Lineage Visualizer

This repository provides a lightweight Python utility to **extract** data lineage information from cloud data‑lake metadata and **visualize** it as a directed graph image.

## Features
- Parse simple JSON metadata describing source, target, and transformation steps.
- Build a `networkx.DiGraph` representing the lineage.
- Render the graph to PNG (or SVG) using Graphviz.
- Command‑line interface for quick usage.
- Unit tests covering extraction and visualization.

## Installation
```bash
git clone https://github.com/yourusername/automated-data-lineage-visualizer.git
cd automated-data-lineage-visualizer
python -m venv .venv
source .venv/bin/activate  # on Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

> **Note**: Graphviz binaries must be installed on your system. On Ubuntu: `sudo apt-get install graphviz`. On macOS: `brew install graphviz`.

## Usage
```bash
python -m src.main --metadata path/to/metadata.json --output lineage.png
```
- `--metadata` – Path to a JSON file describing the lineage.
- `--output` – Desired output image file (PNG or SVG).

### Metadata format
```json
[
  {"source": "raw/customers", "target": "staging/customers", "operation": "copy"},
  {"source": "staging/customers", "target": "dw/customers", "operation": "transform"}
]
```
Each entry represents a directed edge from **source** to **target**.

## Testing
```bash
pytest -q
```
All tests reside in the `tests/` directory.

## License
MIT License. See `LICENSE` for details.

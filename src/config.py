import pathlib

# Default directory where visualizations are stored if not specified
DEFAULT_OUTPUT_DIR = pathlib.Path('outputs')
DEFAULT_OUTPUT_DIR.mkdir(exist_ok=True)

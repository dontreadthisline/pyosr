# PyOSR Development Guide for AI Agents

## Build and Development Commands
- **Install dependencies**: `uv sync` (uses uv package manager)
- **Run main script**: `python main.py` (parses OSM file and builds road graph)
- **Lint code**: `ruff check .` (Ruff is configured for linting)
- **Format code**: `ruff format .` (Ruff for formatting)
- **Python version**: 3.13+ (specified in .python-version)

## Code Style Guidelines
- **Imports**: Group standard library first, then third-party, then local imports
- **Type hints**: Use explicit type annotations (e.g., `def func() -> str:`)
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Error handling**: Return `None` or raise exceptions for invalid operations
- **Data structures**: Use `NamedTuple` for immutable data (types.py: GeoPoint, Road)
- **Interfaces**: Use `Protocol` for interface definitions (types.py: Router)
- **OSM parsing**: Use `osmium.SimpleHandler` for OSM file parsing

## Testing
- **Test framework**: No tests configured; add with pytest if needed
- **Test data**: Use sample OSM subsets from `road_data/` directory
- **Test routing**: Create synthetic road networks for algorithm testing

## Project Structure
- **Package**: `pyosr/` contains core modules (loader, router, types, utils, etc.)
- **Main entry**: `main.py` demonstrates OSM parsing and graph construction
- **Data files**: OSM files in `road_data/` directory (.osm, .osm.pbf formats)
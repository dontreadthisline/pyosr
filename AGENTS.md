# PyOSR Development Guide for AI Agents

## Build and Development Commands

- **Install dependencies**: `uv sync` (uses uv package manager)
- **Run main script**: `python main.py` (parses OSM file and builds road graph)
- **Run with strace**: `./scripts.sh python main.py` (trace system calls)
- **Python version**: 3.13+ (specified in .python-version)

## Code Style Guidelines

### Python Style
- **Imports**: Group standard library first, then third-party, then local imports
- **Type hints**: Use explicit type annotations (e.g., `def func() -> str:`)
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Error handling**: Return `None` or raise exceptions for invalid operations
- **Line length**: Follow standard Python conventions (79-88 chars)

### Project Structure
- **Package**: `pyosr/` contains core modules (graph_builder, router, types, etc.)
- **Main entry**: `main.py` demonstrates OSM parsing and graph construction
- **Data files**: OSM files in `road_data/` directory (.osm, .osm.pbf formats)

### Key Patterns
- Use `osmium.SimpleHandler` for OSM file parsing (graph_builder.py)
- Use `NamedTuple` for data structures (types.py: GeoPoint, Road)
- Use `Protocol` for interface definitions (types.py: Router)
- Process large OSM datasets with streaming filters (FilterOutOfBox)

### Testing
- No test framework configured; add tests with pytest if needed
- Test graph construction with sample OSM data subsets
- Test routing algorithms with synthetic road networks

### Dependencies
- **Core**: osmium[docs]>=4.2.0, rtree>=1.4.1, opencage>=3.2.0, requests>=2.32.5
- **Package manager**: uv (see uv.lock for exact versions)
- **Python**: >=3.13 (requires modern type hint support)
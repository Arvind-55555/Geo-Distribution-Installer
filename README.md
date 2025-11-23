# Geo Distribution Installer 🌍

A comprehensive one-click installation package for geospatial libraries.

## Features

- **One-click installation** of 50+ geospatial libraries
- **Pre-configured environments** with dependency resolution
- **Cross-platform** support (Windows, Linux, macOS)
- **Web mapping** tools (Folium, ipyleaflet, Kepler.gl)
- **Google Maps** integration
- **Advanced analytics** (PySAL, scikit-learn)
- **Jupyter Lab** with geo extensions

## PyPI Package: 
https://pypi.org/project/geo-distro/

## Installation
### Prerequisites
- Python 3.8 or higher
- Conda or Mamba (Miniconda/Anaconda)

### Install from PyPI
```bash
pip install geo-distro
```
### Install from source
```bash
git clone https://github.com/Arvind-55555/Geo-Distribution-Installer.git
cd geo-distro
pip install -e .
```

## Quick Start

### Command Line Interface
``` bash
# Install complete distribution
geo-distro install

# Install with custom environment name
geo-distro install --env-name my-geo-env

# Verify installation
geo-distro verify

# Show information
geo-distro info

# Uninstall
geo-distro uninstall
```
### Python API
``` bash
from geodistro import GeoDistroInstaller

# Create installer
installer = GeoDistroInstaller(verbose=True)

# Install complete distribution
installer.install_all(env_name="my-geo-env")
```

### Method 1: Quick Install (Recommended)

**Windows:**
```bash
install-geo-distro.bat
```

**Linux/MacOS:**
```bash
chmod +x install-geo-distro.sh
./install-geo-distro.sh
```

### Method 2: Python Installer
```bash
python geo-distro-installer.py
```


### Method 3: Manual Environment Setup
```bash
conda env create -f environment.yml
conda activate geo-distro
conda run -n geo-distro python verify-installation.py
```

## Usage

### Activate the environment
```bash
conda activate geo-distro
```

### Start Jupyter Lab
```bash
jupyter lab
```

### Run verification
```bash
conda run -n geo-distro python verify-installation.py
```   

### Try examples
```bash
conda run -n geo-distro python examples/quick-start.py
```
### Basic Spatial Analysis
``` bash
import geopandas as gpd
import matplotlib.pyplot as plt

# Load sample data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(figsize=(15, 10))
plt.show()
```
### Web Mapping
``` bash
import folium

# Create an interactive map
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
folium.Marker([40.7128, -74.0060], popup='New York City').add_to(m)
m.save('my_map.html')
```

## Included Libraries
### Core Geospatial
- GDAL, GEOS, PROJ
- Rasterio, Fiona, Shapely
- GeoPandas, PyProj, Cartopy

### Web Mapping
- Folium, ipyleaflet, Plotly
- Kepler.gl, Dash, Voila

### Google Maps
- googlemaps, gmaps, geopy

### Advanced Analytics
- PySAL, scikit-learn, scikit-image
- MovingPandas, OSMnx

### Development Tools
- Jupyter Lab with geo extensions
- Testing and code quality tools

## Verification
After installation, run:

```bash
python verify-installation.py
```

## Support
This distribution is built on `conda-forge` for reliable dependency management.
- **Documentation:** [GitHub Documentation](https://github.com/Arvind-55555/Geo-Distribution-Installer/wiki)
- **Issues:** [GitHub Issues](https://github.com/Arvind-55555/Geo-Distribution-Installer/issues)
- **Discussions:** GitHub Discussions

## Development
### Contributing

We welcome contributions! Please see our Contributing Guide for details.
We want to make contributing to Geo Distribution as easy and transparent as possible, whether it's:
- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

See CONTRIBUTING.md for detailed guidelines.

### Development Setup
``` bash
# Clone the repository
git clone https://github.com/yourusername/geo-distro.git
cd geo-distro

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Build package
python -m build

# Upload to PyPI (maintainers only)
twine upload dist/*
```
## System Requirements
- Minimum: 4GB RAM, 5GB disk space
- Recommended: 8GB+ RAM, 10GB+ disk space
- Operating Systems: Windows 10+, macOS 10.14+, Ubuntu 16.04+

## Citation
If you use Geo Distribution in your research, please cite:
```bibtex
@software{geo_distro2024,
  title = {Geo Distribution: One-click geospatial library installer},
  author = {Your Name and Contributors},
  year = {2024},
  url = {https://pypi.org/project/geo-distro/},
  version = {0.1.0}
}
```
## Links
- 🌐 Website: [Web Page](https://pypi.org/project/geo-distro/)
- 📦 PyPI: [PyPI](https://pypi.org/project/geo-distro/)
- 📚 Documentation: [GitHub Documentation](https://github.com/Arvind-55555/Geo-Distribution-Installer/wiki)
- 🐛 Issue Tracker: [GitHub Issues](https://github.com/Arvind-55555/Geo-Distribution-Installer/issues)

## License
MIT License - Feel free to use and distribute!


## Installation Instructions

1. **Download all files** into a directory
2. **Run the appropriate installer** for your system:
   - Windows: Double-click `install-geo-distro.bat`
   - Linux/Mac: Run `./install-geo-distro.sh`
   - Or use: `python geo-distro-installer.py`
3. **Wait for installation** (may take 15-30 minutes depending on internet speed)
4. **Verify installation**: `python verify-installation.py`
5. **Start coding**: `conda activate geo-distro && jupyter lab`

This package provides a complete geospatial development environment with all major libraries pre-configured and tested to work together!

## Acknowledgments
- Built on the amazing work of the conda-forge community
- Thanks to all the geospatial Python library maintainers
- Inspired by Anaconda Distribution's approach to package management


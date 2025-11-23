# Geo Distribution 🌍

A comprehensive one-click installation package for geospatial libraries.

## Features

- **One-click installation** of 50+ geospatial libraries
- **Pre-configured environments** with dependency resolution
- **Cross-platform** support (Windows, Linux, macOS)
- **Web mapping** tools (Folium, ipyleaflet, Kepler.gl)
- **Google Maps** integration
- **Advanced analytics** (PySAL, scikit-learn)
- **Jupyter Lab** with geo extensions

## Quick Start

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
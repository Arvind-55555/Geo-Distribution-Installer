"""
Core functionality for Geo Distribution
"""

import os
import sys
import platform
from pathlib import Path
from typing import List, Dict, Optional

class GeoDistroConfig:
    """Configuration for Geo Distribution"""
    
    ENV_NAME = "geo-distro"
    CONDA_FORGE_CHANNELS = ["conda-forge", "defaults"]
    
    # Core geospatial packages (conda)
    CORE_GEOSPATIAL = [
        "gdal", "geos", "proj", "geotiff", "libspatialindex",
        "rasterio", "fiona", "shapely", "pyproj", "cartopy"
    ]
    
    # Python geospatial packages (pip)
    PYTHON_GEOSPATIAL = [
        "geopandas",
        "contextily",
        "folium",
        "ipyleaflet",
        "mapclassify",
        "movingpandas",
        "osmnx",
        "pyogrio",
        "rasterstats",
        "rioxarray",
        "sentinelsat",
        "whitebox",
        "xyzservices"
    ]
    
    # Web mapping packages
    WEB_MAPPING = [
        "plotly",
        "keplergl",
        "dash",
        "dash-leaflet",
        "voila"
    ]
    
    # Advanced analytics
    ADVANCED_ANALYTICS = [
        "scikit-learn",
        "scikit-image",
        "pysal",
        "esda",
        "splot",
        "libpysal",
        "mgwr",
        "spaghetti",
        "pointpats"
    ]
    
    # Google Maps tools
    GOOGLE_MAPS = [
        "googlemaps",
        "gmaps",
        "geopy"
    ]
    
    # Development tools
    DEV_TOOLS = [
        "jupyter",
        "jupyterlab",
        "jupyter-server-proxy",
        "jupyterlab-git",
        "jupyterlab-geojson",
        "black",
        "flake8",
        "pytest",
        "ipywidgets"
    ]
    
    @classmethod
    def get_all_packages(cls) -> Dict[str, List[str]]:
        """Get all packages organized by category"""
        return {
            "core_geospatial": cls.CORE_GEOSPATIAL,
            "python_geospatial": cls.PYTHON_GEOSPATIAL,
            "web_mapping": cls.WEB_MAPPING,
            "advanced_analytics": cls.ADVANCED_ANALYTICS,
            "google_maps": cls.GOOGLE_MAPS,
            "dev_tools": cls.DEV_TOOLS,
        }
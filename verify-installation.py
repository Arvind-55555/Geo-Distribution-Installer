#!/usr/bin/env python3
"""
Verification script for Geo Distribution installation
"""

import importlib
import sys

def check_library(lib_name, version_attr=None):
    """Check if a library can be imported and get its version"""
    try:
        lib = importlib.import_module(lib_name)
        if version_attr and hasattr(lib, version_attr):
            version = getattr(lib, version_attr)
            return True, version
        elif hasattr(lib, '__version__'):
            return True, lib.__version__
        else:
            return True, "unknown version"
    except ImportError as e:
        return False, str(e)

def main():
    libraries_to_check = [
        ("geopandas", "__version__"),
        ("rasterio", "__version__"),
        ("fiona", "__version__"),
        ("shapely", "__version__"),
        ("pyproj", "__version__"),
        ("folium", "__version__"),
        ("googlemaps", "__version__"),
        ("geopy", "__version__"),
        ("cartopy", "__version__"),
        ("osmnx", "__version__"),
        ("contextily", "__version__"),
        ("ipyleaflet", "__version__"),
        ("pysal", "__version__"),
        ("sklearn", "__version__"),
        ("jupyter", "__version__"),
    ]
    
    print("🔍 Verifying Geo Distribution Installation")
    print("=" * 50)
    
    all_ok = True
    for lib_name, version_attr in libraries_to_check:
        success, version_info = check_library(lib_name, version_attr)
        if success:
            print(f"✓ {lib_name:20} {version_info}")
        else:
            print(f"✗ {lib_name:20} {version_info}")
            all_ok = False
    
    print("=" * 50)
    if all_ok:
        print("🎉 All libraries imported successfully!")
    else:
        print("⚠ Some libraries failed to import. Check the installation.")
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
"""
Geo Distribution Installer - One-click setup for geospatial libraries.
"""

import os
import sys
import subprocess
import platform
import argparse
import time
from pathlib import Path

class GeoDistroInstaller:
    def __init__(self):
        self.system = platform.system().lower()
        self.install_method = "conda"  # Default to conda for better dependency management
        
    def check_prerequisites(self):
        """Check if conda/mamba is available"""
        try:
            subprocess.run(["conda", "--version"], capture_output=True, check=True)
            print("✓ Conda found")
            return "conda"
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(["mamba", "--version"], capture_output=True, check=True)
                print("✓ Mamba found")
                return "mamba"
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("⚠ Conda/Mamba not found. Falling back to pip...")
                return "pip"
    
    def create_environment(self, env_name="geo-distro"):
        """Create a dedicated conda environment"""
        if self.install_method in ["conda", "mamba"]:
            try:
                cmd = [self.install_method, "create", "-n", env_name, "python=3.9", "-y"]
                subprocess.run(cmd, check=True)
                print(f"✓ Created environment: {env_name}")
                return env_name
            except subprocess.CalledProcessError as e:
                print(f"⚠ Failed to create environment: {e}")
                return None
        return None
    
    def install_core_geospatial(self, env_name=None):
        """Install core geospatial libraries"""
        print("\n🔧 Installing Core Geospatial Libraries...")
        
        core_packages = [
            "gdal", "geos", "proj", "geotiff", "libspatialindex",
            "rasterio", "fiona", "shapely", "pyproj", "cartopy"
        ]
        
        if self.install_method in ["conda", "mamba"]:
            # Use conda-forge for better geospatial packages
            channels = ["conda-forge", "defaults"]
            for channel in channels:
                subprocess.run([self.install_method, "config", "--add", "channels", channel], 
                             capture_output=True)
            
            activate_cmd = f"conda activate {env_name} && " if env_name else ""
            
            for package in core_packages:
                try:
                    cmd = [self.install_method, "install", "-c", "conda-forge", package, "-y"]
                    if env_name:
                        cmd.extend(["-n", env_name])
                    subprocess.run(cmd, check=True)
                    print(f"✓ Installed: {package}")
                except subprocess.CalledProcessError:
                    print(f"⚠ Failed to install {package} with conda, trying pip...")
                    self.install_with_pip(package, env_name)
        
        else:
            # Pure pip installation
            for package in core_packages:
                self.install_with_pip(package, env_name)
    
    def install_python_geo_libraries(self, env_name=None):
        """Install Python geospatial libraries"""
        print("\n🐍 Installing Python Geospatial Libraries...")
        
        python_packages = [
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
        
        for package in python_packages:
            self.install_with_pip(package, env_name)
    
    def install_web_mapping(self, env_name=None):
        """Install web mapping and visualization libraries"""
        print("\n🌍 Installing Web Mapping Libraries...")
        
        web_packages = [
            "folium",
            "ipyleaflet",
            "plotly",
            "keplergl",
            "dash",
            "dash-leaflet",
            "voila"
        ]
        
        for package in web_packages:
            self.install_with_pip(package, env_name)
    
    def install_advanced_analytics(self, env_name=None):
        """Install advanced geospatial analytics libraries"""
        print("\n📊 Installing Advanced Analytics Libraries...")
        
        advanced_packages = [
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
        
        for package in advanced_packages:
            self.install_with_pip(package, env_name)
    
    def install_google_maps_tools(self, env_name=None):
        """Install Google Maps and related tools"""
        print("\n🗺️ Installing Google Maps Tools...")
        
        google_packages = [
            "googlemaps",
            "gmaps",
            "geopy"
        ]
        
        for package in google_packages:
            self.install_with_pip(package, env_name)
    
    def install_development_tools(self, env_name=None):
        """Install development and utility tools"""
        print("\n⚙️ Installing Development Tools...")
        
        dev_packages = [
            "jupyter",
            "jupyterlab",
            "jupyter-server-proxy",
            "jupyterlab-git",
            "jupyterlab-geojson",
            "jupyterlab-kernelspy",
            "black",
            "flake8",
            "pytest",
            "ipywidgets"
        ]
        
        for package in dev_packages:
            self.install_with_pip(package, env_name)
    
    def install_with_pip(self, package, env_name=None):
        """Install package using pip"""
        try:
            if env_name:
                # Activate environment and install
                if self.system == "windows":
                    activate_cmd = f"conda activate {env_name} && pip install {package}"
                    subprocess.run(activate_cmd, shell=True, check=True)
                else:
                    activate_cmd = f"source activate {env_name} && pip install {package}"
                    subprocess.run(['bash', '-c', activate_cmd], check=True)
            else:
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            print(f"✓ Installed: {package}")
        except subprocess.CalledProcessError:
            print(f"✗ Failed to install: {package}")
    
    def post_installation_check(self):
        """Verify installation"""
        print("\n🔍 Running Post-Installation Checks...")
        
        test_imports = [
            "geopandas", "rasterio", "folium", "googlemaps", 
            "geopy", "shapely", "fiona", "pyproj"
        ]
        
        for lib in test_imports:
            try:
                if env_name:
                    if self.system == "windows":
                        cmd = f"conda activate {env_name} && python -c \"import {lib}; print(f'✓ {lib}: {lib.__version__}')\""
                        subprocess.run(cmd, shell=True, check=True)
                    else:
                        cmd = f"source activate {env_name} && python -c \"import {lib}; print(f'✓ {lib}: {lib.__version__}')\""
                        subprocess.run(['bash', '-c', cmd], check=True)
                else:
                    subprocess.run([sys.executable, "-c", f"import {lib}; print(f'✓ {lib} imported successfully')"], 
                                 check=True)
            except subprocess.CalledProcessError:
                print(f"✗ Failed to import: {lib}")
    
    def create_desktop_shortcuts(self, env_name):
        """Create desktop shortcuts for quick access"""
        print("\n📝 Creating Desktop Shortcuts...")
        
        # Create Jupyter Lab shortcut
        shortcut_content = f"""#!/bin/bash
# Geo Distribution - Jupyter Lab
conda activate {env_name}
jupyter lab
"""
        
        shortcuts_dir = Path.home() / "GeoDistribution"
        shortcuts_dir.mkdir(exist_ok=True)
        
        if self.system == "windows":
            # Create batch file for Windows
            bat_content = f"""@echo off
call conda activate {env_name}
jupyter lab
pause
"""
            bat_file = shortcuts_dir / "GeoJupyterLab.bat"
            bat_file.write_text(bat_content)
            print(f"✓ Created Windows shortcut: {bat_file}")
        
        else:
            # Create shell script for Linux/Mac
            script_file = shortcuts_dir / "geojupyterlab.sh"
            script_file.write_text(shortcut_content)
            script_file.chmod(0o755)
            print(f"✓ Created shell script: {script_file}")
    
    def install_all(self, env_name="geo-distro", create_shortcuts=True):
        """Main installation method"""
        print("🚀 Starting Geo Distribution Installation...")
        print("=" * 50)
        
        # Check prerequisites
        self.install_method = self.check_prerequisites()
        
        # Create environment
        if self.install_method in ["conda", "mamba"]:
            actual_env = self.create_environment(env_name)
        else:
            actual_env = None
            print("⚠ Installing in current Python environment")
        
        # Install all packages
        self.install_core_geospatial(actual_env)
        time.sleep(1)
        
        self.install_python_geo_libraries(actual_env)
        time.sleep(1)
        
        self.install_web_mapping(actual_env)
        time.sleep(1)
        
        self.install_advanced_analytics(actual_env)
        time.sleep(1)
        
        self.install_google_maps_tools(actual_env)
        time.sleep(1)
        
        self.install_development_tools(actual_env)
        
        # Post-installation
        self.post_installation_check()
        
        if create_shortcuts and actual_env:
            self.create_desktop_shortcuts(actual_env)
        
        print("\n🎉 Installation Complete!")
        print("=" * 50)
        print(f"Environment: {actual_env or 'system'}")
        print("Available tools:")
        print("  • Jupyter Lab (jupyter lab)")
        print("  • GeoPandas, Rasterio, GDAL")
        print("  • Folium, ipyleaflet for web mapping")
        print("  • Google Maps API tools")
        print("  • Advanced spatial analytics")
        
        if actual_env:
            print(f"\nTo activate the environment:")
            print(f"  conda activate {actual_env}")

def main():
    parser = argparse.ArgumentParser(description="Geo Distribution Installer")
    parser.add_argument("--env-name", default="geo-distro", help="Environment name")
    parser.add_argument("--no-shortcuts", action="store_true", help="Skip creating shortcuts")
    
    args = parser.parse_args()
    
    installer = GeoDistroInstaller()
    installer.install_all(
        env_name=args.env_name,
        create_shortcuts=not args.no_shortcuts
    )

if __name__ == "__main__":
    main()
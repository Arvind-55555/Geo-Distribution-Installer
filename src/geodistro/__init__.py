"""
Geo Distribution - A comprehensive one-click installation package for geospatial libraries
"""

__version__ = "0.1.0"
__author__ = "Arvind"
__email__ = "arvind.saane.111@gmail.com"

from geodistro.installer import GeoDistroInstaller
from geodistro.verifier import verify_installation

__all__ = ["GeoDistroInstaller", "verify_installation"]
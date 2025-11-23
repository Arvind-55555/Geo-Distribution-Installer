import pytest
from geodistro.installer import GeoDistroInstaller
from geodistro.core import GeoDistroConfig

def test_config():
    """Test configuration values"""
    config = GeoDistroConfig()
    assert config.ENV_NAME == "geo-distro"
    assert len(config.CORE_GEOSPATIAL) > 0

def test_installer_initialization():
    """Test installer initialization"""
    installer = GeoDistroInstaller(verbose=False)
    assert installer.verbose == False
    assert installer.system in ["windows", "linux", "darwin"]
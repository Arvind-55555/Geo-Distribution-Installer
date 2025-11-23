import pytest
from geodistro.verifier import check_library, verify_installation


def test_check_library():
    """Test library checking functionality"""
    # Test with a library that should exist (standard library)
    success, version = check_library("sys")
    assert success is True
    
    # Test with a non-existent library
    success, version = check_library("nonexistent_library_12345")
    assert success is False


def test_verify_installation():
    """Test verification function exists and is callable"""
    # Just test that the function exists and can be called
    # We don't expect all geospatial libraries to be installed in test environment
    result = verify_installation()
    assert isinstance(result, bool)

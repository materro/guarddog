from guarddog.__version__ import __version__

def test_version():
    """Check if version is set correctly"""
    assert __version__ is not None

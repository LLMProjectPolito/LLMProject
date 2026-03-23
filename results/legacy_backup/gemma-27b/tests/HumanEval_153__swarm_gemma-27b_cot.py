import pytest

def test_empty_extensions_list():
    """Test case for when the extensions list is empty."""
    assert Strongest_Extension("MyClass", []) == "MyClass.None"
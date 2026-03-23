import pytest
import math

def test_empty_extensions_list():
    """Test case for an empty list of extensions."""
    assert Strongest_Extension("MyClass", []) == "MyClass.None"
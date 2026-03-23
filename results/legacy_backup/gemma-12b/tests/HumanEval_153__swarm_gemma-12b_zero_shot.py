import pytest
import math

def test_empty_extensions_list():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"
import pytest
import math

def test_basic():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_empty_extensions_list():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"
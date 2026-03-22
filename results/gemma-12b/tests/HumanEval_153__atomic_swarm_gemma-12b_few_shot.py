import pytest
import math

def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension("MyClass", ["AAAA", "BBBB", "CCCC"]) == "MyClass.AAAA"

def test_strongest_extension_same_strength():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"
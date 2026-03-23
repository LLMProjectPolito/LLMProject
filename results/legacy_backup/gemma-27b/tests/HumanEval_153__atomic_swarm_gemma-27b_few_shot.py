import pytest
import math

def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("Class", []) == "Class."

def test_strongest_extension_tie():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
import pytest
import math

def test_Strongest_Extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_Strongest_Extension():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('Test', ['Test', 'Test2']) == 'Test.Test'
    assert Strongest_Extension('Class', ['Class', 'Class2']) == 'Class.Class'
    assert Strongest_Extension('Empty', []) == 'Empty.Empty'

def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
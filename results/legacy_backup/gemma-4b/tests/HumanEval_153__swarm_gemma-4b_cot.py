import pytest
import math

def test_Strongest_Extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_Strongest_Extension_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_Strongest_Extension_empty_extensions():
    assert Strongest_Extension('Class', []) == 'Class.None'

def test_Strongest_Extension_all_uppercase():
    assert Strongest_Extension('Upper', ['ABC', 'DEF']) == 'Upper.ABC'

def test_Strongest_Extension_all_lowercase():
    assert Strongest_Extension('Lower', ['abc', 'def']) == 'Lower.abc'

def test_Strongest_Extension_mixed_case():
    assert Strongest_Extension('Mixed', ['aBc', 'DeF']) == 'Mixed.aBc'

def test_Strongest_Extension_single_extension():
    assert Strongest_Extension('Single', ['Extension']) == 'Single.Extension'
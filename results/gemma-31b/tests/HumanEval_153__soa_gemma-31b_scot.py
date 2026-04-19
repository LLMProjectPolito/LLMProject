
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

import pytest

def test_strongest_extension_basic():
    """Test basic functionality with a clear winner."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie_break():
    """Test that the first extension is chosen in case of a tie in strength."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_uppercase():
    """Test extensions that are all uppercase."""
    assert Strongest_Extension('Base', ['AAA', 'BB', 'C']) == 'Base.AAA'

def test_strongest_extension_all_lowercase():
    """Test extensions that are all lowercase (negative strength)."""
    assert Strongest_Extension('Base', ['abc', 'de', 'f']) == 'Base.f' # f: 0-1=-1, de: 0-2=-2, abc: 0-3=-3

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_strongest_extension_mixed_case_tie():
    """Test tie-breaking with mixed case strings."""
    # 'Ab' -> 1-1 = 0
    # 'Ba' -> 1-1 = 0
    # 'XY' -> 2-0 = 2
    # 'ZW' -> 2-0 = 2
    assert Strongest_Extension('Test', ['Ab', 'Ba', 'XY', 'ZW']) == 'Test.XY'

def test_strongest_extension_non_alpha():
    """Test extensions containing non-alphabetic characters (should be ignored)."""
    # 'A1' -> 1-0 = 1
    # 'a1' -> 0-1 = -1
    # 'A!' -> 1-0 = 1
    assert Strongest_Extension('Data', ['A1', 'a1', 'A!']) == 'Data.A1'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("MyClass", ["a", "b", "c"], "MyClass.a"), # All -1, pick first
    ("MyClass", ["A", "B", "C"], "MyClass.A"), # All 1, pick first
    ("MyClass", ["aB", "Ab"], "MyClass.aB"),   # Both 0, pick first
    ("MyClass", ["ABC", "abc"], "MyClass.ABC"), # 3 vs -3
    ("MyClass", ["", ""], "MyClass."),         # Empty strings: 0-0=0, pick first
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
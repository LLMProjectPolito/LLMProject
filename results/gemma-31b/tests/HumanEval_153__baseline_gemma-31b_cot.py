
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
    """Test the basic functionality with the provided examples."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_tie_break():
    """Test that the first extension is chosen when strengths are equal."""
    # 'AAA' strength: 3-0 = 3
    # 'BBB' strength: 3-0 = 3
    # 'CCC' strength: 3-0 = 3
    assert Strongest_Extension('Class', ['AAA', 'BBB', 'CCC']) == 'Class.AAA'
    
    # 'Ab' strength: 1-1 = 0
    # 'Cd' strength: 1-1 = 0
    assert Strongest_Extension('Class', ['Ab', 'Cd']) == 'Class.Ab'

def test_strongest_extension_all_lowercase():
    """Test extensions that consist only of lowercase letters (negative strength)."""
    # 'abc' strength: 0-3 = -3
    # 'a' strength: 0-1 = -1
    # 'abcd' strength: 0-4 = -4
    assert Strongest_Extension('Class', ['abc', 'a', 'abcd']) == 'Class.a'

def test_strongest_extension_all_uppercase():
    """Test extensions that consist only of uppercase letters (positive strength)."""
    # 'A' strength: 1-0 = 1
    # 'AA' strength: 2-0 = 2
    # 'AAA' strength: 3-0 = 3
    assert Strongest_Extension('Class', ['A', 'AA', 'AAA']) == 'Class.AAA'

def test_strongest_extension_mixed_case():
    """Test extensions with a mix of upper and lower case."""
    # 'aB' strength: 1-1 = 0
    # 'AB' strength: 2-0 = 2
    # 'ab' strength: 0-2 = -2
    assert Strongest_Extension('Class', ['aB', 'AB', 'ab']) == 'Class.AB'

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_strongest_extension_non_alpha():
    """Test extensions containing non-alphabetic characters."""
    # 'A1' strength: 1-0 = 1
    # 'a1' strength: 0-1 = -1
    # '123' strength: 0-0 = 0
    assert Strongest_Extension('Class', ['A1', 'a1', '123']) == 'Class.A1'
    assert Strongest_Extension('Class', ['a1', '123']) == 'Class.123'

def test_strongest_extension_empty_string_extension():
    """Test extensions that are empty strings."""
    # '' strength: 0-0 = 0
    # 'a' strength: 0-1 = -1
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'
    # 'A' strength: 1-0 = 1
    # '' strength: 0-0 = 0
    assert Strongest_Extension('Class', ['A', '']) == 'Class.A'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Test", ["Upper", "lower", "MIXED"], "Test.MIXED"), # Upper: 1-4=-3, lower: 0-5=-5, MIXED: 5-0=5
    ("Test", ["a", "b", "c"], "Test.a"), # All -1, pick first
    ("Test", ["A", "B", "C"], "Test.A"), # All 1, pick first
    ("Test", ["Aa", "Bb", "Cc"], "Test.Aa"), # All 0, pick first
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
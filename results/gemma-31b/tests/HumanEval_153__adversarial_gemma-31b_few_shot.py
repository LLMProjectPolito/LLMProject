
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
    """Tests the basic functionality provided in the problem description."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_tie_breaking():
    """
    Tests that if two extensions have the same strength, 
    the one appearing first in the list is chosen.
    """
    # 'AA' strength: 2-0 = 2
    # 'BB' strength: 2-0 = 2
    assert Strongest_Extension('my_class', ['AA', 'BB']) == 'my_class.AA'
    
    # 'a' strength: 0-1 = -1
    # 'b' strength: 0-1 = -1
    assert Strongest_Extension('my_class', ['a', 'b']) == 'my_class.a'

def test_strongest_extension_all_lowercase():
    """Tests behavior when all extensions are lowercase (negative strengths)."""
    # 'abc' strength: 0-3 = -3
    # 'abcd' strength: 0-4 = -4
    # -3 is greater than -4
    assert Strongest_Extension('Test', ['abc', 'abcd']) == 'Test.abc'

def test_strongest_extension_all_uppercase():
    """Tests behavior when all extensions are uppercase (positive strengths)."""
    # 'A' strength: 1-0 = 1
    # 'ABC' strength: 3-0 = 3
    assert Strongest_Extension('Test', ['A', 'ABC']) == 'Test.ABC'

def test_strongest_extension_single_element():
    """Tests a list containing only one extension."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_strongest_extension_non_alpha_chars():
    """
    Tests that numbers and symbols are ignored in the strength calculation 
    (only uppercase and lowercase letters should count).
    """
    # 'A1' strength: 1-0 = 1
    # 'a1' strength: 0-1 = -1
    # '123' strength: 0-0 = 0
    assert Strongest_Extension('Class', ['a1', '123', 'A1']) == 'Class.A1'
    assert Strongest_Extension('Class', ['a1', '123']) == 'Class.123'

def test_strongest_extension_empty_strings():
    """Tests behavior with empty strings as extensions."""
    # '' strength: 0-0 = 0
    # 'a' strength: 0-1 = -1
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Base", ["UPPER", "lower"], "Base.UPPER"),
    ("Base", ["lower", "UPPER"], "Base.UPPER"),
    ("Base", ["MixedCase", "ALLCAPS"], "Base.ALLCAPS"),
    ("Base", ["alllow", "alllow"], "Base.alllow"),
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    """General regression suite for various combinations."""
    assert Strongest_Extension(class_name, extensions) == expected
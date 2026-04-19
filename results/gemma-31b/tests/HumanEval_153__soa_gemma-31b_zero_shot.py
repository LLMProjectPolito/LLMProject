
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
    """Test the provided example cases."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_uppercase():
    """Test when all extensions are uppercase (strength = length)."""
    assert Strongest_Extension('Class', ['A', 'BB', 'CCC']) == 'Class.CCC'
    assert Strongest_Extension('Class', ['CCC', 'BB', 'A']) == 'Class.CCC'

def test_strongest_extension_all_lowercase():
    """Test when all extensions are lowercase (strength = -length)."""
    assert Strongest_Extension('Class', ['a', 'bb', 'ccc']) == 'Class.a'
    assert Strongest_Extension('Class', ['ccc', 'bb', 'a']) == 'Class.a'

def test_strongest_extension_tie_breaking():
    """Test that the first extension is chosen in case of a tie."""
    # 'AA' strength: 2-0=2; 'BB' strength: 2-0=2; 'CC' strength: 2-0=2
    assert Strongest_Extension('Class', ['AA', 'BB', 'CC']) == 'Class.AA'
    # 'Ab' strength: 1-1=0; 'Cd' strength: 1-1=0
    assert Strongest_Extension('Class', ['Ab', 'Cd']) == 'Class.Ab'

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_strongest_extension_mixed_case_negative_strength():
    """Test cases where all strengths are negative."""
    # 'abcD' : 1-3 = -2
    # 'abCD' : 2-2 = 0
    # 'abcd' : 0-4 = -4
    assert Strongest_Extension('Class', ['abcD', 'abCD', 'abcd']) == 'Class.abCD'

def test_strongest_extension_non_alpha_chars():
    """
    Test how the function handles non-alphabetic characters.
    Based on the prompt, only uppercase and lowercase letters should be counted.
    """
    # 'A1' : CAP=1, SM=0 -> 1
    # 'a1' : CAP=0, SM=1 -> -1
    # '11' : CAP=0, SM=0 -> 0
    assert Strongest_Extension('Class', ['A1', 'a1', '11']) == 'Class.A1'
    assert Strongest_Extension('Class', ['a1', '11']) == 'Class.11'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Test", ["UPPER", "lower", "Mixed"], "Test.UPPER"),
    ("Test", ["lower", "Mixed", "UPPER"], "Test.UPPER"),
    ("Test", ["aB", "cD", "eF"], "Test.aB"),
    ("Test", ["ABC", "def", "GHI"], "Test.ABC"),
    ("Test", ["abc", "def", "ghi"], "Test.abc"),
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
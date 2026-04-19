
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
    """Test when all extensions are uppercase."""
    assert Strongest_Extension('Base', ['A', 'BB', 'CCC']) == 'Base.CCC'
    assert Strongest_Extension('Base', ['CCC', 'BB', 'A']) == 'Base.CCC'

def test_strongest_extension_all_lowercase():
    """Test when all extensions are lowercase."""
    # 'a' strength: 0-1 = -1
    # 'aa' strength: 0-2 = -2
    # 'aaa' strength: 0-3 = -3
    assert Strongest_Extension('Base', ['a', 'aa', 'aaa']) == 'Base.a'

def test_strongest_extension_tie_breaking():
    """Test that the first extension is chosen in case of a tie."""
    # 'Ab' strength: 1-1 = 0
    # 'Cd' strength: 1-1 = 0
    # 'Ef' strength: 1-1 = 0
    assert Strongest_Extension('Base', ['Ab', 'Cd', 'Ef']) == 'Base.Ab'
    # 'AA' strength: 2-0 = 2
    # 'BB' strength: 2-0 = 2
    assert Strongest_Extension('Base', ['AA', 'BB']) == 'Base.AA'

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('Base', ['OnlyOne']) == 'Base.OnlyOne'

def test_strongest_extension_mixed_case():
    """Test with a variety of mixed case strengths."""
    # 'ABC' : 3-0 = 3
    # 'abc' : 0-3 = -3
    # 'AbC' : 2-1 = 1
    # 'aBc' : 1-2 = -1
    assert Strongest_Extension('Base', ['abc', 'aBc', 'AbC', 'ABC']) == 'Base.ABC'
    assert Strongest_Extension('Base', ['ABC', 'AbC', 'aBc', 'abc']) == 'Base.ABC'

def test_strongest_extension_non_alpha():
    """Test that non-alphabetic characters are ignored in strength calculation."""
    # 'A1' : 1-0 = 1
    # 'a1' : 0-1 = -1
    # '123' : 0-0 = 0
    assert Strongest_Extension('Base', ['a1', '123', 'A1']) == 'Base.A1'
    assert Strongest_Extension('Base', ['123', 'a1']) == 'Base.123'

def test_strongest_extension_empty_strings():
    """Test behavior with empty strings as extensions."""
    # '' strength: 0-0 = 0
    # 'a' strength: 0-1 = -1
    assert Strongest_Extension('Base', ['', 'a']) == 'Base.'
    # 'a' strength: -1
    # '' strength: 0
    assert Strongest_Extension('Base', ['a', '']) == 'Base.'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Test", ["UPPER", "lower", "Mixed"], "Test.UPPER"),
    ("Test", ["lower", "Mixed", "UPPER"], "Test.UPPER"),
    ("Test", ["Mixed", "Mixed2"], "Test.Mixed"), # Mixed: 1-4=-3, Mixed2: 1-4=-3 (Tie)
    ("Test", ["A", "B", "C"], "Test.A"), # Tie
    ("Test", ["a", "b", "c"], "Test.a"), # Tie
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
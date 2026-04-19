
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
    """Test the provided example case."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie_breaker():
    """Test that the first extension is chosen in case of a tie in strength."""
    # 'AA' strength: 2-0 = 2, 'BB' strength: 2-0 = 2, 'CC' strength: 2-0 = 2
    assert Strongest_Extension('Class', ['AA', 'BB', 'CC']) == 'Class.AA'
    # 'Ab' strength: 1-1 = 0, 'Cd' strength: 1-1 = 0
    assert Strongest_Extension('Class', ['Ab', 'Cd']) == 'Class.Ab'

def test_strongest_extension_all_lowercase():
    """Test cases where extensions consist only of lowercase letters (negative strengths)."""
    # 'abc' = -3, 'de' = -2, 'fghij' = -5. Max is -2.
    assert Strongest_Extension('Base', ['abc', 'de', 'fghij']) == 'Base.de'
    # Tie case: 'abc' = -3, 'def' = -3. Pick first.
    assert Strongest_Extension('Test', ['abc', 'def']) == 'Test.abc'

def test_strongest_extension_all_uppercase():
    """Test cases where extensions consist only of uppercase letters (positive strengths)."""
    # 'A' = 1, 'BB' = 2, 'CCC' = 3. Max is 3.
    assert Strongest_Extension('Base', ['A', 'BB', 'CCC']) == 'Base.CCC'
    # Tie case: 'AAA' = 3, 'BBB' = 3. Pick first.
    assert Strongest_Extension('Test', ['AAA', 'BBB']) == 'Test.AAA'

def test_strongest_extension_mixed_casing():
    """Test a variety of mixed casing scenarios."""
    # 'AbC' -> 2-1 = 1, 'aBc' -> 1-2 = -1, 'ABC' -> 3-0 = 3
    assert Strongest_Extension('Class', ['AbC', 'aBc', 'ABC']) == 'Class.ABC'
    # 'a' -> -1, 'A' -> 1
    assert Strongest_Extension('Class', ['a', 'A']) == 'Class.A'

def test_strongest_extension_non_alphabetic():
    """Test extensions containing non-alphabetic characters (should not affect counts)."""
    # 'A1' -> 1-0 = 1, 'a1' -> 0-1 = -1, '123' -> 0-0 = 0
    assert Strongest_Extension('Class', ['a1', '123', 'A1']) == 'Class.A1'
    # '123' -> 0, 'a1' -> -1
    assert Strongest_Extension('Class', ['123', 'a1']) == 'Class.123'

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('MyClass', ['OnlyOne']) == 'MyClass.OnlyOne'

def test_strongest_extension_empty_strings():
    """Test extensions that are empty strings."""
    # Empty string: 0-0 = 0, 'a': 0-1 = -1
    assert Strongest_Extension('Base', ['', 'a']) == 'Base.'
    # Empty string: 0, 'A': 1-0 = 1
    assert Strongest_Extension('Base', ['', 'A']) == 'Base.A'

def test_strongest_extension_large_input():
    """Test with a larger list of extensions to ensure robustness."""
    extensions = ['a' * 100, 'A' * 100, 'b' * 50 + 'B' * 50]
    # 'a'*100: -100, 'A'*100: 100, 'b'*50 + 'B'*50: 0
    assert Strongest_Extension('BigClass', extensions) == 'BigClass.' + 'A' * 100

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Test", ["ABC", "def"], "Test.ABC"),
    ("Test", ["def", "ABC"], "Test.ABC"),
    ("Test", ["AbC", "aBC"], "Test.AbC"), # Both 1, pick first
    ("Test", ["a", "b", "c"], "Test.a"), # All -1, pick first
    ("Test", ["A", "B", "C"], "Test.A"), # All 1, pick first
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
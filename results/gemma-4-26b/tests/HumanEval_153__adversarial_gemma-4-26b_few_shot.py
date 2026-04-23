
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

# The function signature for reference
# def Strongest_Extension(class_name: str, extensions: list[str]) -> str:

def test_strongest_extension_basic():
    """Tests standard functionality with varying strengths."""
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"
    assert Strongest_Extension("Base", ["abc", "ABC", "aBc"]) == "Base.ABC"

def test_strongest_extension_tie_breaker():
    """
    Requirement: If there are two or more extensions with the same strength, 
    choose the one that comes first in the list.
    """
    # 'AA' strength: 2-0 = 2. 'CC' strength: 2-0 = 2. 'AA' is first.
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"
    # All have strength 0
    assert Strongest_Extension("Tie", ["Ab", "aB", "Ab"]) == "Tie.Ab"

def test_strongest_extension_negative_strength():
    """Tests cases where all extensions have negative strength (more lowercase than uppercase)."""
    # 'abc' strength: 0-3 = -3. 'aB' strength: 1-1 = 0.
    assert Strongest_Extension("Neg", ["abc", "def", "aB"]) == "Neg.aB"
    # All negative
    assert Strongest_Extension("AllNeg", ["aaa", "bbb", "ccc"]) == "AllNeg.aaa"

def test_strongest_extension_single_element():
    """Tests a list containing only one extension."""
    assert Strongest_Extension("Single", ["OnlyOne"]) == "Single.OnlyOne"
    assert Strongest_Extension("Single", ["onlyone"]) == "Single.onlyone"

def test_strongest_extension_non_alphabetic():
    """
    Tests how the function handles numbers and symbols.
    The prompt defines strength based on CAP (uppercase) and SM (lowercase).
    Non-alphabetic characters should not contribute to either count.
    """
    # 'A1!' strength: 1-0 = 1. 'a1!' strength: 0-1 = -1.
    assert Strongest_Extension("Special", ["A1!", "a1!"]) == "Special.A1!"
    # '123' strength: 0-0 = 0.
    assert Strongest_Extension("Numbers", ["123", "A"]) == "Numbers.A"

def test_strongest_extension_empty_strings():
    """Tests behavior with empty strings within the list."""
    # '' strength: 0-0 = 0. 'A' strength: 1-0 = 1.
    assert Strongest_Extension("EmptyStr", ["", "A"]) == "EmptyStr.A"
    # '' strength: 0. 'a' strength: -1.
    assert Strongest_Extension("EmptyStrNeg", ["", "a"]) == "EmptyStr."

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Class", ["A", "B", "C"], "Class.A"),
    ("Class", ["a", "b", "c"], "Class.a"),
    ("Class", ["Aa", "Bb", "Cc"], "Class.Aa"),
    ("Class", ["AAA", "aaa"], "Class.AAA"),
])
def test_parameterized_strengths(class_name, extensions, expected):
    """Bulk testing of various strength combinations."""
    assert Strongest_Extension(class_name, extensions) == expected

def test_strongest_extension_empty_list():
    """
    Edge Case: What happens if the extensions list is empty?
    The prompt doesn't specify, but a robust function should handle this 
    without crashing (e.g., returning None or raising a specific error).
    """
    with pytest.raises((ValueError, IndexError, AttributeError)):
        # Depending on implementation, this might raise an error.
        # If the implementation returns None, change this to:
        # assert Strongest_Extension("Empty", []) is None
        Strongest_Extension("Empty", [])

def test_class_name_formatting():
    """Ensures the class name is prepended correctly even with unusual characters."""
    assert Strongest_Extension("My_Class_123", ["Ext"]) == "My_Class_123.Ext"
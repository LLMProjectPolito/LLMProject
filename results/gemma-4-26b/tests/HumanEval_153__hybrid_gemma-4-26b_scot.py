
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

# Note: Strongest_Extension is assumed to be available in the environment.

@pytest.mark.parametrize("class_name, extensions, expected", [
    # --- Docstring Examples ---
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
    ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
    
    # --- Basic Strength Scenarios ---
    ("PositiveTest", ['AAA', 'B', 'CC'], "PositiveTest.AAA"),   # 3, 1, 2
    ("NegativeTest", ['abc', 'defg', 'h'], "NegativeTest.h"),   # -3, -4, -1
    ("ZeroStrength", ['Ab', 'aB', 'cC', 'Cc'], "ZeroStrength.Ab"), # All 0
    ("MixedStrength", ["aA", "Aa", "AA", "aa"], "Mixed.AA"),    # -0, 0, 2, -2
    ("Complex", ["aB1c", "Ab2C", "ABC"], "Complex.ABC"),        # 0, 2, 3
    
    # --- Single Element ---
    ("Single", ['OnlyOne'], "Single.OnlyOne"),
    ("SingleLower", ['onlyone'], "Single.onlyone"),
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    """Tests standard functional requirements and docstring examples using parametrization."""
    assert Strongest_Extension(class_name, extensions) == expected


def test_tie_breaking_logic():
    """Explicitly verifies the 'first in list' rule for various tie scenarios."""
    # Tie between 2nd and 3rd elements
    assert Strongest_Extension('Class', ['a', 'A', 'B', 'c']) == 'Class.A'
    
    # All elements have identical strength (0)
    assert Strongest_Extension('Tie', ['Ab', 'Ba', 'aB', 'Ab']) == 'Tie.Ab'
    
    # All elements have identical strength (positive)
    assert Strongest_Extension('Same', ['AAA', 'BBB', 'CCC']) == 'Same.AAA'
    
    # Tie between elements with negative strength
    # 'abc' (-3), 'def' (-3), 'gh' (-2) -> 'gh' wins
    # 'abc' (-3), 'def' (-3), 'g' (-1) -> 'g' wins
    assert Strongest_Extension('NegTie', ['abc', 'def', 'g']) == 'NegTie.g'


def test_character_and_format_edge_cases():
    """Tests handling of non-alphabetic characters, empty strings, and class name formatting."""
    # Non-alphabetic characters ignored in strength
    # 'A!B' (2-0=2), 'A1b' (1-1=0), 'A_b' (1-1=0)
    assert Strongest_Extension('Data', ['A1b', 'A!B', 'A_b']) == 'Data.A!B'
    
    # Numeric/Symbol only strings (strength 0)
    assert Strongest_Extension('Numeric', ['123', 'ABC', '!!!']) == 'Numeric.ABC'
    
    # Empty string as an extension (strength 0)
    assert Strongest_Extension('EmptyExt', [""], "EmptyExt.")
    
    # Empty string inside a list (strength 0)
    # '' (0), 'A' (1), 'a' (-1)
    assert Strongest_Extension('EmptyInList', ['', 'A', 'a'], 'EmptyInList.A')
    
    # Special characters in class name
    assert Strongest_Extension('Special_Class', ['Ext'], "Special_Class.Ext")


def test_extreme_values():
    """Tests stability with very large strings and extreme strength differences."""
    class_name = "Extreme"
    
    # Extreme difference in strength
    # a...a: -20, A: 1, a...aA: -19
    extensions = ["aaaaaaaaaaaaaaaaaaaa", "A", "aaaaaaaaaaaaaaaaaaaaA"]
    assert Strongest_Extension(class_name, extensions) == "Extreme.A"
    
    # Very long strings
    long_upper = "A" * 1000
    long_lower = "a" * 1000
    assert Strongest_Extension("Long", [long_lower, long_upper]) == "Long." + long_upper
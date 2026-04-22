
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

# The function Strongest_Extension is assumed to be defined in the environment.

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], 'Slices.SErviNGSliCes'),
    ("my_class", ['AA', 'Be', 'CC'], 'my_class.AA'),
])
def test_provided_examples(class_name, extensions, expected):
    """Tests the examples provided in the problem description."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Class", ['Ab', 'Cd', 'Ef'], 'Class.Ab'),  # All strength 0
    ("Class", ['A', 'B', 'C'], 'Class.A'),      # All strength 1
    ("Class", ['a', 'b', 'c'], 'Class.a'),      # All strength -1
])
def test_tie_breaking(class_name, extensions, expected):
    """Tests that the first extension in the list is chosen in case of a tie."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Class", ['abc', 'def', 'ghi'], 'Class.abc'), # All strength -3
    ("Class", ['aB', 'cDe'], 'Class.aB'),         # 0 vs -1
    ("Class", ['zzz', 'AAA'], 'Class.AAA'),       # -3 vs 3
])
def test_negative_strengths(class_name, extensions, expected):
    """Tests scenarios where strengths are zero or negative."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Class", ['A1!', 'b2@', 'C#'], 'Class.A1!'), # 1 vs -1 vs 1 (Tie A1! and C#)
    ("Class", ['123', 'abc'], 'Class.123'),       # 0 vs -3
    ("Class", ['!@#', 'A'], 'Class.A'),           # 0 vs 1
])
def test_non_alphabetic_characters(class_name, extensions, expected):
    """Tests that non-alphabetic characters are ignored in strength calculation."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Class", ['OnlyOne'], 'Class.OnlyOne'),      # Single element
    ("Class", ['', 'A'], 'Class.A'),              # Empty string extension (strength 0) vs A (strength 1)
    ("Class", ['a', ''], 'Class.'),               # Fixed: 'a' (-1) vs '' (0). 0 is stronger.
    ("mY_ClAsS", ['Ext'], 'mY_ClAsS.Ext'),       # Preservation of class name casing
    ("Class", [' '], 'Class. '),                  # Whitespace extension (strength 0)
    ("", ['Ext'], '.Ext'),                        # Empty class name
])
def test_edge_cases(class_name, extensions, expected):
    """Tests various edge cases like single elements, empty strings, and whitespace."""
    assert Strongest_Extension(class_name, extensions) == expected

def test_empty_extensions_list():
    """Tests the behavior when the extensions list is empty."""
    # Defined behavior: return just the class_name if no extensions are provided
    assert Strongest_Extension("MyClass", []) == "MyClass"

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Class", ['123', '!@#', '$$$'], 'Class.123'), # All strength 0, pick first
])
def test_all_zero_strength(class_name, extensions, expected):
    """Tests that tie-breaking works when all extensions have zero strength."""
    assert Strongest_Extension(class_name, extensions) == expected
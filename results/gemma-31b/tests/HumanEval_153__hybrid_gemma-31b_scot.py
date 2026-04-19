
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
    # Provided examples from the problem description
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
    ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
])
def test_provided_examples(class_name, extensions, expected):
    """Verify the function works with the examples provided in the docstring."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    # Positive strength tie: All strength 3, pick first
    ("MyClass", ["ABC", "DEF", "GHI"], "MyClass.ABC"),
    # Negative strength tie: All strength -3, pick first
    ("MyClass", ["abc", "def", "ghi"], "MyClass.abc"),
    # Zero strength tie: All strength 0, pick first
    ("MyClass", ["Ab", "Ba", "Cd"], "MyClass.Ab"),
    # Mixed tie: 'aB' (0) and 'Ab' (0), pick first
    ("Class", ["aB", "Ab"], "Class.aB"),
])
def test_tie_breaking(class_name, extensions, expected):
    """Verify that the first extension is chosen when strengths are equal."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    # All lowercase: 'de' (-2) is stronger than 'abc' (-3) or 'fghij' (-5)
    ("Base", ["abc", "de", "fghij"], "Base.de"),
    # All uppercase: 'FGHIJ' (5) is strongest
    ("Base", ["ABC", "DE", "FGHIJ"], "Base.FGHIJ"),
    # Single uppercase vs single lowercase
    ("Test", ["a", "B"], "Test.B"),
])
def test_case_extremes(class_name, extensions, expected):
    """Verify behavior with purely uppercase or purely lowercase extensions."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    # 'A2B' (2-0=2) is strongest; 'A1b' (1-1=0), '345' (0), '!!!' (0)
    ("Class", ["A1b", "A2B", "345", "!!!"], "Class.A2B"),
    # All strength 1, pick first
    ("Class1", ["A123", "B!!!", "C456"], "Class1.A123"),
    # All strength 0, pick first
    ("Class1", ["123", "456"], "Class1.123"),
])
def test_non_alphabetic_characters(class_name, extensions, expected):
    """Verify that numbers and symbols are ignored in strength calculations."""
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    # Single extension in list
    ("Unique", ["OnlyOne"], "Unique.OnlyOne"),
    # Empty string as the strongest (strength 0)
    ("EmptyTest", ["", "low"], "EmptyTest."),
    # Empty string as the weakest
    ("EmptyTest", ["", "UP"], "EmptyTest.UP"),
    # Only empty strings
    ("EmptyTest", ["", ""], "EmptyTest."),
])
def test_edge_cases(class_name, extensions, expected):
    """Verify behavior with empty strings and minimal lists."""
    assert Strongest_Extension(class_name, extensions) == expected

def test_complex_strength_gradient():
    """
    Test a complex mix of extensions to ensure accuracy of the formula 
    across a wide range of strengths.
    """
    class_name = "Core"
    # 'Strong' : 1U - 5L = -4
    # 'EXT'    : 3U - 0L = 3
    # 'ext'    : 0U - 3L = -3
    # 'Mixed'  : 1U - 4L = -3
    # 'POWER'  : 5U - 0L = 5
    # 'a'      : 0U - 1L = -1
    extensions = ['Strong', 'EXT', 'ext', 'Mixed', 'POWER', 'a']
    assert Strongest_Extension(class_name, extensions) == "Core.POWER"

def test_all_same_strength_stability():
    """
    Explicitly test that the very first item is returned when all 
    extensions have the exact same strength.
    """
    class_name = "Same"
    extensions = ["Ab", "Cd", "Ef", "Gh"] # All strength 0
    assert Strongest_Extension(class_name, extensions) == "Same.Ab"

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

@pytest.mark.parametrize("class_name, extensions, expected", [
    # Provided Example 1
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], 'Slices.SErviNGSliCes'),
    # Provided Example 2
    ('my_class', ['AA', 'Be', 'CC'], 'my_class.AA'),
    # Tie-breaking: same strength, pick the first one in the list
    ("TestClass", ["Ab", "Cd", "Ef"], "TestClass.Ab"),
    ("TestClass", ["A", "B", "C"], "TestClass.A"),
    # All negative strengths
    ("Negative", ["abc", "def", "ghi"], "Negative.abc"),
    # All zero strength (equal CAP and SM)
    ("Zero", ["Ab", "aB", "AaBb"], "Zero.Ab"),
    # Single extension
    ("Single", ["OnlyOne"], "Single.OnlyOne"),
    # Mixed characters (numbers and symbols should not affect CAP or SM)
    ("Symbols", ["A1!", "b2@", "C3#"], "Symbols.A1!"),
    ("Symbols2", ["a1!", "A2@"], "Symbols2.A2@"),
    # Large difference in strength
    ("Strength", ["AAAAA", "aaaaa", "AaAaA"], "Strength.AAAAA"),
    # Empty strings in extensions (strength 0)
    ("Empty", ["", "A", "a"], "Empty.A"),
])
def test_strongest_extension(class_name, extensions, expected):
    """Tests various scenarios including ties, negative strengths, and special characters."""
    assert Strongest_Extension(class_name, extensions) == expected

def test_case_sensitivity_of_class_name():
    """Ensures the class name is returned exactly as provided in the output string."""
    assert Strongest_Extension("lowercase", ["UPPER"]) == "lowercase.UPPER"
    assert Strongest_Extension("UPPERCASE", ["lower"]) == "UPPERCASE.lower"
    assert Strongest_Extension("MixedCase", ["EXT"]) == "MixedCase.EXT"

def test_strength_calculation_logic():
    """
    Explicitly verifies the math: CAP - SM.
    'A' -> 1 - 0 = 1
    'a' -> 0 - 1 = -1
    'Aa' -> 1 - 1 = 0
    'AAa' -> 2 - 1 = 1
    """
    # 'AAa' (1) vs 'A' (1) -> 'AAa' is first
    assert Strongest_Extension("Logic", ["AAa", "A"]) == "Logic.AAa"
    # 'AAa' (1) vs 'AAA' (3) -> 'AAA' is stronger
    assert Strongest_Extension("Logic", ["AAa", "AAA"]) == "Logic.AAA"
    # 'a' (-1) vs 'aa' (-2) -> 'a' is stronger
    assert Strongest_Extension("Logic", ["aa", "a"]) == "Logic.a"

def test_non_alphabetic_impact():
    """Verifies that non-alphabetic characters do not count towards CAP or SM."""
    # 'A!' -> CAP=1, SM=0 -> Strength 1
    # 'a?' -> CAP=0, SM=1 -> Strength -1
    # '12' -> CAP=0, SM=0 -> Strength 0
    assert Strongest_Extension("Char", ["12", "A!", "a?"]) == "Char.A!"
    assert Strongest_Extension("Char", ["12", "a?", "A!"]) == "Char.A!"
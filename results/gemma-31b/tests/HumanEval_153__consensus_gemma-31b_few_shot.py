
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
    """Test the example provided in the prompt."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie_breaker():
    """Test that the first occurrence is chosen in case of a tie."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_uppercase():
    """Test where extensions are all uppercase (strength = length)."""
    assert Strongest_Extension('Class', ['A', 'BB', 'CCC']) == 'Class.CCC'
    assert Strongest_Extension('Class', ['CCC', 'BB', 'A']) == 'Class.CCC'

def test_strongest_extension_all_lowercase():
    """Test where extensions are all lowercase (strength = -length)."""
    assert Strongest_Extension('Class', ['aaa', 'bb', 'c']) == 'Class.c'
    assert Strongest_Extension('Class', ['c', 'bb', 'aaa']) == 'Class.c'

def test_strongest_extension_mixed_case():
    """Test a variety of mixed case strengths."""
    # 'High': 1-3 = -2; 'LOW': 3-0 = 3; 'Mid': 1-2 = -1
    assert Strongest_Extension('Test', ['High', 'LOW', 'Mid']) == 'Test.LOW'
    # 'abc' (-3), 'AbC' (2-1=1), 'ABC' (3)
    assert Strongest_Extension('MyClass', ['abc', 'AbC', 'ABC']) == 'MyClass.ABC'
    # 'aB' (1-1=0), 'XYz' (2-1=1)
    assert Strongest_Extension('MyClass', ['aB', 'XYz']) == 'MyClass.XYz'

def test_strongest_extension_single_element():
    """Test with only one extension in the list."""
    assert Strongest_Extension('OnlyOne', ['Extension']) == 'OnlyOne.Extension'

def test_strongest_extension_equal_strength():
    """Test where all extensions have the same strength."""
    # 'Ab', 'Cd', 'Ef' all have strength 1-1 = 0
    assert Strongest_Extension('Equal', ['Ab', 'Cd', 'Ef']) == 'Equal.Ab'

def test_strongest_extension_non_alpha():
    """Test behavior with non-alphabetic characters (they should not count as CAP or SM)."""
    # 'a1' : 0-1 = -1; '11' : 0-0 = 0; 'A1' : 1-0 = 1
    assert Strongest_Extension('Numeric', ['a1', '11', 'A1']) == 'Numeric.A1'

def test_strongest_extension_empty_string():
    """Test when an extension is an empty string."""
    # Empty string strength: 0 - 0 = 0
    # 'a' strength: -1
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'
    # 'A' strength: 1
    assert Strongest_Extension('Class', ['', 'A']) == 'Class.A'

def test_strongest_extension_long_strings():
    """Test with very long extension strings."""
    ext1 = 'A' * 100 + 'a' * 50  # 100 - 50 = 50
    ext2 = 'A' * 100 + 'a' * 60  # 100 - 60 = 40
    assert Strongest_Extension('Long', [ext1, ext2]) == f'Long.{ext1}'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Base", ["UPPER", "lower", "Mixed"], "Base.UPPER"),
    ("Base", ["lower", "Mixed", "UPPER"], "Base.UPPER"),
    ("Base", ["A", "B", "C"], "Base.A"),
    ("Base", ["a", "b", "c"], "Base.a"),
    ("Base", ["aB", "bA"], "Base.aB"),
    ("Alpha", ["Beta", "Gamma", "Delta"], "Alpha.Beta"),
    ("Gamma", ["aB", "bA", "cC"], "Gamma.aB"),
    ("Delta", ["ZZZ", "aaa", "ZzZ"], "Delta.ZZZ"),
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
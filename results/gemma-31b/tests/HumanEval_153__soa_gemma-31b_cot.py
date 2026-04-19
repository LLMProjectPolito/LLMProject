
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
    # Provided example 1
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], 'Slices.SErviNGSliCes'),
    # Provided example 2: Tie-break (AA and CC both have strength 2, AA comes first)
    ("my_class", ['AA', 'Be', 'CC'], 'my_class.AA'),
    # All lowercase: Strength is negative, first one wins tie
    ("TestClass", ['abc', 'def', 'ghi'], 'TestClass.abc'),
    # All uppercase: Strength is positive, first one wins tie
    ("TestClass", ['ABC', 'DEF', 'GHI'], 'TestClass.ABC'),
    # Mixed case with clear winner
    ("MyClass", ['aB', 'ABC', 'abC'], 'MyClass.ABC'),
    # Single extension
    ("Single", ['OnlyOne'], 'Single.OnlyOne'),
    # Extensions with non-alphabetic characters (should not count towards CAP or SM)
    ("Special", ['A1b', 'A2B', 'a3b'], 'Special.A2B'), 
    # Empty string extension (CAP=0, SM=0, strength=0)
    ("Empty", ['', 'a'], 'Empty.'),
    # Strength 0 vs negative strength
    ("Zero", ['aB', 'abc'], 'Zero.aB'),
    # Strength 0 vs positive strength
    ("Positive", ['aB', 'AB'], 'Positive.AB'),
    # Large difference in strength
    ("Diff", ['aaaaaaaaaa', 'AAAAAAAAAA'], 'Diff.AAAAAAAAAA'),
])
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_strongest_extension_tie_breaking():
    """Explicitly test that the first occurrence is returned in case of a tie."""
    class_name = "TieTest"
    # 'Ab' -> 1-1 = 0
    # 'Ba' -> 1-1 = 0
    # 'Cd' -> 1-1 = 0
    extensions = ['Ab', 'Ba', 'Cd']
    assert Strongest_Extension(class_name, extensions) == "TieTest.Ab"

def test_strongest_extension_case_sensitivity():
    """Test that uppercase and lowercase are counted correctly."""
    class_name = "CaseTest"
    # 'a' -> 0-1 = -1
    # 'A' -> 1-0 = 1
    extensions = ['a', 'A']
    assert Strongest_Extension(class_name, extensions) == "CaseTest.A"
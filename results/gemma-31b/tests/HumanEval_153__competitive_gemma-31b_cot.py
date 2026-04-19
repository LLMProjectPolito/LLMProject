
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
    # Provided examples
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], 'Slices.SErviNGSliCes'),
    ("my_class", ['AA', 'Be', 'CC'], 'my_class.AA'),
    
    # Tie-breaking: first occurrence should win
    ("Base", ["AAA", "BBB", "CCC"], "Base.AAA"),
    ("Base", ["abc", "def", "ghi"], "Base.abc"),
    
    # All uppercase (Strength = length)
    ("Class", ["A", "BB", "CCC"], "Class.CCC"),
    
    # All lowercase (Strength = -length)
    ("Class", ["a", "bb", "ccc"], "Class.a"),
    
    # Mixed cases with positive strengths
    ("Class", ["ABCd", "ABCE"], "Class.ABCE"), # 3-1=2 vs 4-0=4
    
    # Mixed cases with negative strengths
    ("Class", ["abcD", "abcdE"], "Class.abcdE"), # 1-3=-2 vs 1-4=-3 -> -2 is stronger
    
    # Single extension
    ("OnlyOne", ["Extension"], "OnlyOne.Extension"),
    
    # Extensions with non-alphabetic characters (should be ignored in CAP/SM count)
    ("Class", ["A1b", "A2b"], "Class.A1b"), # 1-1=0 vs 1-1=0 -> first wins
    ("Class", ["A1", "a1"], "Class.A1"), # 1-0=1 vs 0-1=-1
    
    # Empty strings as extensions
    ("Class", ["", "A"], "Class.A"), # 0-0=0 vs 1-0=1
    ("Class", ["", ""], "Class."), # 0-0=0 vs 0-0=0 -> first wins
])
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_strongest_extension_case_sensitivity():
    # Test that the logic specifically counts uppercase vs lowercase
    # 'aB' -> 1-1 = 0
    # 'Ab' -> 1-1 = 0
    # 'AB' -> 2-0 = 2
    # 'ab' -> 0-2 = -2
    assert Strongest_Extension("Test", ["ab", "aB", "Ab", "AB"]) == "Test.AB"
    assert Strongest_Extension("Test", ["AB", "aB", "Ab", "ab"]) == "Test.AB"
    assert Strongest_Extension("Test", ["ab", "aB", "Ab"]) == "Test.aB"
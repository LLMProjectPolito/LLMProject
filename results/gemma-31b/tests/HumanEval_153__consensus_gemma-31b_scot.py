
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
    
    # Tie-breaking: Same strength, should pick the first one in the list
    ("Base", ["AAA", "BBB"], "Base.AAA"),
    ("Base", ["abc", "def"], "Base.abc"),
    ("Tie", ["Ab", "Ba"], "Tie.Ab"),
    
    # All lowercase extensions (negative strengths)
    ("Class", ["abc", "ab", "abcd"], "Class.ab"), # -3, -2, -4 -> -2 is strongest
    ("Class", ["abc", "de", "f"], "Class.f"),     # -3, -2, -1 -> -1 is strongest
    
    # All uppercase extensions (positive strengths)
    ("Class", ["A", "AB", "ABC"], "Class.ABC"),   # 1, 2, 3 -> 3 is strongest
    ("Base", ["EXT1", "EXT2", "EXT3"], "Base.EXT1"), # Tie-break
    
    # Mixed cases and strengths
    ("Test", ["aB", "Ab", "ABC"], "Test.ABC"),    # 0, 0, 3 -> 3
    ("Test", ["aB", "Ab", "abc"], "Test.aB"),     # 0, 0, -3 -> 0 (first one)
    ("Base", ["Lower", "Zero", "UPPER", "Mixed"], "Base.UPPER"),
    
    # Single extension
    ("Single", ["OnlyOne"], "Single.OnlyOne"),
    
    # Extensions with non-alphabetic characters (should not count towards CAP or SM)
    ("Class", ["A1", "a1", "11"], "Class.A1"),    # 1, -1, 0 -> 1
    ("Base", ["a123", "A!b", "A123"], "Base.A123"), # -1, 0, 1 -> 1
    
    # Empty string extensions (Strength 0)
    ("Class", ["", "a"], "Class."),               # 0, -1 -> 0
    ("Class", ["", "A"], "Class.A"),              # 0, 1 -> 1
    
    # Class name case sensitivity
    ("my_CLASS_name", ["Ext"], "my_CLASS_name.Ext"),
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    """Tests the Strongest_Extension function with various scenarios."""
    assert Strongest_Extension(class_name, extensions) == expected

def test_strongest_extension_long_strings():
    """Tests with longer strings to ensure counting and tie-breaking are robust."""
    # Case 1: Tie-break with long strings
    ext1 = "A" * 100 + "a" * 50  # 100 - 50 = 50
    ext2 = "A" * 60 + "a" * 10   # 60 - 10 = 50
    assert Strongest_Extension("Long", [ext1, ext2]) == f"Long.{ext1}"
    
    # Case 2: Strength difference with long strings
    ext_low = "A" * 100 + "a" * 70  # 30
    ext_high = "A" * 100 + "a" * 40 # 60
    assert Strongest_Extension("LongClass", [ext_low, ext_high]) == f"LongClass.{ext_high}"
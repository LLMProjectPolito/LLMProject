
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

def test_basic_example():
    """Test the example provided in the docstring."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_tie_break():
    """Test that the first extension is chosen in case of a tie in strength."""
    # AA: 2-0=2, Be: 1-1=0, CC: 2-0=2. Tie between AA and CC.
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    # All same strength: 1-1=0. Should pick the first.
    assert Strongest_Extension('Test', ['Ab', 'Cd', 'Ef']) == 'Test.Ab'

def test_all_uppercase():
    """Test extensions consisting only of uppercase letters."""
    # A: 1-0=1, ABC: 3-0=3, AB: 2-0=2
    assert Strongest_Extension('Class', ['A', 'ABC', 'AB']) == 'Class.ABC'

def test_all_lowercase():
    """Test extensions consisting only of lowercase letters."""
    # a: 0-1=-1, abc: 0-3=-3, ab: 0-2=-2
    assert Strongest_Extension('Class', ['a', 'abc', 'ab']) == 'Class.a'

def test_mixed_characters():
    """Test extensions containing non-alphabetic characters (should be ignored in CAP/SM)."""
    # 'A123': CAP=1, SM=0 -> 1
    # 'a123': CAP=0, SM=1 -> -1
    # 'A1a2': CAP=1, SM=1 -> 0
    assert Strongest_Extension('Class', ['a123', 'A1a2', 'A123']) == 'Class.A123'

def test_single_extension():
    """Test with only one extension in the list."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_empty_class_name():
    """Test with an empty class name string."""
    assert Strongest_Extension('', ['Ext1', 'Ext2']) == '.Ext1'

def test_negative_strengths():
    """Test where all extensions have negative strengths."""
    # 'abc': 0-3=-3
    # 'ab': 0-2=-2
    # 'a': 0-1=-1
    assert Strongest_Extension('Class', ['abc', 'ab', 'a']) == 'Class.a'

def test_varying_lengths():
    """Test extensions of significantly different lengths."""
    # 'A': 1-0=1
    # 'aaaaaaaaaaA': 1-10=-9
    assert Strongest_Extension('Class', ['aaaaaaaaaaA', 'A']) == 'Class.A'

def test_case_sensitivity_of_class_name():
    """Ensure the class name is returned exactly as provided."""
    assert Strongest_Extension('my_CLASS_name', ['Ext']) == 'my_CLASS_name.Ext'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Base", ["UPPER", "lower", "Mixed"], "Base.UPPER"),
    ("Base", ["lower", "Mixed", "UPPER"], "Base.UPPER"),
    ("Base", ["Mixed", "UPPER", "lower"], "Base.UPPER"),
    ("Base", ["aB", "bA"], "Base.aB"), # Both 1-1=0, pick first
])
def test_positional_strength(class_name, extensions, expected):
    """Test that the strongest extension is found regardless of its position."""
    assert Strongest_Extension(class_name, extensions) == expected
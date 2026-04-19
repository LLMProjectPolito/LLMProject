
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
    """Test the basic functionality with the provided example."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie_break():
    """Test that the first extension is chosen in case of a tie in strength."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('Base', ['A', 'B', 'C']) == 'Base.A'

def test_strongest_extension_all_uppercase():
    """Test with extensions that are all uppercase; the longest should be strongest."""
    assert Strongest_Extension('Base', ['A', 'BB', 'CCC']) == 'Base.CCC'
    assert Strongest_Extension('Class', ['ABC', 'DEFG', 'HI']) == 'Class.DEFG'

def test_strongest_extension_all_lowercase():
    """Test with extensions that are all lowercase; the shortest should be strongest (least negative)."""
    assert Strongest_Extension('Base', ['abc', 'de', 'f']) == 'Base.f'
    assert Strongest_Extension('Class', ['abc', 'defg', 'hi']) == 'Class.hi'
    assert Strongest_Extension('Neg', ['aaa', 'aa', 'a']) == 'Neg.a'

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('Single', ['OnlyOne']) == 'Single.OnlyOne'

def test_strongest_extension_mixed_case():
    """Test various mixed case scenarios."""
    # 'XyZ': 2-1=1; 'abc': 0-3=-3; 'ABC': 3-0=3
    assert Strongest_Extension('Test', ['XyZ', 'abc', 'ABC']) == 'Test.ABC'
    # 'aB': 1-1=0; 'abB': 1-2=-1; 'abbB': 1-3=-2
    assert Strongest_Extension('Test', ['aB', 'abB', 'abbB']) == 'Test.aB'

def test_strongest_extension_empty_strings():
    """Test behavior when extensions are empty strings (strength 0-0=0)."""
    # Empty strings have strength 0. 'a' has strength -1.
    assert Strongest_Extension('Empty', ['', 'a']) == 'Empty.'
    # Both empty have strength 0, pick first.
    assert Strongest_Extension('Empty', ['', '']) == 'Empty.'
    # 'A' has strength 1, wins over empty string.
    assert Strongest_Extension('Class', ['', 'a', 'A']) == 'Class.A'

def test_strongest_extension_non_alpha():
    """Test extensions containing non-alphabetic characters (should not count towards CAP or SM)."""
    # 'A1': 1-0=1; 'a1': 0-1=-1; '123': 0-0=0
    assert Strongest_Extension('Num', ['A1', 'a1', '123']) == 'Num.A1'
    # '123': 0; '!!!': 0. Tie goes to first.
    assert Strongest_Extension('Num', ['123', '!!!']) == 'Num.123'
    # 'A_B' -> 2-0=2
    assert Strongest_Extension('Class', ['A1', 'a1', '123', 'A_B']) == 'Class.A_B'

def test_strongest_extension_class_name_variations():
    """Test different types of class names."""
    assert Strongest_Extension('my_class_123', ['Ext']) == 'my_class_123.Ext'
    assert Strongest_Extension('', ['Ext']) == '.Ext'

def test_strongest_extension_zero_strength():
    """Test cases where strength is exactly 0."""
    # 'Ab' -> 1-1=0; 'Cd' -> 1-1=0; '123' -> 0-0=0. First one wins.
    assert Strongest_Extension('Class', ['Ab', 'Cd', '123']) == 'Class.Ab'

def test_strongest_extension_very_long_extensions():
    """Test with long strings to ensure stability."""
    ext1 = 'A' * 100 + 'a' * 50  # 100 - 50 = 50
    ext2 = 'A' * 100 + 'a' * 60  # 100 - 60 = 40
    assert Strongest_Extension('LongClass', [ext1, ext2]) == f'LongClass.{ext1}'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Test", ["UPPER", "lower", "Mixed"], "Test.UPPER"),
    ("Test", ["lower", "UPPER", "Mixed"], "Test.UPPER"),
    ("Test", ["Mixed", "UPPER", "lower"], "Test.UPPER"),
    ("Logic", ["aB", "bA", "cC"], "Logic.aB"),
    ("Data", ["XYZ", "XYZa", "XYZb"], "Data.XYZ"),
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    """Parametrized tests for various combinations of cases."""
    assert Strongest_Extension(class_name, extensions) == expected
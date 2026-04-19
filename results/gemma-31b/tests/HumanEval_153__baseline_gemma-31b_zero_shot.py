
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

def test_strongest_extension_provided_examples():
    """Test the examples provided in the problem description."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_uppercase():
    """Test cases where extensions consist only of uppercase letters."""
    # AA: 2-0=2, B: 1-0=1, CCC: 3-0=3
    assert Strongest_Extension('MyClass', ['AA', 'B', 'CCC']) == 'MyClass.CCC'

def test_strongest_extension_all_lowercase():
    """Test cases where extensions consist only of lowercase letters."""
    # aaa: 0-3=-3, b: 0-1=-1, cc: 0-2=-2
    # Strongest is -1
    assert Strongest_Extension('MyClass', ['aaa', 'b', 'cc']) == 'MyClass.b'

def test_strongest_extension_tie_breaker():
    """Test that the first extension is chosen in case of a tie in strength."""
    # AA: 2-0=2, BB: 2-0=2, CC: 2-0=2
    assert Strongest_Extension('MyClass', ['AA', 'BB', 'CC']) == 'MyClass.AA'
    # a: 0-1=-1, b: 0-1=-1
    assert Strongest_Extension('MyClass', ['a', 'b']) == 'MyClass.a'

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('MyClass', ['OnlyOne']) == 'MyClass.OnlyOne'

def test_strongest_extension_mixed_characters():
    """Test extensions containing non-alphabetic characters (should be ignored in count)."""
    # A1: 1-0=1, a1: 0-1=-1, 123: 0-0=0
    assert Strongest_Extension('MyClass', ['A1', 'a1', '123']) == 'MyClass.A1'
    # A!b: 1-1=0, B@c: 1-1=0
    assert Strongest_Extension('MyClass', ['A!b', 'B@c']) == 'MyClass.A!b'

def test_strongest_extension_zero_strength():
    """Test cases where the strongest strength is exactly 0."""
    # Ab: 1-1=0, abc: 0-3=-3
    assert Strongest_Extension('MyClass', ['Ab', 'abc']) == 'MyClass.Ab'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Test", ["UPPER", "lower", "Mixed"], "Test.UPPER"),
    ("Test", ["lower", "UPPER", "Mixed"], "Test.UPPER"),
    ("Test", ["aB", "bA"], "Test.aB"),
    ("Test", ["", "a"], "Test."), # Empty string: 0-0=0, 'a': 0-1=-1
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    """Parametrized tests for various edge cases."""
    assert Strongest_Extension(class_name, extensions) == expected
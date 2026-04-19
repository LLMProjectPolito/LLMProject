
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
    """Test the basic functionality with a clear winner."""
    # 'SErviNGSliCes': CAP=6 (S,E,N,G,S,C), SM=7 (e,r,v,i,l,i,e,s) -> 6-7 = -1
    # 'Cheese': CAP=1 (C), SM=5 (h,e,e,s,e) -> 1-5 = -4
    # 'StuFfed': CAP=2 (S,F), SM=5 (t,u,f,e,d) -> 2-5 = -3
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie():
    """Test that the first extension is chosen when strengths are equal."""
    # 'AA': 2-0 = 2
    # 'Be': 1-1 = 0
    # 'CC': 2-0 = 2
    # AA and CC tie, AA comes first.
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_lowercase():
    """Test behavior when all extensions are lowercase (negative strengths)."""
    # 'abc': 0-3 = -3
    # 'abcd': 0-4 = -4
    # -3 is greater than -4
    assert Strongest_Extension('Test', ['abc', 'abcd']) == 'Test.abc'

def test_strongest_extension_all_uppercase():
    """Test behavior when all extensions are uppercase."""
    # 'ABC': 3-0 = 3
    # 'ABCD': 4-0 = 4
    assert Strongest_Extension('Test', ['ABC', 'ABCD']) == 'Test.ABCD'

def test_strongest_extension_single_element():
    """Test with a list containing only one extension."""
    assert Strongest_Extension('MyClass', ['OnlyOne']) == 'MyClass.OnlyOne'

def test_strongest_extension_mixed_characters():
    """Test that non-alphabetic characters are ignored in strength calculation."""
    # 'A1b': CAP=1, SM=1 -> 0
    # 'B22': CAP=1, SM=0 -> 1
    # 'c33': CAP=0, SM=1 -> -1
    assert Strongest_Extension('Class', ['A1b', 'B22', 'c33']) == 'Class.B22'

def test_strongest_extension_empty_strings():
    """Test behavior with empty strings as extensions."""
    # '': 0-0 = 0
    # 'a': 0-1 = -1
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'

def test_strongest_extension_long_strings():
    """Test with longer strings to ensure counting is accurate."""
    ext1 = "A" * 10 + "a" * 5  # 10 - 5 = 5
    ext2 = "A" * 5 + "a" * 10  # 5 - 10 = -5
    assert Strongest_Extension('Long', [ext1, ext2]) == f'Long.{ext1}'

# --- New Edge Case Tests based on Review ---

def test_strongest_extension_empty_list():
    """Test behavior when the extensions list is empty. 
    Expected: Return None or just the class name (depending on implementation).
    Assuming None for this specification.
    """
    assert Strongest_Extension('MyClass', []) is None

def test_strongest_extension_non_alphabetic():
    """Test extensions consisting entirely of non-alphabetic characters.
    All strengths will be 0, so the first one should be chosen.
    """
    # '123': 0-0 = 0
    # '!!!': 0-0 = 0
    assert Strongest_Extension('Class', ['123', '!!!']) == 'Class.123'

def test_strongest_extension_empty_class_name():
    """Test behavior when the className argument is an empty string."""
    # 'Ext': 1-2 = -1
    assert Strongest_Extension('', ['Ext']) == '.Ext'
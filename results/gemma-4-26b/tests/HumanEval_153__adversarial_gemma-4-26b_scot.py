
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

def test_provided_examples():
    """Verify the function works with the examples provided in the docstring."""
    # Example 1
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    # Example 2
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_tie_breaking_logic():
    """Ensure that if strengths are equal, the first occurrence in the list is chosen."""
    # All have strength 0 (1 upper, 1 lower)
    extensions = ['Ab', 'Cd', 'Ef', 'Gh']
    assert Strongest_Extension('Test', extensions) == 'Test.Ab'
    
    # All have strength 2 (2 upper, 0 lower)
    extensions = ['AA', 'BB', 'CC']
    assert Strongest_Extension('Test', extensions) == 'Test.AA'

def test_negative_strength_dominance():
    """Ensure the function correctly identifies the strongest extension when all are negative."""
    # Strengths: 'a'=-1, 'bb'=-2, 'ccc'=-3. Max is -1.
    assert Strongest_Extension('Class', ['a', 'bb', 'ccc']) == 'Class.a'
    # Strengths: 'abc'=-3, 'ABC'=3, 'Abc'=-1. Max is 3.
    assert Strongest_Extension('Class', ['abc', 'ABC', 'Abc']) == 'Class.ABC'

def test_non_alphabetic_characters():
    """Ensure numbers and symbols do not interfere with the CAP - SM calculation."""
    # 'A1!' -> CAP=1, SM=0, Strength=1
    # 'a2@' -> CAP=0, SM=1, Strength=-1
    assert Strongest_Extension('Data', ['A1!', 'a2@']) == 'Data.A1!'
    
    # '123' -> CAP=0, SM=0, Strength=0
    # 'ABC' -> CAP=3, SM=0, Strength=3
    assert Strongest_Extension('Data', ['123', 'ABC']) == 'Data.ABC'

def test_single_extension():
    """Test behavior with a list containing exactly one extension."""
    assert Strongest_Extension('Solo', ['OnlyOne']) == 'Solo.OnlyOne'

def test_empty_extension_string():
    """Test behavior when an extension is an empty string."""
    # Empty string has CAP=0, SM=0, Strength=0
    assert Strongest_Extension('Empty', ['', 'A']) == 'Empty.A'
    assert Strongest_Extension('Empty', ['', 'a']) == 'Empty.'

def test_empty_extension_list():
    """Test that an empty list of extensions raises a ValueError (standard max() behavior)."""
    with pytest.raises(ValueError):
        Strongest_Extension('NoExt', [])

def test_class_name_integrity():
    """Ensure the class name is preserved exactly as provided, including special characters."""
    assert Strongest_Extension('My-Class_123', ['Ext']) == 'My-Class_123.Ext'

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

def test_docstring_example_1():
    """Test the primary example provided in the docstring."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_docstring_example_2():
    """Test the tie-breaking example provided in the docstring."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_all_uppercase():
    """Test extensions that are entirely uppercase."""
    # 'AAA' strength: 3-0 = 3; 'B' strength: 1-0 = 1
    assert Strongest_Extension('Base', ['AAA', 'B']) == 'Base.AAA'

def test_all_lowercase():
    """Test extensions that are entirely lowercase."""
    # 'aaa' strength: 0-3 = -3; 'b' strength: 0-1 = -1
    # 'b' is stronger (-1 > -3)
    assert Strongest_Extension('Base', ['aaa', 'b']) == 'Base.b'

def test_mixed_case_tie():
    """Test that the first extension is chosen when strengths are identical."""
    # 'Ab' strength: 1-1 = 0
    # 'Cd' strength: 1-1 = 0
    # 'Ef' strength: 1-1 = 0
    assert Strongest_Extension('Class', ['Ab', 'Cd', 'Ef']) == 'Class.Ab'

def test_single_extension():
    """Test the function with a list containing only one extension."""
    assert Strongest_Extension('Unique', ['OnlyOne']) == 'Unique.OnlyOne'

def test_non_alphabetic_characters():
    """Test that non-alpha characters are ignored in strength calculation."""
    # 'A1' strength: 1-0 = 1
    # 'a2' strength: 0-1 = -1
    # '123' strength: 0-0 = 0
    assert Strongest_Extension('Numeric', ['A1', 'a2', '123']) == 'Numeric.A1'
    
    # 'A!' strength: 1-0 = 1
    # 'B?' strength: 1-0 = 1
    # Tie goes to 'A!'
    assert Strongest_Extension('Symbol', ['A!', 'B?']) == 'Symbol.A!'

def test_empty_extension_string():
    """Test behavior when an extension is an empty string."""
    # '' strength: 0-0 = 0
    # 'a' strength: 0-1 = -1
    # Empty string is stronger than 'a'
    assert Strongest_Extension('Empty', ['', 'a']) == 'Empty.'

def test_large_strength_difference():
    """Test with a significant difference in strength."""
    # 'VERYSTRONG' strength: 10-0 = 10
    # 'veryweak' strength: 0-8 = -8
    assert Strongest_Extension('Test', ['veryweak', 'VERYSTRONG']) == 'Test.VERYSTRONG'
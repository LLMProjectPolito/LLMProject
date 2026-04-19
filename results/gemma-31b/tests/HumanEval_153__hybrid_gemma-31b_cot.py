
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

def test_strongest_extension_basic_example():
    """Test the provided example from the prompt."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie_break():
    """Test that the first extension is chosen when strengths are equal."""
    # AA: 2-0 = 2, Be: 1-1 = 0, CC: 2-0 = 2. AA and CC tie; AA comes first.
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    # ABC: 3, DEF: 3, GHI: 3. ABC comes first.
    assert Strongest_Extension('TestClass', ['ABC', 'DEF', 'GHI']) == 'TestClass.ABC'

def test_strongest_extension_single_element():
    """Test with only one extension in the list."""
    assert Strongest_Extension('Test', ['OnlyOne']) == 'Test.OnlyOne'

def test_strongest_extension_all_lowercase():
    """Test extensions that only contain lowercase letters (negative strength)."""
    # abc: -3, ab: -2, a: -1. Max is -1.
    assert Strongest_Extension('Class', ['abc', 'ab', 'a']) == 'Class.a'

def test_strongest_extension_all_uppercase():
    """Test extensions that only contain uppercase letters (positive strength)."""
    # A: 1, AB: 2, ABC: 3. Max is 3.
    assert Strongest_Extension('Class', ['A', 'AB', 'ABC']) == 'Class.ABC'

def test_strongest_extension_mixed_case_strengths():
    """Test a variety of mixed case strings to ensure calculation is accurate."""
    # 'aB': 0, 'abB': -1, 'ABb': 1, 'AB': 2, 'A': 1. Max is 2.
    assert Strongest_Extension('Complex', ['aB', 'abB', 'ABb', 'AB', 'A']) == 'Complex.AB'
    # 'up': -2, 'Up': 0, 'UP': 2. Max is 2.
    assert Strongest_Extension('Mixed', ['up', 'Up', 'UP']) == 'Mixed.UP'

def test_strongest_extension_non_alpha():
    """Test extensions containing numbers or symbols which should not affect strength."""
    # A1b: 1-1 = 0, B2c: 1-1 = 0, C3D: 2-0 = 2.
    assert Strongest_Extension('MyClass', ['A1b', 'B2c', 'C3D']) == 'MyClass.C3D'
    # a1: -1, 123: 0, A1: 1.
    assert Strongest_Extension('Numeric', ['a1', '123', 'A1']) == 'Numeric.A1'
    # '123': 0, '!!!': 0, ' ': 0. Ties go to the first.
    assert Strongest_Extension('Empty', ['123', '!!!', ' ']) == 'Empty.123'

def test_strongest_extension_empty_strings():
    """Test behavior with empty class names or empty extension strings."""
    # Empty class name
    assert Strongest_Extension('', ['Strong']) == '.Strong'
    # Empty extension string: strength 0. 'a' is -1. Empty wins.
    assert Strongest_Extension('Empty', ['', 'a']) == 'Empty.'
    # Empty extension string: strength 0. 'A' is 1. 'A' wins.
    assert Strongest_Extension('Empty', ['', 'A']) == 'Empty.A'

def test_strongest_extension_class_name_variations():
    """Test that different class name formats are handled correctly."""
    assert Strongest_Extension('123_Class', ['ExtA', 'ExtB']) == '123_Class.ExtA'

def test_strongest_extension_all_negative():
    """Test when all extensions have negative strength to ensure max() handles negatives."""
    # 'abcde': -5, 'abcd': -4, 'abc': -3. Max is -3.
    assert Strongest_Extension('Negative', ['abcde', 'abcd', 'abc']) == 'Negative.abc'

def test_strongest_extension_long_strings():
    """Test with very long strings to ensure performance and logic hold."""
    long_upper = 'A' * 1000
    long_lower = 'a' * 1000
    mixed = ('A' * 500) + ('a' * 500)
    # long_upper: 1000, long_lower: -1000, mixed: 0.
    assert Strongest_Extension('Long', [long_lower, mixed, long_upper]) == f'Long.{long_upper}'
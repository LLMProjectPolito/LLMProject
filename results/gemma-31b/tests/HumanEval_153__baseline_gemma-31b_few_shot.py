
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
    """Tests the basic functionality with the provided example."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie():
    """Tests that the first extension is chosen when strengths are equal."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_lowercase():
    """Tests cases where all extensions have negative strength."""
    # 'abc' strength: 0 - 3 = -3
    # 'defg' strength: 0 - 4 = -4
    assert Strongest_Extension('Test', ['abc', 'defg']) == 'Test.abc'

def test_strongest_extension_all_uppercase():
    """Tests cases where all extensions have positive strength."""
    # 'ABC' strength: 3 - 0 = 3
    # 'DEFG' strength: 4 - 0 = 4
    assert Strongest_Extension('Test', ['ABC', 'DEFG']) == 'Test.DEFG'

def test_strongest_extension_single_element():
    """Tests the function with a list containing only one extension."""
    assert Strongest_Extension('Single', ['OnlyOne']) == 'Single.OnlyOne'

def test_strongest_extension_mixed_tie():
    """Tests multiple extensions with the same mixed-case strength."""
    # 'aB' strength: 1 - 1 = 0
    # 'bA' strength: 1 - 1 = 0
    # 'cC' strength: 1 - 1 = 0
    assert Strongest_Extension('Base', ['aB', 'bA', 'cC']) == 'Base.aB'

def test_strongest_extension_with_non_alpha():
    """Tests that non-alphabetic characters are ignored in strength calculation."""
    # 'A1b' strength: 1 (A) - 1 (b) = 0
    # 'B22' strength: 1 (B) - 0 = 1
    assert Strongest_Extension('Class', ['A1b', 'B22']) == 'Class.B22'

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

def test_provided_example_slices():
    """Tests the specific example provided in the docstring."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_provided_example_my_class():
    """Tests the second example provided in the docstring involving a tie."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_tie_breaker_logic():
    """Ensures that if strengths are equal, the first occurrence in the list is chosen."""
    # All extensions have strength 0 (1 upper, 1 lower)
    extensions = ['Ab', 'Cd', 'Ef', 'Gh']
    assert Strongest_Extension('TestClass', extensions) == 'TestClass.Ab'

def test_all_negative_strengths():
    """Tests case where all extensions have negative strength (more lowercase than uppercase)."""
    # 'abc' -> -3, 'def' -> -3, 'G' -> 1, 'h' -> -1
    extensions = ['abc', 'def', 'h', 'G']
    assert Strongest_Extension('TestClass', extensions) == 'TestClass.G'

def test_all_positive_strengths():
    """Tests case where all extensions have positive strength."""
    # 'AAA' -> 3, 'BB' -> 2, 'C' -> 1
    extensions = ['AAA', 'BB', 'C']
    assert Strongest_Extension('TestClass', extensions) == 'TestClass.AAA'

def test_single_extension():
    """Tests a list containing only one extension."""
    assert Strongest_Extension('Solo', ['OnlyOne']) == 'Solo.OnlyOne'

def test_non_alphabetic_characters():
    """Tests that numbers and symbols do not contribute to CAP or SM."""
    # 'A1!' -> CAP=1, SM=0 -> Strength 1
    # 'a2@' -> CAP=0, SM=1 -> Strength -1
    # '!!'  -> CAP=0, SM=0 -> Strength 0
    extensions = ['a2@', '!!', 'A1!']
    assert Strongest_Extension('Class', extensions) == 'Class.A1!'

def test_empty_extension_string():
    """Tests behavior when an extension is an empty string."""
    # '' -> Strength 0
    # 'A' -> Strength 1
    assert Strongest_Extension('Class', ['', 'A']) == 'Class.A'

def test_case_sensitivity_and_mixed():
    """Tests a complex mix of cases and characters."""
    # 'aB' -> 1-1 = 0
    # 'AB' -> 2-0 = 2
    # 'ab' -> 0-2 = -2
    extensions = ['ab', 'aB', 'AB']
    assert Strongest_Extension('Mix', extensions) == 'Mix.AB'
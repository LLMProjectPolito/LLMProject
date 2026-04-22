
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

def test_provided_example_1():
    """Tests the specific example provided in the problem description."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_provided_example_2():
    """Tests the second example provided in the problem description."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_tie_breaking_logic():
    """Ensures that if strengths are equal, the first occurrence in the list is chosen."""
    # All have strength 0 (1 uppercase, 1 lowercase)
    assert Strongest_Extension('Class', ['Ab', 'Cd', 'Ef']) == 'Class.Ab'
    # All have strength 2 (2 uppercase, 0 lowercase)
    assert Strongest_Extension('Class', ['AA', 'BB', 'CC']) == 'Class.AA'
    # All have strength -1 (1 uppercase, 2 lowercase)
    assert Strongest_Extension('Class', ['Aaa', 'Bbb', 'Ccc']) == 'Class.Aaa'

def test_all_negative_strengths():
    """Tests behavior when all extensions have negative strength."""
    # 'aaa' -> -3, 'bb' -> -2, 'c' -> -1
    # Max is -1
    assert Strongest_Extension('Class', ['aaa', 'bb', 'c']) == 'Class.c'
    # 'aa' -> -2, 'bb' -> -2, 'ccc' -> -3
    # Max is -2, first is 'aa'
    assert Strongest_Extension('Class', ['aa', 'bb', 'ccc']) == 'Class.aa'

def test_non_alphabetic_characters():
    """Tests that numbers and symbols do not contribute to CAP or SM."""
    # 'A1' -> CAP=1, SM=0 -> 1
    # 'a!' -> CAP=0, SM=1 -> -1
    # '123' -> CAP=0, SM=0 -> 0
    assert Strongest_Extension('Class', ['a!', 'A1', '123']) == 'Class.A1'
    # 'A B' -> CAP=1, SM=1 -> 0
    assert Strongest_Extension('Class', ['A B', 'A']) == 'Class.A'

def test_empty_extension_string():
    """Tests behavior with an empty string as an extension."""
    # '' -> CAP=0, SM=0 -> 0
    # 'A' -> 1
    # 'a' -> -1
    assert Strongest_Extension('Class', ['', 'A', 'a']) == 'Class.A'
    assert Strongest_Extension('Class', ['', 'a', 'b']) == 'Class.' # Wait, if '' is strongest, result is 'Class.'

def test_single_extension():
    """Tests the function with a list containing only one extension."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_all_lowercase_and_uppercase():
    """Tests edge cases of purely lowercase or purely uppercase strings."""
    assert Strongest_Extension('Class', ['abc', 'def']) == 'Class.abc'
    assert Strongest_Extension('Class', ['ABC', 'DEF']) == 'Class.ABC'

def test_class_name_formatting():
    """Tests that the class name is preserved exactly as provided, including special characters."""
    assert Strongest_Extension('My_Class-123', ['Ext']) == 'My_Class-123.Ext'
    assert Strongest_Extension(' ', ['A']) == ' .A'

def test_zero_strength_mix():
    """Tests a mix of positive, negative, and zero strength extensions."""
    # 'A' (1), 'a' (-1), 'Ab' (0), '123' (0)
    # Max is 1
    assert Strongest_Extension('Class', ['a', 'Ab', '123', 'A']) == 'Class.A'
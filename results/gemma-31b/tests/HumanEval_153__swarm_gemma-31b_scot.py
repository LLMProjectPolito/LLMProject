
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
import math

def test_strongest_extension_non_alpha_and_negative_strengths():
    """
    Tests that non-alphabetic characters are ignored and that the function
    correctly handles a mix of negative strengths and ties.
    """
    class_name = "MyClass"
    # 'abc': 0-3 = -3
    # '123': 0-0 = 0 (Strongest)
    # 'aB1': 1-1 = 0 (Tie with '123', but comes later)
    # 'cd': 0-2 = -2
    extensions = ['abc', '123', 'aB1', 'cd']
    assert Strongest_Extension(class_name, extensions) == "MyClass.123"

def test_strongest_extension_non_alpha_and_ties():
    """
    Test edge case where multiple extensions have the same strength (0),
    including extensions with non-alphabetic characters and empty strings.
    The tie-break rule should ensure the first occurrence is returned.
    """
    class_name = "BaseClass"
    extensions = ["A1b", "B2a", "123", "", "C3d"]
    # Calculation:
    # "A1b": 1 upper, 1 lower -> 0
    # "B2a": 1 upper, 1 lower -> 0
    # "123": 0 upper, 0 lower -> 0
    # "":    0 upper, 0 lower -> 0
    # "C3d": 1 upper, 1 lower -> 0
    # All strengths are 0; first one is "A1b".
    assert Strongest_Extension(class_name, extensions) == "BaseClass.A1b"

def test_strongest_extension_non_alpha_tie():
    """
    Test Case: Extensions with non-alphabetic characters and balanced cases.
    Max strength is 0. The first extension with strength 0 is "123".
    """
    class_name = "Meta"
    extensions = ["123", "!!!", "aB", "cd"]
    # "123" -> CAP: 0, SM: 0 -> Strength: 0
    # "!!!" -> CAP: 0, SM: 0 -> Strength: 0
    # "aB"  -> CAP: 1, SM: 1 -> Strength: 0
    # "cd"  -> CAP: 0, SM: 2 -> Strength: -2
    assert Strongest_Extension(class_name, extensions) == "Meta.123"
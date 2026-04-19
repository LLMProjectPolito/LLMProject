
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

def test_strongest_extension_non_alpha_tie():
    """
    Test the case where extensions contain only non-alphabetic characters.
    All such extensions will have a strength of 0 (0 uppercase - 0 lowercase).
    The tie-breaker should return the first extension in the list.
    """
    assert Strongest_Extension("BaseClass", ["123", "!!!", "   "]) == "BaseClass.123"

def test_strongest_extension_mixed_non_alpha_tie():
    """
    Tests the function's ability to handle non-alphabetic characters and tie-breaking.
    'aB1': CAP=1 ('B'), SM=1 ('a') -> strength = 0
    'C2d': CAP=1 ('C'), SM=1 ('d') -> strength = 0
    '!!!': CAP=0, SM=0 -> strength = 0
    Since all have strength 0, the first one in the list ('aB1') should be chosen.
    """
    assert Strongest_Extension("Base", ["aB1", "C2d", "!!!"]) == "Base.aB1"

def test_strongest_extension_negative_tie_with_non_letters():
    """
    Test case where all extensions have the same negative strength
    and contain non-alphabetic characters to ensure only letters are counted
    and the first occurrence is returned in a tie.
    """
    assert Strongest_Extension("MyClass", ["a1", "b2", "c3"]) == "MyClass.a1"
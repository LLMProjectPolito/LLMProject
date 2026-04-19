
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

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("MyClass", ["abc", "123", "456"], "MyClass.123"),
    ("MyClass", ["aB1", "C2d", "e3F"], "MyClass.aB1"),
    ("TestClass", ["abc", "def", "ghi"], "TestClass.abc"),
])
def test_strongest_extension_tie_breaking(class_name, extensions, expected):
    """
    Tests that the first occurrence is returned when strengths tie, 
    covering non-alphabetic, mixed, and all-negative strength scenarios.
    """
    assert Strongest_Extension(class_name, extensions) == expected
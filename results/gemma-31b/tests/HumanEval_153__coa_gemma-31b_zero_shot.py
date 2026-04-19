
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


# Focus: Boundary Values
def test_strongest_extension_tie_boundary():
    # Boundary: Multiple extensions with the exact same maximum strength
    # 'AA' (2-0=2), 'BB' (2-0=2), 'CC' (2-0=2) -> Should pick the first one
    assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

def test_strongest_extension_single_element():
    # Boundary: Minimum list size (one extension)
    assert Strongest_Extension("MyClass", ["onlyOne"]) == "MyClass.onlyOne"

def test_strongest_extension_extreme_strengths():
    # Boundary: Maximum possible strength (all upper) vs minimum possible strength (all lower)
    # 'abc' (0-3=-3), 'ABC' (3-0=3)
    assert Strongest_Extension("MyClass", ["abc", "ABC"]) == "MyClass.ABC"

# Focus: Logic Branches
import pytest

def test_strongest_extension_tie_breaker():
    # Test that the first extension is chosen when multiple have the same maximum strength
    # 'AA': 2-0=2, 'BB': 2-0=2, 'CC': 2-0=2
    assert Strongest_Extension('my_class', ['AA', 'BB', 'CC']) == 'my_class.AA'

def test_strongest_extension_negative_strengths():
    # Test logic when all strengths are negative (finding the maximum/least negative)
    # 'Cheese': 1-5 = -4
    # 'StuFfed': 2-5 = -3
    # 'SErviNGSliCes': 6-7 = -1
    assert Strongest_Extension('Slices', ['Cheese', 'StuFfed', 'SErviNGSliCes']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_mixed_extremes():
    # Test logic with purely lowercase vs purely uppercase extensions
    # 'abc': 0-3 = -3
    # 'ABC': 3-0 = 3
    # 'aB': 1-1 = 0
    assert Strongest_Extension('Test', ['abc', 'aB', 'ABC']) == 'Test.ABC'

# Focus: Type Scenarios
import pytest

def test_strongest_extension_extreme_cases():
    # Testing extensions with only uppercase (max strength) and only lowercase (min strength)
    assert Strongest_Extension("MyClass", ["UPPER", "lower"]) == "MyClass.UPPER"
    assert Strongest_Extension("MyClass", ["lower", "UPPER"]) == "MyClass.UPPER"

def test_strongest_extension_non_alphabetic():
    # Testing extensions with non-alphabetic characters (strength 0)
    # "123" has 0 caps, 0 smalls -> 0. "!!!" has 0 caps, 0 smalls -> 0.
    # Should return the first one in the list.
    assert Strongest_Extension("MyClass", ["123", "!!!"]) == "MyClass.123"

def test_strongest_extension_empty_and_mixed():
    # Testing empty strings (strength 0) against lowercase strings (negative strength)
    assert Strongest_Extension("MyClass", ["", "abc"]) == "MyClass."
    # Testing mixed characters where strength is 0
    assert Strongest_Extension("MyClass", ["A1b", "C2d"]) == "MyClass.A1b"
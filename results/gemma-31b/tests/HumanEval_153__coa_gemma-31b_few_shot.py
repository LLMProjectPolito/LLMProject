
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
import pytest

def test_strongest_extension_tie_break():
    # Boundary: Multiple extensions with the same strength, should return the first one
    assert Strongest_Extension('MyClass', ['AA', 'BB', 'CC']) == 'MyClass.AA'
    assert Strongest_Extension('MyClass', ['ab', 'cd', 'ef']) == 'MyClass.ab'

def test_strongest_extension_extreme_strengths():
    # Boundary: Extensions with only uppercase (max strength) and only lowercase (min strength)
    assert Strongest_Extension('MyClass', ['abc', 'ABC']) == 'MyClass.ABC'
    assert Strongest_Extension('MyClass', ['ABC', 'abc']) == 'MyClass.ABC'

def test_strongest_extension_single_char():
    # Boundary: Minimum length extensions (single characters)
    assert Strongest_Extension('MyClass', ['a', 'A']) == 'MyClass.A'
    assert Strongest_Extension('MyClass', ['A', 'a']) == 'MyClass.A'

# Focus: Logic Branches
import pytest

def test_strongest_extension_tie_breaker():
    # Both 'AA' and 'BB' have strength 2 (2-0). Should return the first one.
    assert Strongest_Extension('MyClass', ['AA', 'BB', 'CC']) == 'MyClass.AA'

def test_strongest_extension_negative_strengths():
    # 'abc' strength: 0-3 = -3
    # 'abcd' strength: 0-4 = -4
    # 'abcde' strength: 0-5 = -5
    # 'abc' is the strongest (maximum value).
    assert Strongest_Extension('MyClass', ['abc', 'abcd', 'abcde']) == 'MyClass.abc'

def test_strongest_extension_mixed_logic():
    # 'aB' strength: 1-1 = 0
    # 'Abc' strength: 1-2 = -1
    # 'ABC' strength: 3-0 = 3
    assert Strongest_Extension('MyClass', ['aB', 'Abc', 'ABC']) == 'MyClass.ABC'

# Focus: Type Scenarios
import pytest

def test_strongest_extension_non_alpha_types():
    """Test extensions containing only non-alphabetic characters (strength should be 0)."""
    assert Strongest_Extension('Class', ['123', '456']) == 'Class.123'
    assert Strongest_Extension('Class', ['!!!', '???']) == 'Class.!!!'
    assert Strongest_Extension('Class', ['1a', '2A']) == 'Class.2A'

def test_strongest_extension_extreme_case_types():
    """Test extensions consisting exclusively of one case (maximum/minimum strength)."""
    assert Strongest_Extension('Class', ['AAA', 'aaa']) == 'Class.AAA'
    assert Strongest_Extension('Class', ['aaa', 'AAA']) == 'Class.AAA'
    assert Strongest_Extension('Class', ['a', 'A']) == 'Class.A'

def test_strongest_extension_empty_string_types():
    """Test extensions that are empty strings or whitespace."""
    assert Strongest_Extension('Class', ['', ' ']) == 'Class.'
    assert Strongest_Extension('Class', [' ', '']) == 'Class. '
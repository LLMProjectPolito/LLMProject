
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

def test_strongest_extension_tie_breaker():
    # Boundary: Multiple extensions with the same maximum strength
    # 'AA': 2-0=2, 'BB': 2-0=2. Should pick the first one.
    assert Strongest_Extension('MyClass', ['AA', 'BB', 'CC']) == 'MyClass.AA'
    # 'a': 0-1=-1, 'b': 0-1=-1. Should pick the first one.
    assert Strongest_Extension('MyClass', ['a', 'b', 'c']) == 'MyClass.a'

def test_strongest_extension_extremes():
    # Boundary: All uppercase (max positive) vs all lowercase (max negative)
    assert Strongest_Extension('MyClass', ['abc', 'ABC']) == 'MyClass.ABC'
    # Boundary: Single character extensions
    assert Strongest_Extension('MyClass', ['a', 'A']) == 'MyClass.A'

def test_strongest_extension_empty_and_zero():
    # Boundary: Empty string extension (strength 0-0=0)
    assert Strongest_Extension('MyClass', ['']) == 'MyClass.'
    # Boundary: Extension with equal number of upper and lower case (strength 0)
    assert Strongest_Extension('MyClass', ['Ab', 'abc']) == 'MyClass.Ab'

# Focus: Logic Branches
import pytest

def test_strongest_extension_tie_breaker():
    # Test that the first extension is chosen when strengths are equal
    # 'AA': 2-0=2, 'BB': 2-0=2, 'CC': 2-0=2
    assert Strongest_Extension('my_class', ['AA', 'BB', 'CC']) == 'my_class.AA'

def test_strongest_extension_negative_strengths():
    # Test logic when all strengths are negative (mostly lowercase)
    # 'abc': 0-3=-3, 'ab': 0-2=-2, 'a': 0-1=-1
    assert Strongest_Extension('Base', ['abc', 'ab', 'a']) == 'Base.a'

def test_strongest_extension_mixed_logic():
    # Test a mix of positive, negative, and zero strengths
    # 'ABC': 3-0=3, 'Abc': 1-2=-1, 'aB': 1-1=0
    assert Strongest_Extension('Test', ['Abc', 'aB', 'ABC']) == 'Test.ABC'

# Focus: Type Scenarios
import pytest

def test_non_alphabetic_characters():
    # Tests extensions containing numbers and symbols to ensure only letters are counted
    assert Strongest_Extension('MyClass', ['A1', 'a1', 'A1a']) == 'MyClass.A1'
    assert Strongest_Extension('MyClass', ['123', '!!!', ' ']) == 'MyClass.123'

def test_extreme_casing():
    # Tests extensions with only uppercase or only lowercase letters
    assert Strongest_Extension('MyClass', ['ABC', 'abc']) == 'MyClass.ABC'
    assert Strongest_Extension('MyClass', ['abc', 'ABC']) == 'MyClass.ABC'
    assert Strongest_Extension('MyClass', ['aaa', 'bbb']) == 'MyClass.aaa'

def test_empty_and_special_strings():
    # Tests empty strings as class names or extensions
    assert Strongest_Extension('', ['Ext']) == '.Ext'
    assert Strongest_Extension('MyClass', ['']) == 'MyClass.'
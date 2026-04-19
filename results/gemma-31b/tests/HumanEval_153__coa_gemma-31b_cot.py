
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

def test_strongest_extension_ties():
    # Boundary: Multiple extensions with the same maximum strength. 
    # Should return the first one in the list.
    assert Strongest_Extension('MyClass', ['AAA', 'BBB', 'CCC']) == 'MyClass.AAA'
    assert Strongest_Extension('MyClass', ['Ab', 'Cd', 'Ef']) == 'MyClass.Ab'

def test_strongest_extension_all_lowercase():
    # Boundary: Extensions with 0 uppercase letters (minimum possible strength for length).
    # Should still return the first one if all are equally weak.
    assert Strongest_Extension('MyClass', ['abc', 'def', 'ghi']) == 'MyClass.abc'

def test_strongest_extension_single_char():
    # Boundary: Extensions consisting of a single character.
    assert Strongest_Extension('MyClass', ['a', 'A']) == 'MyClass.A'
    assert Strongest_Extension('MyClass', ['A', 'a']) == 'MyClass.A'

# Focus: Logic Branches
def test_strongest_extension_tie_breaker():
    # Tests that when multiple extensions have the same maximum strength, the first one is chosen
    assert Strongest_Extension('MyClass', ['AA', 'BB', 'Cc']) == 'MyClass.AA'

def test_strongest_extension_negative_strengths():
    # Tests logic when all extensions have negative strengths (SM > CAP)
    # 'abc' strength: 0 - 3 = -3
    # 'ab' strength: 0 - 2 = -2
    assert Strongest_Extension('MyClass', ['abc', 'ab']) == 'MyClass.ab'

def test_strongest_extension_mixed_case():
    # Tests clear winner with mixed case letters
    # 'Strong' strength: 1 - 5 = -4
    # 'STRONG' strength: 6 - 0 = 6
    # 'stRoNg' strength: 1 - 5 = -4
    assert Strongest_Extension('MyClass', ['Strong', 'STRONG', 'stRoNg']) == 'MyClass.STRONG'

# Focus: Character Sets
import pytest

def test_character_sets_mixed_non_alpha():
    # Tests how the function handles non-alphabetic characters (numbers, symbols)
    # 'A123' -> CAP=1, SM=0, Strength=1
    # 'a123' -> CAP=0, SM=1, Strength=-1
    # 'B!@#' -> CAP=1, SM=0, Strength=1
    # Tie between 'A123' and 'B!@#', 'A123' comes first.
    assert Strongest_Extension('Base', ['A123', 'a123', 'B!@#']) == 'Base.A123'

def test_character_sets_no_alpha():
    # Tests extensions containing no letters at all
    # '123' -> CAP=0, SM=0, Strength=0
    # '!!!' -> CAP=0, SM=0, Strength=0
    # Tie between '123' and '!!!', '123' comes first.
    assert Strongest_Extension('Base', ['123', '!!!']) == 'Base.123'

def test_character_sets_extreme_cases():
    # Tests all uppercase vs all lowercase
    # 'UPPER' -> CAP=5, SM=0, Strength=5
    # 'lower' -> CAP=0, SM=5, Strength=-5
    assert Strongest_Extension('Base', ['lower', 'UPPER']) == 'Base.UPPER'

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
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = 0
        sm = 0
        for char in extension:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = f"{class_name}.{extension}"
        elif strength == max_strength and strongest_extension == "":
            strongest_extension = f"{class_name}.{extension}"

    return strongest_extension


def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('AnotherClass', ['ExAmPlE', 'Test']) == 'AnotherClass.ExAmPlE'
    assert Strongest_Extension('YetAnother', ['aBcDeFg', '12345']) == 'YetAnother.aBcDeFg'
    assert Strongest_Extension('Simple', []) == 'Simple.'

def test_strongest_extension_same_strength():
    assert Strongest_Extension('Class1', ['A', 'B']) == 'Class1.A'
    assert Strongest_Extension('Class2', ['a', 'b']) == 'Class2.a'
    assert Strongest_Extension('Class3', ['AA', 'BB']) == 'Class3.AA'

def test_strongest_extension_empty_extension():
    assert Strongest_Extension('Class4', ['']) == 'Class4.'
    assert Strongest_Extension('Class5', ['  ']) == 'Class5.'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Class6', ['MiXeD', 'lower']) == 'Class6.MiXeD'
    assert Strongest_Extension('Class7', ['Lower', 'MiXeD']) == 'Class7.Lower'

def test_strongest_extension_no_uppercase():
    assert Strongest_Extension('Class8', ['lowerLower']) == 'Class8.lowerLower'
    assert Strongest_Extension('Class9', ['lower']) == 'Class9.lower'

def test_strongest_extension_no_lowercase():
    assert Strongest_Extension('Class10', ['upperUpper']) == 'Class10.upperUpper'
    assert Strongest_Extension('Class11', ['upper']) == 'Class11.upper'

def test_strongest_extension_empty_class_and_extensions():
     assert Strongest_Extension('Empty', []) == 'Empty.'

### Problem:
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """

### Tests (Pytest):
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

### Problem:
def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """

### Tests (Pytest):
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
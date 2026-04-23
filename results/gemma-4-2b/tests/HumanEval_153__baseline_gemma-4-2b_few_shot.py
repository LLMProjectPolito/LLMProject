
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
    strongest_extension = None
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
            strongest_extension = extension
        elif strength == max_strength and extensions.index(extension) < extensions.index(strongest_extension):
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) is None

def test_strongest_extension_example1():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_multiple_strongest():
    assert Strongest_Extension('my_class', ['AA', 'BB', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('my_class', []) == 'my_class.None'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('my_class', ['aBc', 'AbC']) == 'my_class.aBc'

def test_strongest_extension_complex_case():
    assert Strongest_Extension('my_class', ['Slices', 'SErviNGSliCes', 'Cheese', 'StuFfed']) == 'my_class.SErviNGSliCes'
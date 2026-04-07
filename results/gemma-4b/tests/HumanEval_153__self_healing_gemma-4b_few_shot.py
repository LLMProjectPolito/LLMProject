
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
    strongest_extension = None
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class."

def test_single_extension():
    assert Strongest_Extension("Slices", ["SErviNGSliCes"]) == "Slices.SErviNGSliCes"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese"]) == "Slices.SErviNGSliCes"

def test_mixed_case_extension():
    assert Strongest_Extension("my_class", ["aBcDeFg"]) == "my_class.aBcDeFg"

def test_extension_with_numbers():
    assert Strongest_Extension("my_class", ["123"]) == "my_class.123"

def test_extension_with_special_characters():
    assert Strongest_Extension("my_class", ["!@#"]) == "my_class.!@#"

def test_extension_with_uppercase_and_lowercase():
    assert Strongest_Extension("my_class", ["AbCdEf"]) == "my_class.AbCdEf"

def test_extension_with_all_uppercase():
    assert Strongest_Extension("my_class", ["ABCDEF"]) == "my_class.ABCDEF"

def test_extension_with_all_lowercase():
    assert Strongest_Extension("my_class", ["abcdef"]) == "my_class.abcdef"

def test_complex_extension():
    assert Strongest_Extension("my_class", ["TestExtension123"]) == "my_class.TestExtension123"

def test_class_name_with_special_characters():
    assert Strongest_Extension("my.class", ["abc"]) == "my.class.abc"
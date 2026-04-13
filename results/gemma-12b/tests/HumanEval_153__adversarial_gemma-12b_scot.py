
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
    if not extensions:
        return f"{class_name}.None"

    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        low_count = sum(1 for char in extension if char.islower())
        strength = cap_count - low_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


def test_basic_case():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_same_strength():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class.None"

def test_no_uppercase():
    assert Strongest_Extension("my_class", ['alllowercase']) == "my_class.alllowercase"

def test_no_lowercase():
    assert Strongest_Extension("my_class", ['UPPERCASE']) == "my_class.UPPERCASE"

def test_only_uppercase():
    assert Strongest_Extension("my_class", ['UPPERCASE']) == "my_class.UPPERCASE"

def test_only_lowercase():
    assert Strongest_Extension("my_class", ['lowercase']) == "my_class.lowercase"

def test_class_name_with_underscore():
    assert Strongest_Extension("my_class_name", ['AA', 'Be', 'CC']) == "my_class_name.AA"

def test_extension_with_numbers():
    assert Strongest_Extension("my_class", ['AA123', 'Be', 'CC']) == "my_class.AA123"

def test_extension_with_special_characters():
    assert Strongest_Extension("my_class", ['AA!', 'Be', 'CC']) == "my_class.AA!"
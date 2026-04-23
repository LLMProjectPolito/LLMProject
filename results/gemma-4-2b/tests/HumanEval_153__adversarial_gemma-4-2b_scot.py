
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
            if 'A' <= char <= 'Z':
                cap += 1
            elif 'a' <= char <= 'z':
                sm += 1

        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


def test_basic_case():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_all_uppercase():
    assert Strongest_Extension("my_class", ["AAAA", "BBBB"]) == "my_class.AAAA"

def test_all_lowercase():
    assert Strongest_Extension("my_class", ["a", "b", "c"]) == "my_class.a"

def test_mixed_case():
    assert Strongest_Extension("my_class", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "my_class.SErviNGSliCes"

def test_empty_extension_list():
    assert Strongest_Extension("my_class", []) == "my_class."

def test_class_name_with_special_characters():
    assert Strongest_Extension("my+class", ["AA", "Be", "CC"]) == "my+class.AA"

def test_multiple_same_strength():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_short_extensions():
    assert Strongest_Extension("my_class", ["A", "B"]) == "my_class.A"

def test_long_extensions():
    assert Strongest_Extension("my_class", ["A" * 100, "B" * 100]) == "my_class.A"
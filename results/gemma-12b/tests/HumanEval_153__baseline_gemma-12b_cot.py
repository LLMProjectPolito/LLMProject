
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
    pass

def calculate_strength(extension):
    cap_count = sum(1 for char in extension if char.isupper())
    low_count = sum(1 for char in extension if char.islower())
    return cap_count - low_count

def test_strongest_extension_basic():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_strongest_extension_same_strength():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_strongest_extension_single_extension():
    assert Strongest_Extension("TestClass", ["Extension1"]) == "TestClass.Extension1"

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension("Class", ["AAAA"]) == "Class.AAAA"

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension("Class", ["aaaa"]) == "Class.aaaa"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("Class", ["aA"]) == "Class.aA"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Class", ["bbbb"]) == "Class.bbbb"

def test_strongest_extension_zero_strength():
    assert Strongest_Extension("Class", ["abcABC"]) == "Class.abcABC"

def test_strongest_extension_class_with_special_chars():
    assert Strongest_Extension("My_Class!", ["Extension!"]) == "My_Class!.Extension!"

def test_strongest_extension_extension_with_special_chars():
    assert Strongest_Extension("Class", ["Extension!"]) == "Class.Extension!"

def test_strongest_extension_long_extensions():
    assert Strongest_Extension("Class", ["VeryLongExtension1", "VeryLongExtension2"]) == "Class.VeryLongExtension1"

def test_strongest_extension_numbers_in_extension():
    assert Strongest_Extension("Class", ["Extension123"]) == "Class.Extension123"

def test_strongest_extension_numbers_and_letters():
    assert Strongest_Extension("Class", ["A1B2C"]) == "Class.A1B2C"
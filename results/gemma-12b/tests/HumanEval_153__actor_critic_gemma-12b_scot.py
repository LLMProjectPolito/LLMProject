
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
from your_module import Strongest_Extension  # Replace your_module

def test_basic_case():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_single_extension():
    assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

def test_equal_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"
    assert Strongest_Extension("MyClass", ["aa", "Bb", "cc"]) == "MyClass.aa"  # Covers lowercase as well

def test_no_uppercase_lowercase():
    assert Strongest_Extension("MyClass", ["1234", "5678", "9012"]) == "MyClass.1234"

def test_empty_class_name():
    # Tests the edge case where the class name is empty. This is relevant because
    # an empty class name is a valid input, and the function should handle it gracefully.
    assert Strongest_Extension("", ["Extension1", "Extension2"]) == ".Extension1"

def test_class_name_with_special_characters():
    assert Strongest_Extension("My_Class!", ["Extension1", "Extension2"]) == "My_Class!.Extension1"

def test_mixed_case_extensions():
    assert Strongest_Extension("MyClass", ["MiXeD1", "mIxEd2", "MiXeD3"]) == "MyClass.MiXeD1"

def test_empty_extension():
    assert Strongest_Extension("MyClass", ["", "Extension1"]) == "MyClass.Extension1"

def test_extensions_with_different_lengths():
    assert Strongest_Extension("MyClass", ["ABC", "AB"]) == "MyClass.AB"

def test_extensions_with_special_characters():
    assert Strongest_Extension("MyClass", ["Extension!", "Extension2"]) == "MyClass.Extension!"

def test_extensions_with_unicode():
    assert Strongest_Extension("MyClass", ["你好", "世界"]) == "MyClass.你好"
    assert Strongest_Extension("你好世界", ["Extension1", "Extension2"]) == "你好世界.Extension1"

def test_very_long_extension():
    long_extension = "A" * 1000
    assert Strongest_Extension("MyClass", [long_extension, "B"]) == "MyClass." + long_extension

def test_none_extension():
    assert Strongest_Extension("MyClass", ["Extension1", None, "Extension2"]) == "MyClass.Extension1"

def test_different_strength_definition():
    # Tests that the longest string is chosen when extensions have equal strength
    assert Strongest_Extension("MyClass", ["AB", "ABC"]) == "MyClass.ABC"

def test_multiple_none_values():
    assert Strongest_Extension("MyClass", [None, None, None]) == "MyClass."

def test_special_character_extension():
    assert Strongest_Extension("MyClass", ["!@#$%^"]) == "MyClass.!@#$%^"

def test_numeric_class_name():
    assert Strongest_Extension("123", ["Extension1", "Extension2"]) == "123.Extension1"
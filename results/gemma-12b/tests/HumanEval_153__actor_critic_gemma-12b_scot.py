
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

def test_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_single_extension():
    assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

def test_multiple_extensions_different_strengths():
    extensions = ["AA", "Be", "CC"]
    assert Strongest_Extension("MyClass", extensions) == "MyClass.AA"

def test_multiple_extensions_same_strength():
    extensions = ["AA", "BB", "CC"]
    assert Strongest_Extension("MyClass", extensions) == "MyClass.AA"

def test_extension_no_uppercase():
    assert Strongest_Extension("MyClass", ["lowercase"]) == "MyClass.lowercase"

def test_extension_no_lowercase():
    assert Strongest_Extension("MyClass", ["UPPERCASE"]) == "MyClass.UPPERCASE"

def test_extension_mixed_case():
    assert Strongest_Extension("MyClass", ["MiXeDCase"]) == "MyClass.MiXeDCase"

def test_empty_class_name():
    assert Strongest_Extension("", ["Extension1"]) == ".Extension1"

def test_class_name_with_special_characters():
    assert Strongest_Extension("My!Class#", ["Extension1"]) == "My!Class#.Extension1"

def test_extension_with_numbers():
    assert Strongest_Extension("MyClass", ["Ext123"]) == "MyClass.Ext123"

def test_extension_with_symbols():
    assert Strongest_Extension("MyClass", ["Ext$#@"]) == "MyClass.Ext$#@"

def test_class_name_and_extension_empty():
    assert Strongest_Extension("", []) == "."
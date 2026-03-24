
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
    assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_multiple_extensions_same_strength_first_wins():
    assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

def test_negative_strength():
    assert Strongest_Extension("MyClass", ["SErviNGSliCes"]) == "MyClass.SErviNGSliCes"

def test_positive_strength():
    assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

def test_mixed_case_extensions():
    assert Strongest_Extension("MyClass", ["aA", "Bb", "Cc"]) == "MyClass.aA"

def test_extension_with_numbers():
    assert Strongest_Extension("MyClass", ["A1", "B2", "C3"]) == "MyClass.A1"

def test_extension_with_symbols():
    assert Strongest_Extension("MyClass", ["A!", "B@", "C#"]) == "MyClass.A!"

def test_class_name_with_underscores():
    assert Strongest_Extension("My_Class", ["AA", "Be", "CC"]) == "My_Class.AA"

def test_class_name_with_spaces():
    assert Strongest_Extension("My Class", ["AA", "Be", "CC"]) == "My Class.AA"

def test_class_name_empty():
    assert Strongest_Extension("", ["AA", "Be", "CC"]) == ".AA"

def test_multiple_extensions_with_same_strength_and_different_lengths():
    assert Strongest_Extension("MyClass", ["AA", "BB", "A"]) == "MyClass.AA"

def test_complex_extensions():
    extensions = ["SErviNGSliCes", "Cheese", "StuFfed"]
    assert Strongest_Extension("Slices", extensions) == "Slices.SErviNGSliCes"

def test_all_extensions_have_zero_strength():
    assert Strongest_Extension("MyClass", ["aa", "bb", "cc"]) == "MyClass.aa"

def test_extension_with_only_uppercase():
    assert Strongest_Extension("MyClass", ["AAAA"]) == "MyClass.AAAA"

def test_extension_with_only_lowercase():
    assert Strongest_Extension("MyClass", ["aaaa"]) == "MyClass.aaaa"

def test_extension_with_mixed_case_and_same_strength():
    assert Strongest_Extension("MyClass", ["aA", "Aa"]) == "MyClass.aA"

def test_long_extensions():
    assert Strongest_Extension("MyClass", ["ThisIsALongExtension", "AnotherLongExtension"]) == "MyClass.ThisIsALongExtension"

def test_all_lowercase():
    assert Strongest_Extension("MyClass", ["be", "cc", "aa"]) == "MyClass.aa"

def test_all_uppercase():
    assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

def test_extension_with_special_characters():
    assert Strongest_Extension("MyClass", ["A@", "b#", "C$"]) == "MyClass.A@"

def test_extension_with_unicode_characters():
    assert Strongest_Extension("MyClass", ["Aé", "bç", "Cü"]) == "MyClass.Aé"

def test_extension_with_whitespace():
    assert Strongest_Extension("MyClass", [" A ", "b ", "C "]) == "MyClass. A "
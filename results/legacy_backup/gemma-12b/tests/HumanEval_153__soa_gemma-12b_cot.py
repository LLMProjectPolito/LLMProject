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

def test_Strongest_Extension_basic():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_Strongest_Extension_same_strength():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_Strongest_Extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_Strongest_Extension_single_extension():
    assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

def test_Strongest_Extension_all_uppercase():
    assert Strongest_Extension("MyClass", ["AAAA"]) == "MyClass.AAAA"

def test_Strongest_Extension_all_lowercase():
    assert Strongest_Extension("MyClass", ["aaaa"]) == "MyClass.aaaa"

def test_Strongest_Extension_mixed_case():
    assert Strongest_Extension("MyClass", ["aA"]) == "MyClass.aA"

def test_Strongest_Extension_negative_strength():
    assert Strongest_Extension("MyClass", ["abc"]) == "MyClass.abc"

def test_Strongest_Extension_zero_strength():
    assert Strongest_Extension("MyClass", ["ab"]) == "MyClass.ab"

def test_Strongest_Extension_class_name_empty():
    assert Strongest_Extension("", ["Extension1"]) == ".Extension1"

def test_Strongest_Extension_class_name_with_spaces():
    assert Strongest_Extension("My Class", ["Extension1"]) == "My Class.Extension1"

def test_Strongest_Extension_extension_with_spaces():
    assert Strongest_Extension("MyClass", ["Extension 1"]) == "MyClass.Extension 1"

def test_Strongest_Extension_multiple_extensions_same_strength():
    assert Strongest_Extension("MyClass", ["AA", "CC", "BB"]) == "MyClass.AA"

def test_Strongest_Extension_long_extensions():
    assert Strongest_Extension("MyClass", ["ThisIsALongExtension", "AnotherLongExtension"]) == "MyClass.ThisIsALongExtension"

def test_Strongest_Extension_special_characters():
    assert Strongest_Extension("MyClass", ["!@#", "$%^"]) == "MyClass.!@#"
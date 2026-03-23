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

def test_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_single_extension():
    assert Strongest_Extension("MyClass", ["Extension"]) == "MyClass.Extension"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_multiple_extensions_same_strengths():
    assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

def test_extensions_with_mixed_case():
    assert Strongest_Extension("MyClass", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "MyClass.SErviNGSliCes"

def test_extensions_with_negative_strength():
    assert Strongest_Extension("MyClass", ["aA", "bB", "cC"]) == "MyClass.aA"

def test_extensions_with_zero_strength():
    assert Strongest_Extension("MyClass", ["Aa", "Bb", "Cc"]) == "MyClass.Aa"

def test_class_name_with_special_characters():
    assert Strongest_Extension("My_Class!", ["Extension"]) == "My_Class!.Extension"

def test_extension_name_with_special_characters():
    assert Strongest_Extension("MyClass", ["Extension!"]) == "MyClass.Extension!"

def test_class_name_and_extension_with_special_characters():
    assert Strongest_Extension("My_Class!", ["Extension!"]) == "My_Class!.Extension!"

def test_long_class_name():
    assert Strongest_Extension("ThisIsAVeryLongClassName", ["Extension"]) == "ThisIsAVeryLongClassName.Extension"

def test_long_extension_name():
    assert Strongest_Extension("MyClass", ["ThisIsAVeryLongExtensionName"]) == "MyClass.ThisIsAVeryLongExtensionName"

def test_class_name_and_extension_with_numbers():
    assert Strongest_Extension("Class123", ["Extension456"]) == "Class123.Extension456"

def test_empty_class_name():
    assert Strongest_Extension("", ["Extension"]) == ".Extension"

def test_empty_extension_name():
    assert Strongest_Extension("MyClass", [""]) == "MyClass."
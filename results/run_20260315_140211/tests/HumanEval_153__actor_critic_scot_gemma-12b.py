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
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
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

def test_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_single_extension():
    assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

def test_extensions_with_equal_uppercase_and_lowercase():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_extension_with_zero_strength():
    assert Strongest_Extension("MyClass", ["Aa"]) == "MyClass.Aa"

def test_extension_with_negative_strength():
    assert Strongest_Extension("MyClass", ["abc"]) == "MyClass.abc"

def test_extension_with_only_uppercase():
    assert Strongest_Extension("MyClass", ["AAAA"]) == "MyClass.AAAA"

def test_extension_with_only_lowercase():
    assert Strongest_Extension("MyClass", ["aaaa"]) == "MyClass.aaaa"

def test_class_name_with_special_characters():
    assert Strongest_Extension("My_Class!", ["Extension1"]) == "My_Class!.Extension1"

def test_empty_class_name():
    assert Strongest_Extension("", ["Extension1"]) == ".Extension1"

def test_special_characters_and_mixed_case():
    assert Strongest_Extension("MyClass", ["MiXeDCase!"]) == "MyClass.MiXeDCase!"

def test_multiple_extensions_with_equal_strength():
    assert Strongest_Extension("MyClass", ["AB", "Ba", "CC"]) == "MyClass.AB"

def test_extremely_long_extension():
    long_extension = "A" * 5000
    assert Strongest_Extension("MyClass", [long_extension]) == "MyClass." + long_extension

def test_numeric_extension():
    assert Strongest_Extension("MyClass", ["12345"]) == "MyClass.12345"

def test_unicode_extension():
    assert Strongest_Extension("MyClass", ["Café"]) == "MyClass.Café"
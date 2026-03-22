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
        return class_name + "."
    
    strongest_extension = extensions[0]
    max_strength = 0
    
    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
            
    return class_name + "." + strongest_extension

def test_basic_case():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_empty_extension_list():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_single_extension():
    assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

def test_tie_breaker():
    assert Strongest_Extension("MyClass", ["AA", "BB"]) == "MyClass.AA"

def test_all_uppercase():
    assert Strongest_Extension("MyClass", ["AAA", "BBB"]) == "MyClass.AAA"

def test_all_lowercase():
    assert Strongest_Extension("MyClass", ["aaa", "bbb"]) == "MyClass.aaa"

def test_mixed_case():
    assert Strongest_Extension("MyClass", ["aA", "Bb", "Cc"]) == "MyClass.aA"

def test_empty_extension_name():
    assert Strongest_Extension("MyClass", ["", "Extension"]) == "MyClass.Extension"

def test_class_name_with_numbers():
    assert Strongest_Extension("MyClass123", ["Extension"]) == "MyClass123.Extension"

def test_extension_name_with_numbers():
    assert Strongest_Extension("MyClass", ["Extension123"]) == "MyClass.Extension123"

def test_class_name_with_special_chars():
    assert Strongest_Extension("My_Class!", ["Extension"]) == "My_Class!.Extension"

def test_extension_name_with_special_chars():
    assert Strongest_Extension("MyClass", ["Extension!"]) == "MyClass.Extension!"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("MyClass", ["aA", "Aa", "bB"]) == "MyClass.aA"

def test_negative_strength():
    assert Strongest_Extension("MyClass", ["abc", "ABC"]) == "MyClass.ABC"

def test_long_extensions():
    assert Strongest_Extension("MyClass", ["VeryLongExtensionName", "Short"]) == "MyClass.VeryLongExtensionName"
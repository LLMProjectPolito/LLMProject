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
        cap_count = 0
        sm_count = 0
        for char in extension:
            if char.isupper():
                cap_count += 1
            elif char.islower():
                sm_count += 1
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + "." + strongest_extension

def test_Strongest_Extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_Strongest_Extension_single_extension():
    assert Strongest_Extension("MyClass", ["Extension1"]) == "MyClass.Extension1"

def test_Strongest_Extension_multiple_extensions_different_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_Strongest_Extension_multiple_extensions_same_strengths():
    assert Strongest_Extension("MyClass", ["AA", "CC", "BB"]) == "MyClass.AA"

def test_Strongest_Extension_example_case():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_Strongest_Extension_all_uppercase():
    assert Strongest_Extension("MyClass", ["AAAA"]) == "MyClass.AAAA"

def test_Strongest_Extension_all_lowercase():
    assert Strongest_Extension("MyClass", ["aaaa"]) == "MyClass.aaaa"

def test_Strongest_Extension_mixed_case():
    assert Strongest_Extension("MyClass", ["aA"]) == "MyClass.aA"

def test_Strongest_Extension_numbers_and_symbols():
    assert Strongest_Extension("MyClass", ["123", "!@#"]) == "MyClass.123"

def test_Strongest_Extension_extension_with_space():
    assert Strongest_Extension("MyClass", ["Extension With Space"]) == "MyClass.Extension With Space"

def test_Strongest_Extension_class_name_with_space():
    assert Strongest_Extension("My Class", ["Extension1"]) == "My Class.Extension1"

def test_Strongest_Extension_class_name_and_extension_with_space():
    assert Strongest_Extension("My Class", ["Extension With Space"]) == "My Class.Extension With Space"
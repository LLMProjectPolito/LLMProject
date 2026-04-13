
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
    strongest_extension = None
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        
        try:
            strength = cap_count - sm_count
        except TypeError:
            strength = float('-inf')

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    if strongest_extension is None:
        return f"{class_name}."
    else:
        return f"{class_name}.{strongest_extension}"

def test_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_single_extension():
    assert Strongest_Extension("MyClass", ["Extension"]) == "MyClass.Extension"

def test_multiple_extensions():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_equal_strength_first_wins():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_all_uppercase():
    assert Strongest_Extension("TestClass", ["UPPER", "CASE"]) == "TestClass.UPPER"

def test_all_lowercase():
    assert Strongest_Extension("TestClass", ["lower", "case"]) == "TestClass.lower"

def test_mixed_case():
    assert Strongest_Extension("TestClass", ["MiXeD", "CaSe"]) == "TestClass.MiXeD"

def test_numbers_and_symbols():
    assert Strongest_Extension("TestClass", ["Ext123!", "Ext456@"]) == "TestClass.Ext123!"

def test_empty_string_extension():
    assert Strongest_Extension("TestClass", ["", "Extension"]) == "TestClass.Extension"

def test_extension_with_spaces():
    assert Strongest_Extension("TestClass", ["Extension With Spaces", "AnotherExtension"]) == "TestClass.Extension With Spaces"

def test_negative_strength():
    assert Strongest_Extension("TestClass", ["aA", "bB"]) == "TestClass.aA"

def test_large_number_of_extensions():
    extensions = ["Ext" + str(i) for i in range(100)]
    assert Strongest_Extension("TestClass", extensions) == "TestClass.Ext0"

def test_class_name_with_spaces():
    assert Strongest_Extension("My Class", ["Extension"]) == "My Class.Extension"

def test_class_name_with_numbers():
    assert Strongest_Extension("MyClass123", ["Extension"]) == "MyClass123.Extension"

def test_empty_extensions_2():
    assert Strongest_Extension("Class", []) == "Class."

def test_single_extension_2():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_multiple_extensions_2():
    assert Strongest_Extension("Class", ["Extension1", "Extension2"]) == "Class.Extension1"

def test_same_strength_first_wins_2():
    assert Strongest_Extension("Class", ["AA", "Be", "CC"]) == "Class.AA"

def test_negative_strength_2():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_all_uppercase_2():
    assert Strongest_Extension("Class", ["AAA", "BBB"]) == "Class.AAA"

def test_all_lowercase_2():
    assert Strongest_Extension("Class", ["aaa", "bbb"]) == "Class.aaa"

def test_mixed_case_2():
    assert Strongest_Extension("Class", ["aA", "Aa"]) == "Class.aA"

def test_empty_string_extension_2():
    assert Strongest_Extension("Class", [""]) == "Class."

def test_extension_with_numbers_2():
    assert Strongest_Extension("Class", ["Ext1", "Ext2"]) == "Class.Ext1"

def test_extension_with_special_characters_2():
    assert Strongest_Extension("Class", ["Ext!", "Ext@"]) == "Class.Ext!"

def test_class_name_with_numbers_2():
    assert Strongest_Extension("Class123", ["Ext1", "Ext2"]) == "Class123.Ext1"

def test_class_name_with_special_characters_2():
    assert Strongest_Extension("Class!", ["Ext1", "Ext2"]) == "Class!.Ext1"

def test_long_extensions_2():
    assert Strongest_Extension("Class", ["VeryLongExtension1", "VeryLongExtension2"]) == "Class.VeryLongExtension1"

def test_extensions_with_same_length_2():
    assert Strongest_Extension("Class", ["ABCdef", "aBcDef"]) == "Class.ABCdef"

def test_extensions_with_different_lengths_2():
    assert Strongest_Extension("Class", ["AB", "ABCdef"]) == "Class.AB"

def test_strength_zero_2():
    assert Strongest_Extension("Class", ["Ab", "aB"]) == "Class.Ab"

def test_multiple_extensions_same_strength_2():
    assert Strongest_Extension("Class", ["Aa", "aA", "Bb", "bB"]) == "Class.Aa"

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

def test_empty_extensions():
    assert Strongest_Extension("Class", []) == "Class."

def test_single_extension():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_multiple_extensions():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_equal_strength_first_wins():
    assert Strongest_Extension("Class", ["AA", "Be", "CC"]) == "Class.AA"

def test_all_uppercase():
    assert Strongest_Extension("Class", ["AAA", "BBB", "CCC"]) == "Class.AAA"

def test_all_lowercase():
    assert Strongest_Extension("Class", ["aaa", "bbb", "ccc"]) == "Class.aaa"

def test_mixed_case():
    assert Strongest_Extension("Class", ["aA", "Aa", "AA"]) == "Class.AA"

def test_negative_strength():
    assert Strongest_Extension("Class", ["abc", "def", "ghi"]) == "Class.abc"

def test_zero_strength():
    assert Strongest_Extension("Class", ["aA", "Bb", "Cc"]) == "Class.aA"

def test_long_extension_names():
    assert Strongest_Extension("Class", ["VeryLongExtensionName", "ShortName"]) == "Class.VeryLongExtensionName"

def test_extension_names_with_numbers():
    assert Strongest_Extension("Class", ["Extension123", "AnotherExtension"]) == "Class.Extension123"

def test_extension_names_with_special_characters():
    assert Strongest_Extension("Class", ["Extension!", "AnotherExtension"]) == "Class.Extension!"

def test_class_name_with_numbers():
    assert Strongest_Extension("Class123", ["Extension"]) == "Class123.Extension"

def test_class_name_with_special_characters():
    assert Strongest_Extension("Class!", ["Extension"]) == "Class!.Extension"

def test_multiple_extensions_with_same_strength():
    assert Strongest_Extension("Class", ["ab", "cd", "ef"]) == "Class.ab"

def test_multiple_extensions_with_varying_strengths():
    assert Strongest_Extension("Class", ["aB", "Ab", "bA", "BA"]) == "Class.aB"
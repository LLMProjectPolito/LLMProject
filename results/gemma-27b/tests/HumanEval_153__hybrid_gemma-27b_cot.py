
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
    assert Strongest_Extension("Class", ["Extension1", "Extension2"]) == "Class.Extension1"

def test_equal_strength_first_wins():
    assert Strongest_Extension("Class", ["AA", "BB"]) == "Class.AA"

def test_all_uppercase():
    assert Strongest_Extension("Class", ["AAA", "BBB", "CCC"]) == "Class.AAA"

def test_all_lowercase():
    assert Strongest_Extension("Class", ["aaa", "bbb", "ccc"]) == "Class.aaa"

def test_mixed_case():
    assert Strongest_Extension("Class", ["aA", "Aa", "AA"]) == "Class.AA"

def test_empty_string_extension():
    assert Strongest_Extension("Class", [""]) == "Class."

def test_extension_with_numbers():
    assert Strongest_Extension("Class", ["Ext1", "Ext2"]) == "Class.Ext1"

def test_extension_with_special_characters():
    assert Strongest_Extension("Class", ["Ext!", "Ext@"]) == "Class.Ext!"

def test_class_name_with_numbers():
    assert Strongest_Extension("Class123", ["ExtA", "ExtB"]) == "Class123.ExtA"

def test_class_name_with_special_characters():
    assert Strongest_Extension("Class!", ["ExtA", "ExtB"]) == "Class!.ExtA"

def test_negative_strength():
    assert Strongest_Extension("Class", ["abc", "ABC"]) == "Class.ABC"
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_zero_strength():
    assert Strongest_Extension("Class", ["aB", "Ab"]) == "Class.aB"

def test_long_extensions():
    assert Strongest_Extension("Class", ["VeryLongExtension1", "VeryLongExtension2"]) == "Class.VeryLongExtension1"

def test_extensions_with_same_length():
    assert Strongest_Extension("Class", ["AbCd", "aBcD"]) == "Class.AbCd"
    assert Strongest_Extension("Class", ["ABCdef", "aBcDef"]) == "Class.ABCdef"

def test_extensions_with_different_lengths():
    assert Strongest_Extension("Class", ["A", "AB"]) == "Class.AB"
    assert Strongest_Extension("Class", ["AB", "ABCdef"]) == "Class.AB"

def test_strength_zero():
    assert Strongest_Extension("Class", ["Ab", "aB"]) == "Class.Ab"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("Class", ["Aa", "aA", "Bb", "bB"]) == "Class.Aa"
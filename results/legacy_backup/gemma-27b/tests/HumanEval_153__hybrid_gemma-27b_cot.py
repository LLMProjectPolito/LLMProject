import pytest

def test_empty_extensions():
    assert Strongest_Extension("Class", []) == "Class."

def test_single_extension():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_multiple_extensions():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

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

def test_zero_strength():
    assert Strongest_Extension("Class", ["aB", "Ab"]) == "Class.aB"

def test_long_extensions():
    assert Strongest_Extension("Class", ["VeryLongExtension1", "VeryLongExtension2"]) == "Class.VeryLongExtension1"

def test_extensions_with_same_length():
    assert Strongest_Extension("Class", ["AbCd", "aBcD"]) == "Class.AbCd"

def test_extensions_with_different_lengths():
    assert Strongest_Extension("Class", ["A", "AB"]) == "Class.A"

def test_negative_strength_2():
    assert Strongest_Extension("Class", ["a", "A"]) == "Class.A"

def test_zero_strength_2():
    assert Strongest_Extension("Class", ["aA", "Bb"]) == "Class.aA"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("Class", ["ab", "cd", "ef"]) == "Class.ab"

def test_mixed_case_and_numbers():
    assert Strongest_Extension("Class", ["ExT1", "eXt2"]) == "Class.ExT1"
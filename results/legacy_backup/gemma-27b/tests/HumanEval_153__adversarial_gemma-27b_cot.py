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

def test_empty_string_extension():
    assert Strongest_Extension("Class", ["", "Extension"]) == "Class."

def test_extension_with_numbers():
    assert Strongest_Extension("Class", ["Ext1", "Ext2"]) == "Class.Ext1"

def test_extension_with_special_characters():
    assert Strongest_Extension("Class", ["Ext!", "Ext@"]) == "Class.Ext!"

def test_class_name_with_numbers():
    assert Strongest_Extension("Class123", ["Ext"]) == "Class123.Ext"

def test_class_name_with_special_characters():
    assert Strongest_Extension("Class!", ["Ext"]) == "Class!.Ext"

def test_long_extensions():
    assert Strongest_Extension("Class", ["VeryLongExtension1", "VeryLongExtension2"]) == "Class.VeryLongExtension1"

def test_negative_strength():
    assert Strongest_Extension("Class", ["a", "A"]) == "Class.A"

def test_zero_strength():
    assert Strongest_Extension("Class", ["aA", "Aa"]) == "Class.aA"
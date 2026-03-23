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
    assert Strongest_Extension("Class", ["VeryLongExtensionName", "ShortExtension"]) == "Class.VeryLongExtensionName"

def test_extension_names_with_numbers():
    assert Strongest_Extension("Class", ["Extension123", "Extension456"]) == "Class.Extension123"

def test_extension_names_with_special_characters():
    assert Strongest_Extension("Class", ["Extension!", "Extension@"]) == "Class.Extension!"

def test_class_name_with_numbers():
    assert Strongest_Extension("Class123", ["ExtensionA", "ExtensionB"]) == "Class123.ExtensionA"

def test_class_name_with_special_characters():
    assert Strongest_Extension("Class!", ["ExtensionA", "ExtensionB"]) == "Class!.ExtensionA"

def test_multiple_extensions_with_same_strength():
    assert Strongest_Extension("Class", ["aA", "Aa", "bB"]) == "Class.aA"
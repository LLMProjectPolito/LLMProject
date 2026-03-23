import pytest
import math

def test_empty_extensions_list():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_extension_with_only_uppercase():
    assert Strongest_Extension("MyClass", ["AAAA"]) == "MyClass.AAAA"

def test_extension_with_only_lowercase():
    assert Strongest_Extension("MyClass", ["aaaa"]) == "MyClass.aaaa"

def test_extension_with_mixed_case_and_same_strength():
    assert Strongest_Extension("MyClass", ["Aa", "aA"]) == "MyClass.Aa"

def test_extension_with_special_characters():
    assert Strongest_Extension("MyClass", ["A!", "b?"]) == "MyClass.A!"

def test_extension_with_numbers():
    assert Strongest_Extension("MyClass", ["A1", "b2"]) == "MyClass.A1"

def test_extension_with_unicode_characters():
    assert Strongest_Extension("MyClass", ["你好", "世界"]) == "MyClass.你好"

def test_extension_with_whitespace():
    assert Strongest_Extension("MyClass", ["A ", " b"]) == "MyClass.A "
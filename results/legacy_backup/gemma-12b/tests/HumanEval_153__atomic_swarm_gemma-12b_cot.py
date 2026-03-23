import pytest
import math

def test_basic():
    class_name = "Slices"
    extensions = ['SErviNGSliCes', 'Cheese', 'StuFfed']
    expected = "Slices.SErviNGSliCes"
    assert Strongest_Extension(class_name, extensions) == expected

def test_empty_extensions():
    """Test with an empty list of extensions."""
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_all_zero_strength():
    """Test when all extensions have zero strength (equal uppercase and lowercase)."""
    assert Strongest_Extension("MyClass", ["aa", "BB", "cc"]) == "MyClass.aa"

def test_negative_strength_dominates():
    """Test when a negative strength extension is the strongest."""
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_equal_strength_first_wins():
    """Test when multiple extensions have the same strength, the first one wins."""
    assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

def test_mixed_strengths():
    """Test with a mix of positive and negative strengths."""
    assert Strongest_Extension("MyClass", ["aA", "bB", "cC"]) == "MyClass.aA"

def test_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_invalid_class_name():
    assert Strongest_Extension(123, ["Extension1", "Extension2"]) == "123.Extension1"

def test_mixed_case_extensions():
    assert Strongest_Extension("Class", ["aA", "Bb", "cC"]) == "Class.aA"

def test_same_strength_extensions():
    assert Strongest_Extension("Class", ["AA", "BB", "CC"]) == "Class.AA"

def test_negative_strength():
    assert Strongest_Extension("Class", ["aA", "bB", "c"]) == "Class.aA"

def test_extension_with_numbers():
    assert Strongest_Extension("Class", ["A1", "b2", "C3"]) == "Class.A1"

def test_extension_with_symbols():
    assert Strongest_Extension("Class", ["A!", "b#", "C$"]) == "Class.A!"
import pytest
import math


# Focus: Boundary Values
def test_boundary_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_boundary_single_extension():
    assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

def test_boundary_equal_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

# Focus: Logic Branches
def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_strongest_extension_single_extension():
    assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

def test_strongest_extension_multiple_extensions_different_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_strongest_extension_multiple_extensions_same_strength():
    assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("TestClass", ["aA", "Bb", "cC"]) == "TestClass.aA"

# Focus: Type Scenarios
def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_strongest_extension_single_extension():
    assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

def test_strongest_extension_multiple_extensions_different_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_strongest_extension_multiple_extensions_same_strengths():
    assert Strongest_Extension("MyClass", ["AA", "BB", "CC"]) == "MyClass.AA"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("TestClass", ["aA", "Bb", "cC"]) == "TestClass.aA"
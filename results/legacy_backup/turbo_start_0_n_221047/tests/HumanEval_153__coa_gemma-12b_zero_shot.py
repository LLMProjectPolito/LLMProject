import pytest
import math


# Focus: Boundary Values
def test_boundary_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_boundary_single_extension():
    assert Strongest_Extension("MyClass", ["A"]) == "MyClass.A"

def test_boundary_equal_strengths():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

# Focus: Logic Branches
def test_strongest_extension_positive_strength():
    assert Strongest_Extension("MyClass", ["AA", "Be", "CC"]) == "MyClass.AA"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_strongest_extension_equal_strength_first_wins():
    assert Strongest_Extension("TestClass", ["AB", "aB", "ba"]) == "TestClass.AB"

# Focus: Type Scenarios
def test_strongest_extension_basic():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_strongest_extension_negative():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_strongest_extension_equal_strength():
    assert Strongest_Extension("BaseClass", ["ExtensionA", "extensionB", "ExtensionC"]) == "BaseClass.ExtensionA"
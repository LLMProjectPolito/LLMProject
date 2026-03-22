import pytest
import math


# Focus: Boundary Values
def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_strongest_extension_single_extension():
    assert Strongest_Extension("MyClass", ["AA"]) == "MyClass.AA"

def test_strongest_extension_same_strength():
    assert Strongest_Extension("MyClass", ["AA", "BB"]) == "MyClass.AA"

# Focus: Logic Branches
def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_negative():
    assert Strongest_Extension('Test', ['abc', 'def', 'ghi']) == 'Test.abc'

# Focus: Type Scenarios
def test_strongest_extension_basic():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_strongest_extension_same_strength():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."
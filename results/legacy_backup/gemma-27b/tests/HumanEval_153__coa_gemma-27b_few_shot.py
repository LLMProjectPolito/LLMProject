import pytest
import math


# Focus: Boundary Values
def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("Class", []) == "Class."

def test_strongest_extension_single_extension():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_strongest_extension_equal_strength_first():
    assert Strongest_Extension("Class", ["AA", "BB"]) == "Class.AA"

# Focus: Equivalence Partitioning
def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_equal_strength():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_negative():
    assert Strongest_Extension('Test', ['abc', 'def', 'ghi']) == 'Test.abc'

# Focus: Error Handling/Invalid Input
def test_strongest_extension_invalid_class_name():
    assert Strongest_Extension(123, ['AA', 'Be']) == '123.AA'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('Class', []) == 'Class.None'

def test_strongest_extension_invalid_extension_names():
    assert Strongest_Extension('Class', [123, 'Be']) == 'Class.Be'
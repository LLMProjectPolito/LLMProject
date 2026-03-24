import pytest
import math


# Focus: Boundary Values
import pytest

def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('my_class', []) == 'my_class.'

# Focus: Type Scenarios
import pytest

def test_strongest_extension_uppercase_only():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_negative_strength():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_equal_strengths():
    assert Strongest_Extension('my_class', ['AA', 'BB']) == 'my_class.AA'

# Focus: Logic Branches
import pytest

def test_strongest_extension_single_extension():
    assert Strongest_Extension('Slices', ['SErviNGSliCes']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_multiple_extensions_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('my_class', []) == 'my_class.'
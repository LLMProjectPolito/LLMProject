import pytest
import math


# Focus: Boundary Values
def test_strongest_extension_1():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_2():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.CC'

# Focus: Type Scenarios
def test_strongest_extension_1():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_2():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.CC'

# Focus: Logic Branches
def test_strongest_extension_1():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_2():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.CC'
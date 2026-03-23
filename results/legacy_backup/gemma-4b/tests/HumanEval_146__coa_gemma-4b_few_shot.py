import pytest
import math


# Focus: Boundary Values
def test_specialFilter_positive():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_negative():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

# Focus: Type Scenarios
def test_specialFilter_positive():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_negative():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

# Focus: Logic Branches
def test_specialFilter_positive():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_mixed():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_negative():
    assert specialFilter([-11, -13, -15]) == 0
import pytest
import math


# Focus: Boundary Values
def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

# Focus: Type Scenarios
def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

# Focus: Logic Branches
def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5
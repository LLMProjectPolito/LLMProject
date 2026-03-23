import pytest
import math


# Focus: Boundary Values
def test_special_factorial_one():
    assert special_factorial(1) == 1

def test_special_factorial_two():
    assert special_factorial(2) == 2

def test_special_factorial_three():
    assert special_factorial(3) == 12

# Focus: Error Handling
import pytest

def test_special_factorial_negative_input():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_zero_input():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_invalid_type():
    with pytest.raises(TypeError):
        special_factorial("abc")

# Focus: Logic Branches
def test_special_factorial_positive():
    assert special_factorial(4) == 288
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12

def test_special_factorial_zero():
    assert special_factorial(0) == 1
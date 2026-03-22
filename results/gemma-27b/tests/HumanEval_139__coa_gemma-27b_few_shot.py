import pytest
import math


# Focus: Boundary Values
def test_special_factorial_boundary_one():
    assert special_factorial(1) == 1

def test_special_factorial_boundary_two():
    assert special_factorial(2) == 2

def test_special_factorial_boundary_zero():
    with pytest.raises(ValueError):
        special_factorial(0)

# Focus: Equivalence Partitioning
import pytest

def test_special_factorial_valid_input():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288

def test_special_factorial_boundary_value():
    assert special_factorial(5) == 34560

# Focus: Error Handling/Invalid Input
import pytest

def test_special_factorial_negative_input():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_zero_input():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_non_integer_input():
    with pytest.raises(TypeError):
        special_factorial(3.14)
import pytest
import math


# Focus: Boundary Values
import pytest

def test_special_factorial_boundary_zero():
    """Test with n = 1 (boundary case)."""
    assert special_factorial(1) == 1

def test_special_factorial_boundary_two():
    """Test with n = 2 (boundary case)."""
    assert special_factorial(2) == 2

def test_special_factorial_boundary_three():
    """Test with n = 3 (boundary case)."""
    assert special_factorial(3) == 18

# Focus: Error Handling
import pytest

def test_special_factorial_negative_input():
    with pytest.raises(ValueError):
        special_factorial(-1)

def test_special_factorial_zero_input():
    with pytest.raises(ValueError):
        special_factorial(0)

def test_special_factorial_invalid_type_input():
    with pytest.raises(TypeError):
        special_factorial("abc")

# Focus: Logic Branches
import pytest

def test_special_factorial_positive_integer():
    assert special_factorial(4) == 288
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(5) == 34560

def test_special_factorial_edge_case():
    assert special_factorial(0) == 1

def test_special_factorial_large_input():
    assert special_factorial(6) == 4320 * 720 * 120 * 24 * 6 * 1 == 29859840000
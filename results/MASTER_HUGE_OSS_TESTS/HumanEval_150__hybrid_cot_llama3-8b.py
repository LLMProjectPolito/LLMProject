import pytest
from math import sqrt

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_valid_inputs():
    """Test with valid inputs."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5

def test_n_is_prime_single_digit():
    """Test when n is a single-digit prime number."""
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 8, 5) == 5

def test_n_is_prime_multi_digit():
    """Test when n is a multi-digit prime number."""
    assert x_or_y(23, 34, 12) == 34
    assert x_or_y(37, 8, 5) == 5

def test_n_is_not_prime_even_composite():
    """Test when n is an even composite number."""
    assert x_or_y(4, 34, 12) == 12
    assert x_or_y(6, 8, 5) == 5

def test_n_is_not_prime_odd_composite():
    """Test when n is an odd composite number."""
    assert x_or_y(9, 34, 12) == 12
    assert x_or_y(15, 8, 5) == 5

def test_edge_cases_n_zero_one():
    """Test when n is 0 or 1."""
    with pytest.raises(TypeError):
        x_or_y(0, 34, 12)
    with pytest.raises(TypeError):
        x_or_y(1, 34, 12)

def test_edge_cases_x_y_zero_one():
    """Test when x or y is 0 or 1."""
    assert x_or_y(7, 0, 12) == 12
    assert x_or_y(7, 34, 0) == 34
    assert x_or_y(7, 1, 12) == 34
    assert x_or_y(7, 34, 1) == 5

def test_edge_case_x_equals_y():
    """Test when x equals y."""
    assert x_or_y(5, 10, 10) == 10

def test_negative_number():
    """Test with negative number."""
    assert x_or_y(-7, 34, 12) == 12

def test_non_integer_input():
    """Test with non-integer input (float)."""
    assert x_or_y(7.5, 34, 12) == 12

def test_invalid_inputs_n_not_integer():
    """Test when n is not an integer."""
    with pytest.raises(TypeError):
        x_or_y(3.14, 34, 12)

def test_invalid_inputs_x_y_not_integer():
    """Test when x or y is not an integer."""
    with pytest.raises(TypeError):
        x_or_y(7, 34.14, 12)
    with pytest.raises(TypeError):
        x_or_y(7, 34, 12.14)

def test_boundary_conditions_lower_bound():
    """Test when n is at the lower bound of a prime number."""
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(3, 8, 5) == 5

def test_boundary_conditions_upper_bound():
    """Test when n is at the upper bound of a prime number."""
    assert x_or_y(997, 34, 12) == 34
    assert x_or_y(999, 8, 5) == 5

def test_prime_number():
    """Test with prime number."""
    assert x_or_y(7, 34, 12) == 34

def test_non_prime_number():
    """Test with non-prime number."""
    assert x_or_y(15, 8, 5) == 5

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest
import math


# Focus: Boundary Values
def test_generate_integers_boundary_equal_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_boundary_equal_odd():
    assert generate_integers(5, 5) == []

def test_generate_integers_boundary_digit_threshold():
    assert generate_integers(8, 11) == [8]

# Focus: Logic Branches
def test_generate_integers_order_branches():
    # Branch: a < b
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    # Branch: a > b (should still return ascending)
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_empty_branches():
    # Branch: Range contains no even digits (outside 0-9)
    assert generate_integers(10, 14) == []
    # Branch: Range contains only odd digits
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []

def test_generate_integers_single_value_branches():
    # Branch: a == b and is even
    assert generate_integers(4, 4) == [4]
    # Branch: a == b and is odd
    assert generate_integers(5, 5) == []

# Focus: Type Scenarios
import pytest

def test_generate_integers_return_type():
    """Verify that the function returns a list."""
    assert isinstance(generate_integers(2, 8), list)

def test_generate_integers_element_type():
    """Verify that all elements in the returned list are integers."""
    result = generate_integers(2, 8)
    assert all(isinstance(x, int) for x in result)

def test_generate_integers_invalid_input_type():
    """Verify that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        generate_integers("2", "8")
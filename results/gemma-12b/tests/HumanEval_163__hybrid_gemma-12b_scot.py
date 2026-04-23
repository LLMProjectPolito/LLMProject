
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
from your_module import generate_integers  # Replace your_module

def test_ascending_range():
    """Tests a basic ascending range."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_descending_range():
    """Tests a basic descending range."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_mixed_range():
    """Tests a range with both even and odd numbers."""
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_no_even_numbers():
    """Tests a range with no even numbers."""
    assert generate_integers(1, 3) == []

def test_single_even_number():
    """Tests a range with only one even number."""
    assert generate_integers(2, 3) == [2]

def test_same_numbers_even():
    """Tests the edge case where a and b are equal and even."""
    assert generate_integers(4, 4) == [4]

def test_same_numbers_odd():
    """Tests the edge case where a and b are equal and odd."""
    assert generate_integers(3, 3) == []

def test_edge_case_zero():
    """Tests the edge case where the range includes zero."""
    assert generate_integers(0, 4) == [0, 2, 4]

def test_large_numbers():
    """Tests a range with large numbers in ascending order."""
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_large_numbers_descending():
    """Tests a range with large numbers in descending order."""
    assert generate_integers(110, 100) == [100, 102, 104, 106, 108, 110]

def test_negative_input():
    """Tests negative input, expecting a TypeError."""
    with pytest.raises(TypeError):
        generate_integers(-2, 8)
    with pytest.raises(TypeError):
        generate_integers(2, -8)
    with pytest.raises(TypeError):
        generate_integers(-2, -8)

def test_a_greater_than_b():
    """Tests the scenario where a is greater than b."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_a_is_even_b_is_odd():
    """Tests the scenario where a is even and b is odd."""
    assert generate_integers(2, 5) == [2, 4]

def test_a_is_odd_b_is_even():
    """Tests the scenario where a is odd and b is even."""
    assert generate_integers(3, 6) == [4, 6]
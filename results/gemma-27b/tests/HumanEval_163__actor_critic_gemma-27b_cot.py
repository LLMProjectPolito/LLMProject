
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

def test_generate_integers_ascending_and_descending():
    """Tests both ascending and descending order with positive numbers."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    """Tests when the range contains no even numbers."""
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range_even():
    """Tests a single-digit range with an even number."""
    assert generate_integers(4, 4) == [4]

def test_generate_integers_single_digit_range_odd():
    """Tests a single-digit range with an odd number."""
    assert generate_integers(3, 3) == []

def test_generate_integers_range_12_to_20():
    """Tests a larger range of positive numbers."""
    assert generate_integers(12, 20) == [12, 14, 16, 18, 20]

def test_generate_integers_range_20_to_12():
    """Tests a larger range of positive numbers in descending order."""
    assert generate_integers(20, 12) == [12, 14, 16, 18, 20]

def test_generate_integers_negative_input():
    """Tests with negative and positive inputs."""
    assert generate_integers(-2, 2) == [2]

def test_generate_integers_negative_and_positive():
    """Tests with negative and positive inputs."""
    assert generate_integers(-4, 6) == [2, 4, 6]

def test_generate_integers_zero_input():
    """Tests with zero and positive inputs."""
    assert generate_integers(0, 4) == [2, 4]

def test_generate_integers_zero_and_negative():
    """Tests with zero and negative inputs."""
    assert generate_integers(-2, 0) == []

def test_generate_integers_start_greater_than_end_both_negative():
    """Tests the edge case where start > end and both are negative."""
    assert generate_integers(-4, -8) == []
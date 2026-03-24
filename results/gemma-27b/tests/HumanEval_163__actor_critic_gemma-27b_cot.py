
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

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_negative_inputs():
    assert generate_integers(-2, -8) == []
    assert generate_integers(-8, -2) == []
    assert generate_integers(-2, 2) == [0]

def test_generate_integers_zero_inputs():
    assert generate_integers(0, 2) == [0, 2]
    assert generate_integers(2, 0) == [0, 2]
    assert generate_integers(0, 0) == [0]

def test_generate_integers_larger_range():
    assert generate_integers(12, 20) == [12, 14, 16, 18, 20]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(10, 5) == [6, 8, 10]

def test_generate_integers_single_digit_range():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_no_even_in_range():
    assert generate_integers(11, 13) == []

def test_generate_integers_small_range():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_large_numbers():
    assert generate_integers(98, 102) == [98, 100, 102]

def test_generate_integers_a_is_even_b_is_odd():
    assert generate_integers(2, 5) == [2, 4]

def test_generate_integers_a_is_odd_b_is_even():
    assert generate_integers(1, 4) == [2, 4]

def test_generate_integers_large_numbers_range():
    assert generate_integers(1000, 1010) == [1000, 1002, 1004, 1006, 1008, 1010]

def test_generate_integers_negative_range_with_even():
    assert generate_integers(-4, -2) == [-4, -2]

def test_generate_integers_large_negative_numbers():
    assert generate_integers(-100, -90) == [-100, -98, -96, -94, -92, -90]

def test_generate_integers_a_equals_b_odd():
    assert generate_integers(3, 3) == []
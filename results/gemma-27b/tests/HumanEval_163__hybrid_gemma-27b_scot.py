
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

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result

def test_ascending_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reverse_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(10, 14) == []

def test_single_digit_even():
    assert generate_integers(4, 4) == [4]

def test_single_digit_odd():
    assert generate_integers(3, 3) == []

def test_range_starts_even():
    assert generate_integers(2, 5) == [2, 4]

def test_range_ends_even():
    assert generate_integers(1, 6) == [2, 4, 6]

def test_zero_in_range():
    assert generate_integers(0, 1) == []

def test_large_numbers():
    assert generate_integers(11, 15) == []

def test_range_with_zero_and_even():
    assert generate_integers(0, 2) == [2]

def test_range_with_negative_numbers():
    assert generate_integers(-2, 2) == [2]
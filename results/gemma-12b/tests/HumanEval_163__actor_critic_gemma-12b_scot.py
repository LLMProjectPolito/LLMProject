
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
    if a < 0 or b < 0 or a == 0 or b == 0:
        return []

    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_positive_range_even():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_positive_range_no_even():
    assert generate_integers(10, 14) == []

def test_equal_even():
    assert generate_integers(4, 4) == [4]

def test_equal_odd():
    assert generate_integers(5, 5) == []

def test_zero_input():
    assert generate_integers(0, 5) == []

def test_negative_input():
    assert generate_integers(-1, 5) == []
    assert generate_integers(5, -1) == []
    assert generate_integers(-1, -2) == []

def test_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_single_even_range():
    assert generate_integers(2, 3) == [2]

def test_negative_zero_input():
    assert generate_integers(-1, 0) == []

def test_equal_even_equal():
    assert generate_integers(2, 2) == [2]

def test_equal_odd_equal():
    assert generate_integers(1, 1) == []
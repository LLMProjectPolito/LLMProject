
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for i in range(a, b + 1):
        s = str(i)
        if all(int(digit) % 2 == 0 for digit in s):
            result.append(i)
    return result

import pytest

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_multiple_even():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_start_and_end_same():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_large_range():
    assert generate_integers(100, 108) == [100, 102, 104, 106, 108]

def test_generate_integers_negative_range():
    assert generate_integers(-2, 2) == [-2, 0, 2]

def test_generate_integers_zero_range():
    assert generate_integers(0, 0) == [0]

def test_generate_integers_mixed_range():
    assert generate_integers(1, 5) == [2, 4]
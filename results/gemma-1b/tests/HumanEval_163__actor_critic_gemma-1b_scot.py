
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
    s = set()
    for i in range(a, b + 1):
        for digit in str(i):
            digit = int(digit)
            if digit % 2 == 0:
                s.add(digit)
    return sorted(list(s))

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == []
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 3) == []

def test_generate_integers_all_even():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_with_zeros():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_large_numbers():
    assert generate_integers(100, 100) == [2, 4, 6, 8]
    assert generate_integers(100, 101) == [2, 4, 6, 8]
    assert generate_integers(101, 100) == []

def test_generate_integers_edge_cases():
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 1) == []
    assert generate_integers(1, 3) == [2]
    assert generate_integers(3, 1) == []
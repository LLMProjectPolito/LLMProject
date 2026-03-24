
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
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

def test_edge_case():
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(5, 5) == []
    assert generate_integers(7, 7) == []

def test_consecutive_even():
    assert generate_integers(2, 3) == [2]

def test_range_with_even_digits():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_range_with_no_even_digits():
    assert generate_integers(10, 14) == []

def test_reverse_range_with_even_digits():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_single_digit_odd():
    assert generate_integers(1, 1) == []
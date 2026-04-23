
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
                result.append(int(digit))
    return sorted(list(set(result)))

def test_edge_case():
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(5, 5) == []
    assert generate_integers(7, 7) == []

def test_consecutive_even():
    assert generate_integers(2, 3) == []

def test_basic_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reverse_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(1, 3) == []

def test_mixed_range():
    assert generate_integers(10, 14) == []

def test_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_larger_range():
    assert generate_integers(100, 110) == [0, 2, 4, 6, 8, 10]
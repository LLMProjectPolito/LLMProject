
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
    digits = []
    for i in range(min(a, b), max(a, b) + 1):
        for digit in str(i):
            digit = int(digit)
            if digit % 2 == 0:
                digits.append(digit)
    return sorted(list(set(digits)))

def test_no_even_digits_in_range():
    assert generate_integers(11, 13) == []

def test_even_digits_in_even_numbers():
    assert generate_integers(22, 28) == [2, 8]

def test_basic_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_range_with_no_even_digits():
    assert generate_integers(10, 14) == []
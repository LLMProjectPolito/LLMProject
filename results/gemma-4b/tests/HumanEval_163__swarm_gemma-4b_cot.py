
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
    if a <= b:
        for i in range(a, b + 1):
            s = str(i)
            for digit in s:
                if int(digit) % 2 == 0:
                    if int(digit) not in result:
                        result.append(int(digit))
        result.sort()
    else:
        for i in range(a, b - 1, -1):
            s = str(i)
            for digit in s:
                if int(digit) % 2 == 0:
                    if int(digit) not in result:
                        result.append(int(digit))
        result.sort()
    return result

def test_generate_integers_same_start_end():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_mixed_digits():
    assert generate_integers(123, 456) == [2, 4, 6]
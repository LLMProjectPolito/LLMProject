
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
    
    even_numbers = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


def test_basic_even_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reverse_order_even():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_equal_even():
    assert generate_integers(10, 10) == [10]

def test_a_greater_than_b_odd():
    assert generate_integers(9, 5) == []

def test_a_less_than_b_odd():
    assert generate_integers(5, 9) == [6, 8]

def test_a_zero_b_positive():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_b_zero_a_positive():
    assert generate_integers(5, 0) == [0, 2, 4]

def test_a_b_zero():
    assert generate_integers(0, 0) == [0]

def test_large_a_small_b():
    assert generate_integers(10**9, 1) == [2, 4, 6, 8]

def test_large_even_range():
    assert generate_integers(10**9, 10**9) == [10**9, 10**9 + 2, 10**9 + 4, 10**9 + 6, 10**9 + 8]

def test_no_even_numbers():
    assert generate_integers(1, 3) == []
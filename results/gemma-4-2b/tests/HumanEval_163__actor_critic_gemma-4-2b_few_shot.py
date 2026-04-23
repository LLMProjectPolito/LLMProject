
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
    if a > b:
        a, b = b, a

    even_digits = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits

import pytest

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_single_number():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(2, 1) == []
    assert generate_integers(8, 8) == [8]

def test_generate_integers_large_range():
    assert generate_integers(1, 100) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

def test_generate_integers_a_equals_b():
    assert generate_integers(5, 5) == [5]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(10, 2) == [10]

def test_generate_integers_a_and_b_same_even_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_and_b_different_even_numbers():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_a_and_b_with_no_even_numbers():
    assert generate_integers(1, 3) == []

def test_generate_integers_a_greater_than_b_correct_range():
    assert generate_integers(10, 2) == [10]

def test_generate_integers_a_and_b_with_no_even_numbers_explicit():
    assert generate_integers(1, 3) == []  # Explicitly stating no even numbers exist

def test_generate_integers_a_and_b_with_no_even_numbers_large_range():
    assert generate_integers(1, 3) == []
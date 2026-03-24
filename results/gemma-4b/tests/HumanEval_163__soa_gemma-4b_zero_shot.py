
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
    result = []
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

def test_generate_integers_normal():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_number():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(5, 1) == [1]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 28) == [2, 4, 6, 8]

def test_generate_integers_with_larger_numbers():
    assert generate_integers(100, 108) == [0, 2, 4, 6, 8]

def test_generate_integers_no_even_digits_in_range():
    assert generate_integers(1, 3) == []

def test_generate_integers_with_duplicate_even_digits():
    assert generate_integers(22, 28) == [2, 4, 6, 8]

def test_generate_integers_a_equals_b():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_and_b_are_same_even_number():
    assert generate_integers(6, 6) == [6]

def test_generate_integers_large_range():
    assert generate_integers(1000, 1010) == [0, 2, 4, 6, 8]
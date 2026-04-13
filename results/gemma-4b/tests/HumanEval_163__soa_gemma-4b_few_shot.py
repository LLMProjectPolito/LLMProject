
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

def test_generate_integers_a_equals_b():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_larger_range():
    assert generate_integers(10, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 24) == [2, 4]

def test_generate_integers_with_mixed_digits():
    assert generate_integers(12, 18) == [2, 4, 6, 8]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(10, 5) == [10, 12, 14, 16, 18]

def test_generate_integers_a_and_b_same_digit():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_a_and_b_different_digits():
    assert generate_integers(12, 14) == []

def test_generate_integers_large_numbers():
    assert generate_integers(100, 104) == [100, 102, 104]
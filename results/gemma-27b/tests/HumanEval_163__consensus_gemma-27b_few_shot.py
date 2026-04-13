
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
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0 and i < 10:
            result.append(i)
    return result

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_start_odd():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_end_odd():
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_large_range():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_empty_range():
    assert generate_integers(10, 9) == []

def test_generate_integers_zero_to_one():
    assert generate_integers(0, 1) == []

def test_generate_integers_single_even_digit():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_odd_digit():
    assert generate_integers(1, 1) == []

def test_generate_integers_mixed_digits():
    assert generate_integers(1, 6) == [2, 4, 6]

def test_generate_integers_same_numbers():
    assert generate_integers(5, 5) == []

def test_generate_integers_zero_to_two():
    assert generate_integers(0, 2) == [2]

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, -1) == []

def test_generate_integers_negative_and_positive():
    assert generate_integers(-1, 2) == [2]

def test_generate_integers_empty_range_2():
    assert generate_integers(15, 16) == []

def test_generate_integers_mixed_numbers():
    assert generate_integers(-1, 5) == [2, 4]

def test_generate_integers_zero_range():
    assert generate_integers(0, 0) == [0]

def test_generate_integers_one_to_zero():
    assert generate_integers(1, 0) == [0]
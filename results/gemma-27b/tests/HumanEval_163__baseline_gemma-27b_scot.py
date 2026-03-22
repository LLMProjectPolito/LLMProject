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

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even_digit():
    assert generate_integers(11, 12) == [2]

def test_generate_integers_same_numbers_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_numbers_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_edge_case_small_range():
    assert generate_integers(1, 2) == [2]

def test_generate_integers_edge_case_larger_range():
    assert generate_integers(123, 128) == [2, 4, 6, 8]

def test_generate_integers_negative_input():
    assert generate_integers(-2, -8) == [2, 4, 6, 8]

def test_generate_integers_mixed_range():
    assert generate_integers(13, 17) == [4, 6]

def test_generate_integers_range_with_zero():
    assert generate_integers(0, 5) == [0, 2, 4]
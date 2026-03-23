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
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]

def test_generate_integers_range_with_one_even():
    assert generate_integers(1, 3) == [2]
    assert generate_integers(3, 5) == [4]

def test_generate_integers_larger_range():
    assert generate_integers(1, 10) == [2, 4, 6, 8]

def test_generate_integers_start_at_even():
    assert generate_integers(4, 7) == [4, 6]

def test_generate_integers_end_at_even():
    assert generate_integers(1, 6) == [2, 4, 6]

def test_generate_integers_negative_inputs():
    assert generate_integers(-2, -1) == []
    assert generate_integers(-5, 5) == [2, 4]

def test_generate_integers_zero_inputs():
    assert generate_integers(0, 0) == []
    assert generate_integers(0, 2) == [2]
    assert generate_integers(2, 0) == [2]

def test_generate_integers_large_numbers():
    assert generate_integers(100, 102) == []
    assert generate_integers(101, 103) == []
    assert generate_integers(100, 108) == [2, 4, 6, 8]
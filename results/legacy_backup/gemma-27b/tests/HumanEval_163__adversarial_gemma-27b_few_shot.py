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

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_evens():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_single_odd():
    assert generate_integers(1, 3) == []

def test_generate_integers_same_number_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_number_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_start_at_zero():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_generate_integers_end_at_nine():
    assert generate_integers(5, 9) == [6, 8]

def test_generate_integers_large_range_no_evens():
    assert generate_integers(11, 15) == []

def test_generate_integers_large_range_with_evens():
    assert generate_integers(10, 18) == []

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, 2) == [] # Should only handle positive integers

def test_generate_integers_mixed_positive_negative():
    assert generate_integers(-1, 5) == [0, 2, 4]
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
    assert generate_integers(1, 3) == [2]
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even_digit():
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == [2]

def test_generate_integers_same_numbers():
    assert generate_integers(4, 4) == [4]
    assert generate_integers(5, 5) == []

def test_generate_integers_range_with_tens():
    assert generate_integers(10, 12) == []
    assert generate_integers(11, 13) == []

def test_generate_integers_edge_case_zero():
    assert generate_integers(0, 1) == [0]
    assert generate_integers(0, 2) == [0, 2]

def test_generate_integers_large_range():
    assert generate_integers(1, 9) == [2, 4, 6, 8]
    assert generate_integers(1, 10) == [2, 4, 6, 8]
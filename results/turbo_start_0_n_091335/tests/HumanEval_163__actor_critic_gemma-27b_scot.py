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
        s = str(i)
        for digit in s:
            digit = int(digit)
            if digit % 2 == 0:
                result.append(digit)
    return sorted(list(set(result)))


def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(11, 13) == []

def test_generate_integers_equal_inputs():
    assert generate_integers(5, 5) == []
    assert generate_integers(0, 0) == [0]
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_multi_digit():
    assert generate_integers(20, 25) == [0, 2, 4]

def test_generate_integers_boundary_case():
    assert generate_integers(10, 14) == [0, 2, 4]

def test_generate_integers_large_numbers():
    assert generate_integers(123, 126) == [2, 4, 6]

def test_generate_integers_with_zero():
    assert generate_integers(0, 2) == [0, 2]

def test_generate_integers_same_even_digit():
    assert generate_integers(22, 24) == [2, 4]

def test_generate_integers_large_range():
    assert generate_integers(100, 110) == [0, 2, 4, 6, 8]

def test_generate_integers_zero_only():
    assert generate_integers(0, 0) == [0]
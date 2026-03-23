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
    digits = set()
    for i in range(min(a, b), max(a, b) + 1):
        for digit in str(i):
            digit = int(digit)
            if digit % 2 == 0:
                digits.add(digit)
    return sorted(list(digits))


def test_basic_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reversed_input():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(10, 14) == []

def test_single_number():
    assert generate_integers(2, 2) == [2]

def test_larger_range():
    assert generate_integers(1, 15) == [0, 2, 4, 6, 8]

def test_range_with_zero():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_adjacent_numbers():
    assert generate_integers(2, 3) == [2]

def test_numbers_with_repeated_digits():
    assert generate_integers(22, 24) == [2, 4]

def test_large_numbers():
    assert generate_integers(1234, 1236) == [2, 4, 6]

def test_another_large_range():
    assert generate_integers(1998, 2002) == [0, 2, 8]
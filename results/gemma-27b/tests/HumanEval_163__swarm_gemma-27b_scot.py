
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
        for digit in str(i):
            digit = int(digit)
            if digit % 2 == 0:
                result.append(digit)
    return sorted(list(set(result)))

def test_even_digits_in_even_numbers():
    assert generate_integers(22, 28) == [2, 8]

def test_generate_integers_example_1():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_example_2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_example_3():
    assert generate_integers(10, 14) == []
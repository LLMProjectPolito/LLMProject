
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
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 28) == [2, 4, 6, 8]
    assert generate_integers(10, 12) == []
    assert generate_integers(22, 28) == [2, 4, 6, 8]

def test_generate_integers_with_larger_numbers():
    assert generate_integers(100, 108) == [0, 2, 4, 6, 8]
    assert generate_integers(200, 208) == [0, 2, 4, 6, 8]
    assert generate_integers(1234, 1236) == [2, 4]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []
    assert generate_integers(11, 13) == []

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(8, 8) == [8]
    assert generate_integers(1, 1) == []

def test_generate_integers_negative_input():
    with pytest.raises(Exception):
        generate_integers(-1, 5)
    with pytest.raises(Exception):
        generate_integers(1, -5)
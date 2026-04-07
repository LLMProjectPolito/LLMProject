
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

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(6, 6) == [6]

def test_generate_integers_empty_range():
    assert generate_integers(10, 10) == []
    assert generate_integers(11, 11) == []

def test_generate_integers_with_zero():
    assert generate_integers(0, 2) == [2]
    assert generate_integers(2, 0) == [2]
    assert generate_integers(10, 12) == []

def test_generate_integers_large_numbers():
    assert generate_integers(123456, 123456) == [2, 4, 6]
    assert generate_integers(123456789, 123456789) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []
    assert generate_integers(11, 13) == []

def test_generate_integers_negative_input():
    with pytest.raises(ValueError):
        generate_integers(-1, 5)
    with pytest.raises(ValueError):
        generate_integers(1, -5)
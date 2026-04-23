
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
        if i % 2 == 0:
            result.append(i)
    return result

def test_generate_integers_positive(a, b):
    assert generate_integers(a, b) == list(range(a, b + 1, 2))

def test_generate_integers_reverse(a, b):
    assert generate_integers(b, a) == list(range(a, b + 1, 2))

def test_generate_integers_same_numbers(a, b):
    assert generate_integers(a, b) == list(range(a, b + 1, 2))

def test_generate_integers_no_even_numbers(a, b):
    assert generate_integers(10, 14) == []

def test_generate_integers_a_equals_1(a, b):
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_a_equals_2(a, b):
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_a_equals_3(a, b):
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_a_equals_4(a, b):
    assert generate_integers(4, 8) == [4, 6, 8]

def test_generate_integers_a_equals_5(a, b):
    assert generate_integers(5, 9) == [6, 8]

def test_generate_integers_a_equals_6(a, b):
    assert generate_integers(6, 10) == [6, 8]

def test_generate_integers_a_equals_7(a, b):
    assert generate_integers(7, 11) == [8, 10]

def test_generate_integers_a_equals_8(a, b):
    assert generate_integers(8, 12) == [8, 10, 12]

def test_generate_integers_a_equals_9(a, b):
    assert generate_integers(9, 13) == [10, 12]

def test_generate_integers_a_equals_10(a, b):
    assert generate_integers(10, 15) == [10, 12, 14]

def test_generate_integers_a_equals_11(a, b):
    assert generate_integers(11, 15) == [12, 14]

def test_generate_integers_a_equals_12(a, b):
    assert generate_integers(12, 16) == [12, 14]

def test_generate_integers_a_equals_13(a, b):
    assert generate_integers(13, 17) == [14, 16]

def test_generate_integers_a_equals_14(a, b):
    assert generate_integers(14, 18) == [14, 16]
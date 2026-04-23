
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

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_number():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(5, 1) == [1]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 28) == [2, 4, 6, 8]

def test_generate_integers_large_numbers():
    assert generate_integers(100, 108) == [0, 2, 4, 6, 8]

def test_generate_integers_mixed_numbers():
    assert generate_integers(12, 18) == [2, 4, 6, 8]

def test_generate_integers_edge_case_1():
    assert generate_integers(1, 1) == []

def test_generate_integers_edge_case_2():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_edge_case_3():
    assert generate_integers(3, 2) == [2]

def test_generate_integers_with_duplicates():
    assert generate_integers(22, 28) == [2, 4, 6, 8]

def test_generate_integers_complex_range():
    assert generate_integers(11, 15) == [2, 4]
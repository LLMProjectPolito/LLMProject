
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

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit_range_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_larger_range():
    assert generate_integers(1, 10) == [2, 4, 6, 8]

def test_generate_integers_larger_range_descending():
    assert generate_integers(10, 1) == [2, 4, 6, 8]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(5, 1) == [2, 4]

def test_generate_integers_edge_case_1():
    assert generate_integers(0, 1) == []

def test_generate_integers_edge_case_2():
    assert generate_integers(1, 0) == []

def test_generate_integers_edge_case_3():
    assert generate_integers(1, 2) == [2]

def test_generate_integers_edge_case_4():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_larger_numbers():
    assert generate_integers(20, 28) == [20, 22, 24, 26, 28]

def test_generate_integers_larger_numbers_descending():
    assert generate_integers(28, 20) == [20, 22, 24, 26, 28]
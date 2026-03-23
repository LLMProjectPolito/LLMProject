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

def test_basic_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_basic_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_mixed_even_odd():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_mixed_even_odd_descending():
    assert generate_integers(9, 1) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(1, 3) == []
    assert generate_integers(10, 14) == []

def test_single_even_number():
    assert generate_integers(2, 2) == [2]

def test_same_number_even():
    assert generate_integers(4, 4) == [4]

def test_same_number_odd():
    assert generate_integers(1, 1) == []

def test_edge_case_zero():
    assert generate_integers(0, 4) == [0, 2, 4]

def test_large_numbers():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_large_range():
    assert generate_integers(1, 21) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_edge_case_a_is_even():
    assert generate_integers(4, 6) == [4, 6]

def test_edge_case_b_is_even():
    assert generate_integers(2, 4) == [2, 4]

def test_a_equals_b():
    assert generate_integers(4, 4) == [4]
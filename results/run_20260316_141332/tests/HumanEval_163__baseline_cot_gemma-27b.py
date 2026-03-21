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

def test_basic_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_single_number_range():
    assert generate_integers(4, 4) == [4]

def test_edge_case_small_numbers():
    assert generate_integers(0, 2) == [0, 2]
    assert generate_integers(1, 3) == [2]

def test_edge_case_larger_numbers():
    assert generate_integers(5, 9) == [6, 8]

def test_boundary_condition_just_outside_range():
    assert generate_integers(1, 1) == []
    assert generate_integers(9, 10) == []

def test_empty_range_odd():
    assert generate_integers(11, 11) == []

def test_a_is_zero():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_b_is_zero():
    assert generate_integers(2, 0) == [0, 2, 4]

def test_negative_numbers():
    assert generate_integers(-2, 2) == [0, 2]

def test_large_range():
    assert generate_integers(1, 8) == [2, 4, 6, 8]
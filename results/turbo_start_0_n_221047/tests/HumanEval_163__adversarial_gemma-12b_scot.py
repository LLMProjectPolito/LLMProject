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
    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_ascending_order():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_descending_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_single_even_number():
    assert generate_integers(2, 3) == [2]

def test_multiple_even_numbers():
    assert generate_integers(1, 10) == [2, 4, 6, 8, 10]

def test_inclusive_range():
    assert generate_integers(2, 4) == [2, 4]
    assert generate_integers(4, 2) == [2, 4]

def test_edge_case_a_equals_b_even():
    assert generate_integers(4, 4) == [4]

def test_edge_case_a_equals_b_odd():
    assert generate_integers(5, 5) == []

def test_large_range():
    assert generate_integers(1, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
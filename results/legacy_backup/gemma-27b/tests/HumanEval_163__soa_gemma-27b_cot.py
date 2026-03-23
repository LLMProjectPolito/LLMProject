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

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_odd():
    assert generate_integers(1, 1) == []

def test_generate_integers_range_with_even_and_odd():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_range_with_only_odd():
    assert generate_integers(1, 3) == []

def test_generate_integers_a_equals_b_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_a_equals_b_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_large_range():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_edge_case_1():
    assert generate_integers(0, 1) == []

def test_generate_integers_edge_case_2():
    assert generate_integers(9, 10) == [2, 4, 6, 8]

def test_generate_integers_edge_case_3():
    assert generate_integers(5, 7) == [6]

def test_generate_integers_negative_input_a():
    assert generate_integers(-2, 5) == [2, 4]

def test_generate_integers_negative_input_b():
    assert generate_integers(2, -5) == [2, 4]

def test_generate_integers_both_negative():
    assert generate_integers(-2, -5) == [2, 4]
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
    assert generate_integers(0, 2) == [2]

def test_generate_integers_edge_case_3():
    assert generate_integers(7, 9) == [8]

def test_generate_integers_negative_inputs():
    assert generate_integers(-2, -1) == []

def test_generate_integers_mixed_inputs():
    assert generate_integers(-1, 2) == [2]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(5, 1) == [2, 4]

def test_generate_integers_start_at_zero():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_generate_integers_end_at_zero():
    assert generate_integers(2, 0) == [2, 4]

def test_generate_integers_empty_range():
    assert generate_integers(10, 11) == []

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, 2) == []

def test_generate_integers_mixed_numbers():
    assert generate_integers(-1, 5) == [2, 4]
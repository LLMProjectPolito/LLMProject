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

def test_a_equals_b_even():
    assert generate_integers(4, 4) == [4]

def test_a_equals_b_odd():
    assert generate_integers(3, 3) == []

def test_small_values():
    assert generate_integers(1, 3) == [2]

def test_large_values():
    assert generate_integers(7, 9) == [8]

def test_empty_range():
    assert generate_integers(5, 5) == []

def test_single_even_number():
    assert generate_integers(1, 2) == [2]

def test_range_with_one_even():
    assert generate_integers(1, 4) == [2, 4]

def test_range_starting_with_even():
    assert generate_integers(2, 5) == [2, 4]

def test_range_ending_with_even():
    assert generate_integers(1, 6) == [2, 4, 6]

def test_a_and_b_are_same_and_even():
    assert generate_integers(6, 6) == [6]

def test_a_and_b_are_same_and_odd():
    assert generate_integers(7, 7) == []
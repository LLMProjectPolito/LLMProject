
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

def test_basic_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_single_even_number():
    assert generate_integers(2, 2) == [2]

def test_adjacent_even_numbers():
    assert generate_integers(4, 6) == [4, 6]

def test_start_at_zero():
    assert generate_integers(0, 4) == [0, 2, 4]

def test_end_at_zero():
    assert generate_integers(2, 0) == [0, 2]

def test_large_numbers():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_same_number():
    assert generate_integers(5, 5) == []

def test_negative_input():
    with pytest.raises(TypeError):
        generate_integers(-2, 8)

def test_float_input():
    with pytest.raises(TypeError):
        generate_integers(2.0, 8)

def test_string_input():
    with pytest.raises(TypeError):
        generate_integers("2", "8")

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
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")

    if a > b:
        a, b = b, a

    result = []
    for i in range(a, b + 1):
        if i % 2 == 0 and 0 <= i <= 9:
            result.append(i)
    return result

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_start_odd():
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_end_odd():
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_large_range():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_edge_case_1():
    assert generate_integers(0, 1) == []

def test_generate_integers_zero_range():
    assert generate_integers(0, 0) == []

def test_generate_integers_large_range_2():
    assert generate_integers(1, 10) == [2, 4, 6, 8]

def test_generate_integers_large_range_3():
    assert generate_integers(15, 20) == [16, 18, 20]

def test_generate_integers_negative_input():
    with pytest.raises(ValueError):
        generate_integers(-1, 5)

def test_generate_integers_negative_range():
    with pytest.raises(ValueError):
        generate_integers(-5, -1)

def test_generate_integers_mixed_range():
    with pytest.raises(ValueError):
        generate_integers(-2, 2)

def test_generate_integers_type_error():
    with pytest.raises(TypeError):
        generate_integers(2.5, 5)
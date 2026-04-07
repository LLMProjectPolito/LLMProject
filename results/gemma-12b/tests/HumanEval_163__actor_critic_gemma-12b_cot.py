
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
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")

    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_adjacent_even():
    assert generate_integers(4, 6) == [4, 6]

def test_generate_integers_zero_input():
    with pytest.raises(ValueError):
        generate_integers(0, 4)
    with pytest.raises(ValueError):
        generate_integers(2, 0)
    with pytest.raises(ValueError):
        generate_integers(0, 0)

def test_generate_integers_a_equals_b_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_non_integer_input():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)
    with pytest.raises(TypeError):
        generate_integers(2, 8.5)
    with pytest.raises(TypeError):
        generate_integers(2, 8)
    with pytest.raises(TypeError):
        generate_integers("2", 8)
    with pytest.raises(TypeError):
        generate_integers(2, "8")
    with pytest.raises(TypeError):
        generate_integers("2", "8")

def test_generate_integers_large_range():
    expected_output = [i for i in range(2, 101, 2)]
    assert generate_integers(1, 100) == expected_output

def test_generate_integers_same_number_odd():
    assert generate_integers(5, 5) == []
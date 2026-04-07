
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
    if a < 0 or b < 0:
        raise TypeError("Inputs must be non-negative.")

    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_start_with_odd():
    assert generate_integers(3, 6) == [4, 6]

def test_generate_integers_end_with_odd():
    assert generate_integers(4, 7) == [4, 6]

def test_generate_integers_large_range():
    assert generate_integers(1, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_negative_input():
    with pytest.raises(TypeError):
        generate_integers(-2, 8)

def test_generate_integers_non_integer_input():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)

def test_generate_integers_string_input():
    with pytest.raises(TypeError):
        generate_integers("2", "8")
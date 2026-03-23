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
        raise TypeError("Inputs must be integers")

    if a <= 0 or b <= 0:
        return []

    if a > b:
        a, b = b, a

    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result


def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_empty_range():
    assert generate_integers(10, 14) == []

def test_generate_integers_equal_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_equal_odd():
    assert generate_integers(5, 5) == []

def test_generate_integers_negative_range():
    assert generate_integers(-4, 2) == []

def test_generate_integers_zero_a():
    assert generate_integers(0, 8) == []

def test_generate_integers_zero_b():
    assert generate_integers(2, 0) == []

def test_generate_integers_non_integer_a():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)

def test_generate_integers_non_integer_b():
    with pytest.raises(TypeError):
        generate_integers(2, 8.5)

def test_generate_integers_both_non_integer():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8.5)
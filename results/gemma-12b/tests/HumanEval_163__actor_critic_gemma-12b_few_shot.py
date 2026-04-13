
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
    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    return result

### Tests (Pytest):
def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(1, 3) == []

def test_generate_integers_equal():
    assert generate_integers(5, 5) == []

def test_generate_integers_negative_a():
    assert generate_integers(-2, 8) == []

def test_generate_integers_negative_b():
    assert generate_integers(2, -8) == []

def test_generate_integers_zero_a():
    assert generate_integers(0, 8) == [0, 2, 4, 6, 8]

def test_generate_integers_zero_b():
    assert generate_integers(2, 0) == []

def test_generate_integers_non_integer_a():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)

def test_generate_integers_non_integer_b():
    with pytest.raises(TypeError):
        generate_integers(2, 8.5)
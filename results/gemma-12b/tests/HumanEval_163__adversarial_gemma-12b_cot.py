
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

def test_example_cases():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_single_even_number():
    assert generate_integers(3, 5) == []
    assert generate_integers(2, 2) == [2]

def test_edge_cases():
    assert generate_integers(2, 4) == [2, 4]
    assert generate_integers(1, 3) == [2]
    assert generate_integers(4, 6) == [4, 6]

def test_empty_range():
    assert generate_integers(1, 2) == [2]
    assert generate_integers(3, 4) == [4]

def test_large_numbers():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]
    assert generate_integers(1000, 1010) == [1000, 1002, 1004, 1006, 1008, 1010]

def test_duplicate_even_numbers():
    assert generate_integers(2, 6) == [2, 4, 6]
    assert generate_integers(4, 8) == [4, 6, 8]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        generate_integers("a", 5)
    with pytest.raises(TypeError):
        generate_integers(2, "b")
    with pytest.raises(TypeError):
        generate_integers(2.5, 5)
    with pytest.raises(TypeError):
        generate_integers(2, 5.5)

def test_invalid_input_value():
    with pytest.raises(ValueError):
        generate_integers(-2, 5)
    with pytest.raises(ValueError):
        generate_integers(2, -5)
    with pytest.raises(ValueError):
        generate_integers(-2, -5)
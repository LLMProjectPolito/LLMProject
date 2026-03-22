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
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")

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
    assert generate_integers(1, 3) == [2]

def test_same_even_number():
    assert generate_integers(4, 4) == [4]

def test_negative_input():
    with pytest.raises(ValueError):
        generate_integers(-2, 8)
    with pytest.raises(ValueError):
        generate_integers(2, -8)
    with pytest.raises(ValueError):
        generate_integers(-2, -8)

def test_zero_input():
    assert generate_integers(0, 4) == [0, 2, 4]
    assert generate_integers(4, 0) == [0, 2, 4]
    assert generate_integers(0, 0) == [0]

def test_non_integer_input():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)
    with pytest.raises(TypeError):
        generate_integers(2, 8.5)
    with pytest.raises(TypeError):
        generate_integers("2", 8)
    with pytest.raises(TypeError):
        generate_integers(2, "8")

def test_large_numbers():
    assert generate_integers(1000, 1010) == [1000, 1002, 1004, 1006, 1008, 1010]
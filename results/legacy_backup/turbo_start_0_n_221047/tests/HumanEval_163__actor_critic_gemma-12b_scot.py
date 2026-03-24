import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []

    Raises:
        TypeError: If a or b are not integers.
        ValueError: If a or b are not positive integers.
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

def test_valid_input():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_even_range():
    assert generate_integers(4, 10) == [4, 6, 8, 10]

def test_equal_even():
    assert generate_integers(4, 4) == [4]

def test_equal_odd():
    assert generate_integers(3, 3) == []

def test_single_even():
    assert generate_integers(1, 2) == [2]

def test_small_range_with_even():
    assert generate_integers(1, 3) == [2]

def test_large_range_with_evens():
    assert generate_integers(1, 100) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

def test_large_numbers():
    assert generate_integers(1000000, 1000010) == [1000000, 1000002, 1000004, 1000006, 1000008, 1000010]

def test_non_integer_inputs():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)

def test_negative_inputs():
    with pytest.raises(ValueError):
        generate_integers(-2, 8)

def test_zero_input():
    with pytest.raises(ValueError):
        generate_integers(0, 2)

def test_mixed_positive_negative():
    with pytest.raises(ValueError):
        generate_integers(-2, 8)
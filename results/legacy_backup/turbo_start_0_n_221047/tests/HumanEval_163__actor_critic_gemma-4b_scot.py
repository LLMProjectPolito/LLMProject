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
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

def get_expected_even_digits(a, b):
    """Helper function to generate a list of expected even digits."""
    expected = []
    for i in range(a, b + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                expected.append(int(digit))
    expected.sort()
    return expected

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(1, 3) == []

def test_generate_integers_single_digit():
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(1, 1) == []

def test_generate_integers_a_equals_b():
    assert generate_integers(5, 5) == [5]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(10, 2) == [2, 4, 6, 8]

def test_generate_integers_multi_digit():
    assert generate_integers(10, 14) == []
    assert generate_integers(20, 25) == [2, 4]
    assert generate_integers(123, 126) == [2, 4, 6]
    assert generate_integers(2468, 2468) == [2, 4, 6, 8]

def test_generate_integers_empty_range():
    assert generate_integers(1, 1) == []

def test_generate_integers_large_numbers():
    assert generate_integers(100000, 100002) == [0, 2, 4, 6, 8]

def test_generate_integers_negative_input():
    # Assuming the function should handle negative input gracefully,
    # either by raising an error or returning an empty list.
    # This test checks for the empty list behavior.
    assert generate_integers(-1, 1) == []
    assert generate_integers(-10, -5) == []
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
    for i in range(min(a, b), max(a, b) + 1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

def test_generate_integers_normal():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_same_numbers():
    assert generate_integers(5, 5) == []

def test_generate_integers_larger_range():
    assert generate_integers(10, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_with_zero():
    assert generate_integers(0, 10) == [0, 2, 4, 6, 8, 10]

def test_generate_integers_negative_a():
    assert generate_integers(-2, 2) == [2]

def test_generate_integers_negative_b():
    assert generate_integers(2, -2) == [2]

def test_generate_integers_both_negative():
    assert generate_integers(-2, -2) == []

def test_generate_integers_a_greater_than_b():
    assert generate_integers(10, 5) == [10]
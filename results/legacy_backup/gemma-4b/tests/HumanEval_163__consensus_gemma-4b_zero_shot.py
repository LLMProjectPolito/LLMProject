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

def test_generate_integers_empty():
    assert generate_integers(1, 1) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_odd():
    assert generate_integers(1, 1) == []

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_mixed():
    assert generate_integers(10, 14) == []

def test_generate_integers_with_zeros():
    assert generate_integers(20, 28) == [2, 4, 6, 8]

def test_generate_integers_with_multiple_even_digits():
    assert generate_integers(12, 18) == [2, 4, 6, 8]

def test_generate_integers_large_range():
    assert generate_integers(100, 108) == [0, 2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 3) == []

def test_generate_integers_start_and_end_same():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_negative_range():
    assert generate_integers(-2, 2) == [2]

def test_generate_integers_negative_and_positive():
    assert generate_integers(-2, 2) == [2]

def test_generate_integers_complex_range():
    assert generate_integers(11, 15) == []

def test_generate_integers_with_duplicate_even_digits():
    assert generate_integers(22, 28) == [2, 4, 6, 8]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_with_leading_zeros():
    assert generate_integers(200, 208) == [0, 2, 4, 6, 8]
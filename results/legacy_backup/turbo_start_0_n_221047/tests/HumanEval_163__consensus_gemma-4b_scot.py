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

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_start_and_end():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_larger_range():
    assert generate_integers(10, 20) == [10, 12, 14, 16, 18, 20]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 24) == [2, 4, 20, 22, 24]

def test_generate_integers_negative_range():
    assert generate_integers(-2, 2) == [2]

def test_generate_integers_large_numbers():
    assert generate_integers(1234, 1236) == [2, 4, 6]

def test_generate_integers_with_duplicates():
    assert generate_integers(2, 6) == [2, 4, 6]
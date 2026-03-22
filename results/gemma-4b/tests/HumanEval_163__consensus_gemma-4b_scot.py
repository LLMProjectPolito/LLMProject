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

def test_generate_integers_a_less_than_b():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(1, 9) == []

def test_generate_integers_a_equals_b():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_consecutive():
    assert generate_integers(2, 4) == [2, 4]

def test_generate_integers_far_apart():
    assert generate_integers(10, 14) == []

def test_generate_integers_mixed_even_digits():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_with_duplicates():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_generate_integers_large_numbers():
    assert generate_integers(1234, 1236) == [2, 4, 6]

def test_generate_integers_zero_start():
    assert generate_integers(20, 28) == [2, 4, 6, 8]
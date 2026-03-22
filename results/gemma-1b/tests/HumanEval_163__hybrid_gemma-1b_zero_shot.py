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
    for num in range(a, b + 1):
        for digit in str(num):
            if int(digit) % 2 == 0:
                result.append(num)
                break
    return result

def test_generate_integers_example1():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_example2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_example3():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit():
    assert generate_integers(5, 5) == []

def test_generate_integers_zero():
    assert generate_integers(0, 0) == []

def test_generate_integers_large_numbers():
    assert generate_integers(100, 100) == [0, 2, 4, 6, 8, 0, 2, 4, 6, 8]

def test_generate_integers_2_8():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_8_2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_10_14():
    assert generate_integers(10, 14) == []

def test_generate_integers_1_2():
    assert generate_integers(1, 2) == [2]

def test_generate_integers_2_1():
    assert generate_integers(2, 1) == [2]

def test_generate_integers_1_3():
    assert generate_integers(1, 3) == [2]

def test_generate_integers_3_2():
    assert generate_integers(3, 2) == [2]

def test_generate_integers_2_3():
    assert generate_integers(2, 3) == [2]
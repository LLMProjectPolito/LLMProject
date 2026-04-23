
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

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_number():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_a_equals_b():
    assert generate_integers(5, 5) == [5]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(14, 10) == [10, 12, 14]

def test_generate_integers_large_numbers():
    assert generate_integers(100, 200) == [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]

def test_generate_integers_a_equals_1():
    assert generate_integers(1, 10) == [2, 4, 6, 8]

def test_generate_integers_a_equals_2():
    assert generate_integers(2, 10) == [2, 4, 6, 8]

def test_generate_integers_a_equals_3():
    assert generate_integers(3, 10) == [4, 6, 8]

def test_generate_integers_a_equals_4():
    assert generate_integers(4, 10) == [4, 6, 8]

def test_generate_integers_a_equals_5():
    assert generate_integers(5, 10) == [6, 8]

def test_generate_integers_a_equals_6():
    assert generate_integers(6, 10) == [6, 8]

def test_generate_integers_a_equals_7():
    assert generate_integers(7, 10) == [8]

def test_generate_integers_a_equals_8():
    assert generate_integers(8, 10) == [8]
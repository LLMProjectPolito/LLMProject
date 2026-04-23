
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
    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
    return result

@pytest.fixture(name="generate_integers")
def test_generate_integers():
    yield generate_integers

def test_generate_integers_example_1():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_example_2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_example_3():
    assert generate_integers(10, 14) == []

def test_generate_integers_same_numbers():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_large_range():
    assert generate_integers(20, 30) == [20, 22, 24, 26, 28, 30]

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, 8) == [2, 4, 6, 8]

def test_generate_integers_mixed_numbers():
    assert generate_integers(-4, 6) == [2, 4, 6]

def test_generate_integers_one_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_empty_range():
    assert generate_integers(10, 10) == []
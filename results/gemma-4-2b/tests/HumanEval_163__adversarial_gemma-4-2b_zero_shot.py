
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
    even_numbers = []
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

@pytest.mark.parametrize("a, b, expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    (1, 1, []),
    (2, 2, [2]),
    (1, 2, [2]),
    (2, 1, [2]),
    (100, 105, [100, 102, 104]),
    (105, 100, [100, 102, 104]),
    (1000, 1005, [1000, 1002, 1004]),
    (1005, 1000, [1000, 1002, 1004]),
    (1, 100, [2, 4, 6, 8]),
    (100, 1, [2, 4, 6, 8]),
    (10, 20, [10, 12, 14, 16, 18, 20]),
    (20, 10, [10, 12, 14, 16, 18, 20]),
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 3),
    (3, 1),
    (2, 4),
    (4, 2),
    (5, 7),
    (7, 5),
    (1, 5),
    (5, 1),
])
def test_generate_integers_small_range(a, b, expected):
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1000, 1001),
    (1001, 1000),
    (1000, 1000),
    (1000, 10000),
    (10000, 1000),
])
def test_generate_integers_large_range(a, b, expected):
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (0, 1),
    (1, 0),
])
def test_generate_integers_zero_boundary(a, b, expected):
    assert generate_integers(a, b) == expected
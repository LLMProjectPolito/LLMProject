
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
    even_numbers = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 8, [2, 4, 6, 8]),
        (8, 2, [2, 4, 6, 8]),
        (10, 14, []),
        (1, 5, [2, 4]),
        (2, 2, [2]),
        (1, 1, []),
        (1, 2, [2]),
        (2, 1, [2]),
        (100, 105, [100, 102, 104]),
        (105, 100, [100, 102, 104]),
        (1, 100, [2, 4, 6, 8, 100]),
        (100, 1, [2, 4, 6, 8, 100]),
        (20, 30, [20, 22, 24, 26, 28, 30]),
        (30, 20, [20, 22, 24, 26, 28, 30]),
    ],
)
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 8, [2, 4, 6, 8]), #Test with 0 as input
        (2, 0, [2, 4, 6, 8]), #Test with 0 as input
        (0, 0, []), #Test with 0 as input
    ],
)
def test_generate_integers_zero(a, b, expected):
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (-2, 8, [2, 4, 6, 8]), #Test with negative input
        (8, -2, [2, 4, 6, 8]), #Test with negative input
        (-2, -8, []), #Test with negative input
    ],
)
def test_generate_integers_negative(a, b, expected):
    assert generate_integers(a, b) == expected
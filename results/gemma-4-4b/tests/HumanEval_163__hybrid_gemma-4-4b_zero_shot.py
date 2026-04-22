
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
        (5, 10, [6, 8]),
        (100, 105, [100, 102, 104]),
        (100, 100, [100]),
        (1, 100, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]),
        (100, 1, [2, 4, 6, 8]),
        (20, 40, [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]),
    ],
)
def test_generate_integers_basic(a, b, expected):
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1000, 1005, [1000, 1002, 1004]),
        (1000, 1000, [1000]),
    ],
)
def test_generate_integers_large_numbers(a, b, expected):
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (100, 200, [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]),
    ],
)
def test_generate_integers_mid_range(a, b, expected):
    assert generate_integers(a, b) == expected
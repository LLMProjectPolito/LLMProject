import pytest
from your_module import order_by_points  # Replace your_module

def digit_sum(n):
    """Helper function to calculate the sum of digits of an integer."""
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
    ([1, -2, 3, -4, 5], [1, -2, 3, -4, 5]),
    ([11, 2, 1, 22], [1, 2, 11, 22]),
    ([0], [0]),
    ([123, 45, 6], [6, 45, 123]),
    ([10, 1, 100], [1, 10, 100]),
    ([5, 5, 5], [5, 5, 5]),
    ([1, 10, 100, 1000], [1, 10, 100, 1000]),
    ([-1, -10, -100], [-1, -10, -100]),
    ([1, -1, 10, -10], [1, -1, 10, -10]),
    ([12, 11, 21], [11, 12, 21]),
    ([1000, 100, 10, 1], [1, 10, 100, 1000]),
    ([1111, 111, 11, 1], [1, 11, 111, 1111]),
    ([1111, 111, 11, 1], [1, 11, 111, 1111])
])
def test_order_by_points(nums, expected):
    """Tests the order_by_points function with various scenarios,
    including empty lists, positive and negative numbers, and different digit sums.
    """
    assert order_by_points(nums) == expected
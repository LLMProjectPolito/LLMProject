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
    ([5], [5]),
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([12, 1, 11, 2], [1, 11, 12, 2]),
    ([10, 2, 3, 4], [10, 2, 3, 4]),
    ([-1, -2, -3], [-1, -2, -3]),
    ([0, 1, -1], [0, 1, -1]),
    ([123, 45, 6], [6, 45, 123]),
    ([1000, 1, 10], [1, 10, 1000]),
    ([11, 2, 3, 4, 5], [2, 3, 4, 5, 11]),
    ([22, 2, 222], [2, 22, 222]),
    ([12345, 6789, 1], [1, 12345, 6789]),
    ([0, 10, 1], [0, 1, 10]),
    ([100, 0, 1], [0, 1, 100]),
    ([-999], [-999]),
    ([1, -10, 2, -20, 3], [1, 3, -10, 2, -20]),
    ([-1, -2], [-1, -2]),
    ([1, 10, 100], [1, 10, 100]),
    ([1000000000, 1], [1, 1000000000]),
    ([0, -0, 1, -1], [0, -0, 1, -1])
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected
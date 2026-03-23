import pytest
from your_module import order_by_points  # Replace your_module

def digit_sum(n):
    """Helper function to calculate the sum of digits of an integer."""
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    if n < 0:
        return -s
    return s

@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
    ([1, -2, 3, -4, 5], [1, -2, 3, -4, 5]),
    ([11, 2, 1, 22], [1, 2, 11, 22]),
    ([5, 55, 555], [5, 55, 555]),
    ([10, 1, 100], [1, 10, 100]),
    ([0], [0]),
    ([1, 1, 1], [1, 1, 1]),
    ([123, 45, 678, 9], [9, 45, 123, 678]),
    ([-123, -45, -678, -9], [-9, -45, -123, -678]),
    ([12, -12, 21], [12, -12, 21]),
    ([1000, 1, 10], [1, 10, 1000]),
    ([-1000, -1, -10], [-1, -10, -1000])
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected
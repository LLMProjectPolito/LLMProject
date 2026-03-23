import pytest
import math

def double_the_difference(numbers):
    """
    Calculates the difference between the sum of squares of the numbers and the sum of the numbers.
    """
    sum_of_squares = sum(x**2 for x in numbers)
    sum_of_numbers = sum(numbers)
    return sum_of_squares - sum_of_numbers

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 3, 2, 0], 10),
        ([-1, -2, 0], 0),
        ([9, -2], 81),
        ([0], 0),
        ([], 0),
    ],
)
def test_double_the_difference(numbers, expected):
    assert double_the_difference(numbers) == expected
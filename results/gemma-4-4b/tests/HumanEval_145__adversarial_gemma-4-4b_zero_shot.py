
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

import pytest

def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def sum_digits(n):
        s = 0
        n = abs(n)
        while n:
            s += n % 10
            n //= 10
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
        ([], []),
        ([12, 1, 11, 2, 22], [1, 2, 11, 12, 22]),
        ([-1, -10, -100], [-1, -10, -100]),
        ([0, 1, 10, 100], [0, 1, 10, 100]),
        ([10, 1, 100, 1000], [1, 10, 100, 1000]),
        ([-1, 1, -10, 10], [1, -1, 10, -10]),
        ([1, 1, 1], [1, 1, 1]),
        ([-1, -1, -1], [-1, -1, -1]),
        ([1, -1], [1, -1]),
        ([-1, 1], [1, -1]),
        ([10, 2], [2, 10]),
        ([2, 10], [2, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 10, 100, 1000, 10000], [1, 10, 100, 1000, 10000]),
        ([-10000, -1000, -100, -10, -1], [-1, -10, -100, -1000, -10000]),
    ],
)
def test_order_by_points(input_list, expected_output):
    assert order_by_points(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list",
    [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [-1, -2, -3],
        [1, -1, 2, -2],
    ],
)
def test_empty_list(input_list):
    assert order_by_points(input_list) == []

@pytest.mark.parametrize(
    "input_list",
    [
        [1, 11, -1, -11, -12],
        [12, 1, 11, 2, 22],
        [-1, -10, -100],
        [0, 1, 10, 100],
        [10, 1, 100, 1000],
        [-1, 1, -10, 10],
        [1, 1, 1],
        [-1, -1, -1],
        [1, -1],
        [-1, 1],
        [10, 2],
        [2, 10],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [10, 100, 1, 1000],
        [-10000, -1000, -100, -10, -1],
    ],
)
def test_order_by_points_general(input_list):
    assert order_by_points(input_list) == sorted(input_list, key=lambda x: (sum_digits(x), input_list.index(x)))

def test_sum_digits_negative_numbers():
    assert sum_digits(-12) == 3
    assert sum_digits(-100) == 1
    assert sum_digits(-1) == 1
    assert sum_digits(-11) == 2
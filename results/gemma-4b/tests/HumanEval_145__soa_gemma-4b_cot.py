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
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single():
    assert order_by_points([5]) == [5]

def test_order_by_points_simple():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_order_by_points_negative():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_order_by_points_mixed():
    assert order_by_points([-1, 1, -2, 2, -3, 3]) == [-1, 1, -2, 2, -3, 3]

def test_order_by_points_example1():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_example2():
    assert order_by_points([10, 1, 100, 11, 101]) == [1, 10, 100, 101, 11]

def test_order_by_points_duplicate_sums():
    assert order_by_points([1, 10, 100, 11, 110]) == [1, 10, 100, 11, 110]

def test_order_by_points_negative_and_positive():
    assert order_by_points([-1, 1, -11, 11]) == [-1, -11, 1, 11]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 6, 789]) == [6, 45, 123, 789]

def test_order_by_points_zero():
    assert order_by_points([0, 1, 0, 10]) == [0, 0, 1, 10]

def test_order_by_points_negative_zero():
    assert order_by_points([-0, 1, -0, 10]) == [-0, -0, 1, 10]
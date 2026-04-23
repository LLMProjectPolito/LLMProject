
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


@pytest.mark.parametrize("input_list, expected_output", [
    (
        [1, 11, -1, -11, -12],
        [-1, -11, 1, -12, 11],
    ),
    (
        [],
        [],
    ),
    (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ),
    (
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ),
    (
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40, 50],
    ),
    (
        [1, 10, 100, 1000],
        [1, 10, 100, 1000],
    ),
    (
        [-1, -10, -100, -1000],
        [-1, -10, -100, -1000],
    ),
    (
        [11, 22, 33, 44, 55],
        [11, 22, 33, 44, 55],
    ),
    (
        [1, 10, 100, 10, 1000],
        [1, 10, 10, 100, 1000],
    ),
    (
        [0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0],
    ),
    (
        [-1, 0, 1],
        [-1, 0, 1],
    ),
])
def test_order_by_points_parametrized(input_list, expected_output):
    assert order_by_points(input_list) == expected_output

@pytest.mark.parametrize("input_list", [
    [],
    [1],
    [1, 10],
    [1, 10, 100],
    [-1],
    [-1, 1],
    [-1, 10],
])
def test_order_by_points_single_element(input_list):
    assert order_by_points(input_list) == input_list

@pytest.mark.parametrize("input_list", [
    [11, 1],
    [1, 11],
    [1, 11, 1],
    [1, 1, 11],
])
def test_order_by_points_equal_sum(input_list):
    result = order_by_points(input_list)
    assert all(result.index(x) < result.index(y) for x, y in zip(result, result[1:]))

@pytest.mark.parametrize("input_list", [
    [123, 456, 789],
    [987, 654, 321],
    [123, 456, 789, 987, 654, 321]
])
def test_order_by_points_large_numbers(input_list):
    assert order_by_points(input_list) == sorted(input_list, key=lambda x: (sum_digits(x), input_list.index(x)))

def test_order_by_points_with_negative_numbers():
    assert order_by_points([-1, -10, -100, -1000]) == [-1, -10, -100, -1000]

def test_order_by_points_empty_list_negative():
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_positive_and_negative():
    assert order_by_points([-1, 1, -2, 2, 3]) == [-1, -2, 1, 2, 3]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 2, 2, 3]) == [1, 1, 2, 2, 3]

def test_same_digit_sum_different_index():
    assert order_by_points([1, 11, 2, 21]) == [1, 2, 11, 21]

def test_same_digit_sum_same_index():
    assert order_by_points([1, 11, 2, 21]) == [1, 11, 2, 21]

def test_complex_example1():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_complex_example2():
    assert order_by_points([10, 20, 30, 1, 2, 3]) == [1, 2, 3, 10, 20, 30]

def test_large_numbers():
    assert order_by_points([123, 456, 789]) == [123, 456, 789]

def test_zero():
    assert order_by_points([0, 1, 2]) == [0, 1, 2]

def test_negative_zero():
    assert order_by_points([-0, 0, -1]) == [-1, 0, -0]
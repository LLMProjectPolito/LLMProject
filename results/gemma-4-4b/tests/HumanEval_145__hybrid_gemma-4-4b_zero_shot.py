
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

class TestOrderByPoints:

    def test_empty_list(self):
        assert order_by_points([]) == []

    def test_single_element(self):
        assert order_by_points([5]) == [5]

    def test_positive_numbers(self):
        assert order_by_points([1, 11, 2, 20, 3]) == [1, 2, 3, 11, 20]

    def test_negative_numbers(self):
        assert order_by_points([-1, -11, -2, -20, -3]) == [-3, -2, -1, -11, -20]

    def test_mixed_positive_and_negative(self):
        assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    def test_same_digit_sum(self):
        assert order_by_points([10, 19, 28, 37]) == [10, 19, 28, 37]

    def test_large_numbers(self):
        assert order_by_points([12345, 54321, 11111]) == [11111, 12345, 54321]
    
    def test_zero(self):
        assert order_by_points([0, 1, -1, 10]) == [0, -1, 1, 10]

    def test_duplicate_numbers(self):
        assert order_by_points([1, 1, 2, 2]) == [1, 1, 2, 2]
    
    def test_all_same_digit_sum(self):
        assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_negative_and_zero(self):
        assert order_by_points([-1, 0, -10]) == [0, -1, -10]
    
    def test_complex_case(self):
        assert order_by_points([12, 21, 1, 10, 20]) == [1, 10, 12, 20, 21]
    
    def test_all_negative(self):
        assert order_by_points([-10, -1, -100]) == [-1, -10, -100]

Suite 2:
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
    "nums, expected",
    [
        ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
        ([], []),
        ([12, 1], [1, 12]),
        ([2, 20, 200], [2, 20, 200]),
        ([-1, -10, 10], [-1, -10, 10]),
        ([100, 10, 1], [1, 10, 100]),
        ([10, 1], [1, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([111, 22, 3, 44], [3, 44, 22, 111]),
        ([-1, 0, 1], [-1, 0, 1]),
        ([1, -1, 2, -2], [-1, 1, -2, 2])
    ],
)
def test_order_by_points_basic(nums, expected):
    assert order_by_points(nums) == expected

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 11, -1, -11, -12, 121, 10], [-1, -11, 1, 10, 11, 121, -12]),
        ([1, 11, -1, -11, -12, 121, 10, 1, 11, -1, -11, -12, 121, 10], [-1, -11, 1, 10, 11, 121, -12, 1, 11, -1, -11, -12, 121, 10]),
    ],
)
def test_order_by_points_larger(nums, expected):
    assert order_by_points(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 2, 1, 20, 100, 200], [1, 2, 10, 20, 100, 200]),
        ([200, 20, 2, 10, 1], [1, 2, 10, 20, 200])
    ],
)
def test_order_by_points_mixed(nums, expected):
    assert order_by_points(nums) == expected

@pytest.mark.parametrize(
    "nums, expected",
    [
       ([1111, 111, 11, 1], [1, 11, 111, 1111])
    ]
)
def test_order_by_points_all_same_sum(nums, expected):
     assert order_by_points(nums) == expected

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, -2, -3], [-1, -2, -3]),
        ([1, 2, 3], [1, 2, 3]),
    ]
)
def test_order_by_points_negative_numbers(nums, expected):
    assert order_by_points(nums) == expected
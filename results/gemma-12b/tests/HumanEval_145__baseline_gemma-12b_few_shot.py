
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

def sum_digits(n: int) -> int:
    """Calculates the sum of the digits of an integer."""
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_same_digit_sum():
    assert order_by_points([1, 10, 100]) == [1, 10, 100]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_order_by_points_zero():
    assert order_by_points([0, 1, -1]) == [0, 1, -1]

def test_order_by_points_duplicate_numbers():
    assert order_by_points([2, 2, 2]) == [2, 2, 2]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 6]) == [45, 6, 123]

def test_order_by_points_complex_case():
    assert order_by_points([12, 21, 3, 1, 4]) == [3, 1, 12, 21, 4]

def test_order_by_points_all_negative():
    assert order_by_points([-12, -21, -3, -1, -4]) == [-1, -3, -12, -21, -4]
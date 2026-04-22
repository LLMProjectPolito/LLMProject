
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
        n = abs(n)  # Handle negative numbers
        while n:
            s += n % 10
            n //= 10
        return s

    return sorted(enumerate(nums), key=lambda x: (sum_digits(x[1]), x[0]))[0].map(1)[1] if nums else []


# Pytest tests for is_palindrome
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_insensitive():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Spaces and punctuation are not handled

def test_palindrome_negative_number():
    assert is_palindrome('-121') == False # Negative sign is not handled

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == False

# Pytest tests for get_max
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_single_element():
    assert get_max([5]) == 5

# Pytest tests for order_by_points
def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_same_digit_sum():
    assert order_by_points([10, 1, 100]) == [1, 10, 100]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 6]) == [6, 45, 123]
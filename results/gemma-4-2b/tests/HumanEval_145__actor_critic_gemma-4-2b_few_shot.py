
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False
    assert is_palindrome(' ') == True
    assert is_palindrome('.,') == True
    assert is_palindrome('0P') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('RaceCar') == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_single():
    assert get_max([5]) == 5

def test_get_max_duplicate():
    assert get_max([5, 5, 5]) == 5

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_same_sum():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 2, -2]) == [-1, -2, 1, 2]

def test_order_by_points_zero():
    assert order_by_points([0, 1, 0, 2]) == [0, 0, 1, 2]
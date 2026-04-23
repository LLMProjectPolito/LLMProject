
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10 and (num % 10 != 0) and (num % 100 != 0):
            num_str = str(abs(num))
            if num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_specialFilter_positive():
    assert specialFilter([15, 33, 55, 77]) == 4

def test_specialFilter_negative():
    assert specialFilter([-15, -33, -55, -77]) == 0

def test_specialFilter_mixed():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([20, 40, 60]) == 0

def test_specialFilter_all_match():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_large_numbers():
    assert specialFilter([1000000001, 1000000003, 1000000005, 1000000007, 1000000009]) == 5

def test_specialFilter_mixed_negative_and_positive():
    assert specialFilter([-15, 33, -55, 77, -99, 101]) == 2
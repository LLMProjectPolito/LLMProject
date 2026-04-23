
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
    s = s.lower()
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
        num_str = str(abs(num))  # Handle negative numbers
        if num > 10 and num_str[0] in '13579' and num_str[-1] in '13579':
            count += 1
    return count



def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True # Test with spaces and punctuation
    assert is_palindrome('Racecar') == True # Test with capitalization
    assert is_palindrome('madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome(' ') == True # Test with space
    assert is_palindrome('') == True # Test empty string

def test_is_palindrome_edge_cases():
    assert is_palindrome('1') == False
    assert is_palindrome('0') == False
    assert is_palindrome('11') == True
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False
    assert is_palindrome('1001') == True
    assert is_palindrome('101') == True
    assert is_palindrome('10') == False
    assert is_palindrome('1') == False
    assert is_palindrome('11111') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 2]) == 9
    assert get_max([10, 5, 20, 15]) == 20
    assert get_max([1]) == 1

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-5, -10, -2]) == -2
    assert get_max([-1, 0, 1]) == 1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4
    assert get_max([5, -10, 2, -1]) == 5

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_some_matching_numbers():
    assert specialFilter([15, 23, 35, 47, 59, 12, 34, 56]) == 3

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -23, -35, -47, -59, -12, -34, -56]) == 0

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([15, -23, 35, -47, 59, 12, -34, 56]) == 3

def test_specialFilter_zero_and_odd_digits():
    assert specialFilter([10, 11, 13, 15, 20, 33]) == 3

def test_specialFilter_large_numbers():
    assert specialFilter([1001, 1234, 5678, 9009]) == 2
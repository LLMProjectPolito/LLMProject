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
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) > 0 and num_str[0] % 2 != 0 and num_str[-1] % 2 != 0:
                count += 1
    return count

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_basic1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_basic2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_no_match():
    assert specialFilter([12, 14, 16, 18]) == 0

def test_specialFilter_all_match():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_mixed():
    assert specialFilter([11, 13, 12, 15, 14, 17, 18, 19]) == 3
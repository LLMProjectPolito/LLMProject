
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

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
            num_str = str(abs(num))  # Handle negative numbers
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == False #Added to test with spaces and punctuation

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('b') == False

def test_palindrome_multiple_chars():
    assert is_palindrome('madam') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('refer') == True

def test_palindrome_not_palindrome():
    assert is_palindrome('hello') == False
    assert is_palindrome('world') == False
    assert is_palindrome('python') == False

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False #Case sensitive

def test_palindrome_with_spaces():
    assert is_palindrome("  radar  ") == False #Spaces are not considered

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

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([2, 4, 6, 8]) == 0

def test_specialFilter_one_match():
    assert specialFilter([15, 25, 35]) == 1

def test_specialFilter_multiple_matches():
    assert specialFilter([15, 35, 55, 75, 95]) == 5

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -35, -55, -75, -95]) == 5

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([15, -35, 55, -75, 95]) == 3

def test_specialFilter_zero():
    assert specialFilter([0, 10, 20]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([1000000001, 1000000003, 1000000005, 1000000007, 1000000009]) == 5

def test_specialFilter_edge_cases():
    assert specialFilter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert specialFilter([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert specialFilter([10, 20, 30, 40, 50]) == 0
    assert specialFilter([100, 101, 102, 103, 104]) == 0
    assert specialFilter([1000, 1001, 1002, 1003, 1004]) == 0
    assert specialFilter([1000000001, 1000000003, 1000000005, 1000000007, 1000000009, 1000000011]) == 5
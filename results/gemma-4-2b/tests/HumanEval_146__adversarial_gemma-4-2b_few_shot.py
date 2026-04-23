
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
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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

# --- Tests for is_palindrome ---
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == True

def test_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam') == True

def test_palindrome_with_numbers():
    assert is_palindrome('121') == True

def test_palindrome_with_numbers_and_letters():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_palindrome_with_leading_and_trailing_spaces():
    assert is_palindrome("  racecar  ") == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) is None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4, -5]) == 4

def test_max_duplicate_values():
    assert get_max([5, 5, 5]) == 5

# --- Tests for specialFilter ---
def test_specialFilter_example1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_example2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_no_match():
    assert specialFilter([22, 44, 66]) == 0

def test_specialFilter_all_match():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([11, -33, 55, -77, 99, -11]) == 3

def test_specialFilter_zero():
    assert specialFilter([0, 10, 20]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([1000000, 1000001, 1000002]) == 1
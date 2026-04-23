
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
        if num > 10:
            num_str = str(abs(num))  # Handle negative numbers
            if len(num_str) > 0 and num_str[0] in '13579' and num_str[-1] in '13579':
                count += 1
    return count

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_multiple_chars():
    assert is_palindrome('racecar') == True
    assert is_palindrome('level') == True
    assert is_palindrome('madam') == True

def test_palindrome_mixed_case():
    assert is_palindrome('RaceCar') == True
    assert is_palindrome('RaCeCaR') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam.') == True

def test_palindrome_with_numbers():
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False

def test_palindrome_with_special_characters():
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('No 'not a palindrome') == True #Handles spaces

def test_palindrome_with_leading_and_trailing_spaces():
    assert is_palindrome('   racecar   ') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed_numbers():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_large_numbers():
  assert get_max([1000000, 2000000]) == 2000000

def test_get_max_with_zeros():
    assert get_max([0, 0, 0]) == 0

def test_get_max_with_duplicates():
    assert get_max([5, 5, 5]) == 5

def test_special_filter_positive():
    assert specialFilter([15, 33, 55, 77, 99, 11, 13, 15]) == 4

def test_special_filter_negative():
    assert specialFilter([-15, -33, -55, -77, -99, -11, -13, -15]) == 0

def test_special_filter_mixed():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_all_negative():
    assert specialFilter([-15, -33, -55, -77, -99]) == 0

def test_special_filter_all_positive():
    assert specialFilter([15, 33, 55, 77, 99]) == 5

def test_special_filter_no_match():
    assert specialFilter([10, 20, 30]) == 0

def test_special_filter_zero():
    assert specialFilter([0, 10]) == 0
    assert specialFilter([1, 10]) == 0
    assert specialFilter([15,0]) == 1

def test_special_filter_zero_and_odd():
    assert specialFilter([0, 15, 33]) == 2

def test_special_filter_with_zeros_and_negative_odd():
    assert specialFilter([0, -15, 15, -33]) == 2

def test_special_filter_empty_list():
    assert specialFilter([]) == 0

def test_special_filter_with_single_element():
    assert specialFilter([15]) == 1
    assert specialFilter([-15]) == 1
    assert specialFilter([10]) == 0
    assert specialFilter([-10]) == 0
    assert specialFilter([1]) == 0
    assert specialFilter([-1]) == 0

def test_special_filter_with_single_element_not_matching():
  assert specialFilter([10]) == 0
  assert specialFilter([-10]) == 0
  assert specialFilter([11]) == 0
  assert specialFilter([-11]) == 0
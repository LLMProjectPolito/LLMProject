import pytest

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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_special_filter_empty():
    assert specialFilter([]) == 0

def test_special_filter_basic1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_basic2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_no_match():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_special_filter_all_match():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_special_filter_mixed():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99, 101]) == 5

def test_special_filter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_special_filter_large_numbers():
    assert specialFilter([1001, 12345, 98765, 11111]) == 2

def test_special_filter_single_digit_greater_than_10():
    assert specialFilter([11]) == 1
    assert specialFilter([12]) == 0

def test_special_filter_two_digit_number():
    assert specialFilter([13]) == 1

def test_special_filter_edge_case_111():
    assert specialFilter([111]) == 1

def test_special_filter_edge_case_1001():
    assert specialFilter([1001]) == 1

def test_special_filter_edge_case_1011():
    assert specialFilter([1011]) == 1

def test_special_filter_edge_case_10():
    assert specialFilter([10]) == 0

def test_special_filter_with_zero():
    assert specialFilter([15, 0, 33]) == 1

def test_special_filter_with_floats():
    assert specialFilter([15.0, 33.0]) == 0 #Floats are not handled, should be integers

def test_special_filter_with_strings():
    assert specialFilter(['15', '33']) == 0 #Strings are not handled, should be integers

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Get Max tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
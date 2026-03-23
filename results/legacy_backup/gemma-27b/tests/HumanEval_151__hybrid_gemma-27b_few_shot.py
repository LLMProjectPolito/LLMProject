import pytest

def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    if not lst:
        return 0
    
    total = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            total += num * num
    return total

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Double the Difference Tests
def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([1, 3, 5]) == 35
    assert double_the_difference([2, 4, 6]) == 0

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([-1, 3, -5, 7]) == 58

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0
    assert double_the_difference([0, 0, 0]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([1, 2, 3, 4, 5, -1, -2]) == 35
    assert double_the_difference([1.5, 2, 3, 4, 5]) == 34 #float ignored
    assert double_the_difference([1, "a", 3, 4, 5]) == 35 #string ignored

def test_double_the_difference_large_numbers():
    assert double_the_difference([99, 101]) == 9802
    assert double_the_difference([1001, 1003]) == 2006010

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_all_floats():
    assert double_the_difference([1.1, 3.3, 5.5]) == 0

def test_empty_list():
    assert double_the_difference([]) == 0

def test_basic_example():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_mixed_positive_and_negative():
    assert double_the_difference([9, -2]) == 81

def test_zero_only():
    assert double_the_difference([0]) == 0

def test_all_odd_positive():
    assert double_the_difference([1, 3, 5]) == 35

def test_all_even_positive():
    assert double_the_difference([2, 4, 6]) == 0

def test_floats_and_integers():
    assert double_the_difference([1, 2.5, 3, 4]) == 10

def test_strings_and_integers():
    assert double_the_difference([1, "a", 3, 4]) == 10

def test_large_numbers():
    assert double_the_difference([101, 203]) == 101**2 + 203**2

def test_mixed_types_and_values():
    assert double_the_difference([1, -2, 3.0, "hello", 5]) == 26

def test_list_with_only_one_odd_number():
    assert double_the_difference([2, 4, 6, 1, 8]) == 1

def test_list_with_only_one_even_number():
    assert double_the_difference([1, 3, 5, 2]) == 35

def test_list_with_multiple_odd_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1 + 9 + 25 + 49 + 81

# Palindrome Tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Get Max Tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
# STEP 1: REASONING
# The function `double_the_difference` calculates the sum of squares of odd integers in a list, ignoring negative numbers and non-integers.
# We need to test various scenarios:
# - Empty list
# - List with only even numbers
# - List with only odd numbers
# - List with a mix of odd and even numbers
# - List with negative numbers
# - List with non-integer numbers (floats, strings)
# - List with a combination of all the above.
# We should also test edge cases like zero.

# STEP 2: PLAN
# 1. test_empty_list: Test with an empty list.
# 2. test_only_even_numbers: Test with a list containing only even numbers.
# 3. test_only_odd_numbers: Test with a list containing only odd numbers.
# 4. test_mixed_odd_even: Test with a list containing both odd and even numbers.
# 5. test_negative_numbers: Test with a list containing negative numbers.
# 6. test_non_integer_numbers: Test with a list containing non-integer numbers (floats, strings).
# 7. test_mixed_types: Test with a list containing a mix of integers, floats, strings, and negative numbers.
# 8. test_zero: Test with a list containing only zero.
# 9. test_large_numbers: Test with large odd numbers to check for potential overflow issues.
# 10. test_single_odd: Test with a list containing only a single odd number.

# STEP 3: CODE
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
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49

def test_mixed_odd_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    assert double_the_difference([-1, -2, 3, 4, -5]) == 9

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2, 3.0, 4]) == 0

def test_mixed_types():
    assert double_the_difference([1, 2.5, 3, "4", -5]) == 1 + 9

def test_zero():
    assert double_the_difference([0, 2, 4, 6]) == 0

def test_large_numbers():
    assert double_the_difference([1001, 1003, 1005]) == 1001*1001 + 1003*1003 + 1005*1005

def test_single_odd():
    assert double_the_difference([5]) == 25
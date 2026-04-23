
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

# STEP 1: REASONING
# The function `double_the_difference` takes a list of numbers as input.
# It calculates the sum of squares of odd numbers in the list, ignoring negative numbers and non-integers.
# The function should return 0 if the input list is empty or if there are no odd numbers.
# The test cases cover various scenarios:
# 1. A list with odd and even numbers.
# 2. A list with only negative numbers.
# 3. A list with only positive numbers.
# 4. A list with zero.
# 5. An empty list.
# 6. A list with only odd numbers.
# 7. A list with a mix of odd and even numbers, including zero.

# STEP 2: PLAN
# The test suite will include the following test functions:
# - test_empty_list: Checks if the function returns 0 for an empty list.
# - test_positive_odd_numbers: Checks if the function returns the correct sum of squares for a list with positive odd numbers.
# - test_negative_numbers: Checks if the function returns 0 for a list with only negative numbers.
# - test_mixed_numbers: Checks if the function returns the correct sum of squares for a list with mixed positive and negative numbers.
# - test_zero: Checks if the function returns 0 for a list with zero.
# - test_only_odd_numbers: Checks if the function returns the correct sum of squares for a list with only odd numbers.
# - test_mixed_odd_even_zero: Checks if the function returns the correct sum of squares for a list with mixed odd, even and zero numbers.

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
        if isinstance(num, int) and num % 2 != 0 and num >= 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25 == 35

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_numbers():
    assert double_the_difference([1, -2, 3, -4]) == 1 + 9 == 10

def test_zero():
    assert double_the_difference([0]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49 == 84

def test_mixed_odd_even_zero():
    assert double_the_difference([1, 2, 3, 4, 5, 0]) == 1 + 9 + 25 == 35
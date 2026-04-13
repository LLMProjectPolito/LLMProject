
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
    total = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            total += num * num
    return total

### SCoT Steps:

# STEP 1: REASONING
# The function `double_the_difference` calculates the sum of squares of odd, positive integers in a list.
# It should handle empty lists, negative numbers, non-integer numbers, and zero correctly.
# The test suite should cover these edge cases and typical scenarios.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Checks the behavior with an empty list.
# - test_positive_odd_numbers: Checks with a list containing only positive odd numbers.
# - test_mixed_numbers: Checks with a list containing positive odd, even, negative, and zero numbers.
# - test_negative_numbers: Checks with a list containing only negative numbers.
# - test_non_integer_numbers: Checks with a list containing non-integer numbers.
# - test_zero_list: Checks with a list containing only zero.
# - test_single_odd_number: Checks with a list containing a single odd number.
# - test_single_even_number: Checks with a list containing a single even number.

# STEP 3: CODE
def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2, -3]) == 0

def test_zero_list():
    assert double_the_difference([0]) == 0

def test_single_odd_number():
    assert double_the_difference([1]) == 1

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_single_negative_odd_number():
    assert double_the_difference([-1]) == 0

def test_multiple_odd_numbers():
    assert double_the_difference([1, 3, 5, 7, 9]) == 165
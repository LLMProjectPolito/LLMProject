
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
        if isinstance(num, int) and num % 2 != 0:
            total += num * num
    return total

### SCoT Steps:

# STEP 1: REASONING
# The function `double_the_difference` calculates the sum of squares of odd integers in a list.
# It should ignore negative numbers and non-integer numbers.
# It should return 0 if the input list is empty.
# We need to test various scenarios including:
#   - Empty list
#   - List with only even numbers
#   - List with only odd numbers
#   - List with mixed odd and even numbers
#   - List with negative numbers
#   - List with non-integer numbers
#   - List with zero

# STEP 2: PLAN
# Test functions:
#   - test_empty_list: Tests the case when the input list is empty.
#   - test_only_even_numbers: Tests the case when the list contains only even numbers.
#   - test_only_odd_numbers: Tests the case when the list contains only odd numbers.
#   - test_mixed_numbers: Tests the case when the list contains both odd and even numbers.
#   - test_negative_numbers: Tests the case when the list contains negative numbers.
#   - test_non_integer_numbers: Tests the case when the list contains non-integer numbers.
#   - test_zero: Tests the case when the list contains zero.
#   - test_example_1: Tests the example case from the docstring.
#   - test_example_2: Tests the example case from the docstring.
#   - test_example_3: Tests the example case from the docstring.

# STEP 3: CODE
#
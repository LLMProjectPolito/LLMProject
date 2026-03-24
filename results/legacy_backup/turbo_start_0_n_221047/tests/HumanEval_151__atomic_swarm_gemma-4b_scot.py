import pytest
import math

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

def test_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

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
### STEP 1: REASONING - The function calculates the sum of squares of odd integers in a list. An edge case is an empty list, which should return 0. Another edge case is a list containing only zeros or negative numbers, which should also return 0.
### STEP 2: PLAN - Test function name: test_empty_list. Scenario: Test with an empty list. Test function name: test_all_zeros. Scenario: Test with a list containing only zeros. Test function name: test_all_negative. Scenario: Test with a list containing only negative numbers.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_zeros():
    assert double_the_difference([0, 0, 0]) == 0

def test_all_negative():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([-1, 2, 3, -4]) == 1 + 9 == 10

def test_single_odd():
    assert double_the_difference([1]) == 1

def test_single_even():
    assert double_the_difference([2]) == 0

def test_mixed_odd_even():
    assert double_the_difference([1, 2, 3, 4]) == 1 + 9 == 10

def test_negative_odd():
    assert double_the_difference([-1, 3]) == 1 + 9 == 10

def test_zero_and_odd():
    assert double_the_difference([0, 1]) == 1

def test_zero_and_negative_odd():
    assert double_the_difference([0, -1]) == 0

def test_complex_list():
    assert double_the_difference([1, 3, 2, 0, -1, -2, 5]) == 1 + 9 + 0 + 1 + 25 == 36

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
        if isinstance(num, int) and num > 0:
            total += num * num
    return total

### SCoT Steps:
### STEP 1: REASONING - The function should handle cases where the input list contains non-integer or negative numbers, or zero. The test should focus on a boundary condition where a non-positive integer is present in the list.
### STEP 2: PLAN - Test function name: test_non_positive_integer. Scenario: Input list containing a non-positive integer.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_non_positive_integer():
    assert double_the_difference([1, 2, 3, -4, 0]) == 1 + 9 + 0 == 10
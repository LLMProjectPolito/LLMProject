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
# Edge cases: empty list, list with only negative numbers, list with only non-integers, list with mixed types, list with zero.

# STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with positive odd integers: [1, 3, 5]
# 3. List with positive even integers: [2, 4, 6]
# 4. List with negative odd integers: [-1, -3, -5]
# 5. List with negative even integers: [-2, -4, -6]
# 6. List with mixed positive and negative integers: [1, -2, 3, -4]
# 7. List with non-integer values: [1.5, 2, 3]
# 8. List with zero: [0]
# 9. List with a single odd number: [1]
# 10. List with a single even number: [2]
# 11. List with a single negative number: [-1]

# STEP 3: CODE
def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_integers():
    assert double_the_difference([1, 3, 5]) == 35

def test_positive_even_integers():
    assert double_the_difference([2, 4, 6]) == 0

def test_negative_odd_integers():
    assert double_the_difference([-1, -3, -5]) == 35

def test_negative_even_integers():
    assert double_the_difference([-2, -4, -6]) == 0

def test_mixed_positive_negative_integers():
    assert double_the_difference([1, -2, 3, -4]) == 30

def test_non_integer_values():
    assert double_the_difference([1.5, 2, 3]) == 0

def test_zero():
    assert double_the_difference([0]) == 0

def test_single_odd_number():
    assert double_the_difference([1]) == 1

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_single_negative_number():
    assert double_the_difference([-1]) == 1

def test_mixed_odd_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_all_negative_and_non_integers():
    assert double_the_difference([-1.5, -2, -3]) == 0
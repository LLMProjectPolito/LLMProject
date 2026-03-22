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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `double_the_difference` calculates the sum of squares of odd, positive integers in a list.
# It ignores negative numbers, non-integer numbers, and zero. An empty list should return 0.
# We need to test various scenarios including empty lists, lists with only negative numbers, lists with mixed positive and negative numbers, lists with zero, lists with only odd numbers, and lists with only even numbers.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list
# test_negative_numbers
# test_mixed_positive_negative
# test_zero
# test_only_odd_numbers
# test_only_even_numbers
# test_single_odd_number
# test_single_even_number
# test_mixed_odd_even_integers
# test_non_integer_values

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([1, -2, 3, -4]) == 1 + 9 == 10

def test_zero():
    assert double_the_difference([0, 1, 2]) == 1

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25 == 35

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_single_odd_number():
    assert double_the_difference([1]) == 1

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_mixed_odd_even_integers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25 == 35

def test_non_integer_values():
    assert double_the_difference([1, 2.5, 3, "a"]) == 1 + 9 == 10

def test_large_numbers():
    assert double_the_difference([1001, 2, 3]) == 1001 + 9 == 1010

def test_duplicate_odd_numbers():
    assert double_the_difference([1, 1, 3, 3]) == 1 + 1 + 9 + 9 == 20
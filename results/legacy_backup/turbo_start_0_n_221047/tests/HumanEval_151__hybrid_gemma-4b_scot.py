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
# The test suite needs to cover these edge cases and ensure the function returns the expected results.

# STEP 2: PLAN
# Test cases:
# 1. Empty list: [] - Expected output: 0
# 2. List with only even numbers: [2, 4, 6] - Expected output: 0
# 3. List with only negative numbers: [-1, -2, -3] - Expected output: 0
# 4. List with mixed positive and negative numbers: [1, -2, 3, -4] - Expected output: 1 + 9 = 10
# 5. List with zero: [0, 1, 2] - Expected output: 1
# 6. List with only zero: [0] - Expected output: 0
# 7. List with odd and even numbers: [1, 2, 3, 4, 5] - Expected output: 1 + 9 + 25 = 35
# 8. List with a single odd number: [7] - Expected output: 49
# 9. List with a single negative odd number: [-7] - Expected output: 49
# 10. List with a single even number: [2] - Expected output: 0
# 11. List with a single zero: [0] - Expected output: 0
# 12. List with a mix of positive and negative odd numbers: [1, -3, 5, -7] - Expected output: 1 + 9 + 25 + 49 = 84

# STEP 3: CODE
### pytest suite
def test_empty_list():
    assert double_the_difference([]) == 0

def test_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([1, -2, 3, -4]) == 10

def test_with_zero():
    assert double_the_difference([0, 1, 2]) == 1

def test_only_zero():
    assert double_the_difference([0]) == 0

def test_odd_and_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_single_odd():
    assert double_the_difference([7]) == 49

def test_single_negative_odd():
    assert double_the_difference([-7]) == 49

def test_single_even():
    assert double_the_difference([2]) == 0

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_mixed_odd_negative():
    assert double_the_difference([1, -3, 5, -7]) == 84
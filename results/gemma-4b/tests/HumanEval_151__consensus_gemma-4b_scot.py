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

### STEP 1: REASONING
# The function `double_the_difference` calculates the sum of squares of odd integers in a list.
# It should handle empty lists, negative numbers, non-integer numbers, and zero correctly.
# The test suite should cover these cases and verify the function's output against the expected values.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with only even numbers: [2, 4, 6]
# 3. List with only odd numbers: [1, 3, 5]
# 4. List with mixed odd and even numbers: [1, 2, 3, 4, 5]
# 5. List with negative odd numbers: [-1, -3]
# 6. List with negative and odd numbers: [-1, 3]
# 7. List with zero: [0]
# 8. List with non-integer values: [1, 2.5, 3]
# 9. List with a mix of integers and floats: [1, 2.0, 3]
# 10. List with a single odd number: [1]
# 11. List with a single even number: [2]

### STEP 3: CODE
def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_odd_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_negative_odd_numbers():
    assert double_the_difference([-1, -3]) == 10

def test_negative_and_odd_numbers():
    assert double_the_difference([-1, 3]) == 10

def test_zero():
    assert double_the_difference([0]) == 0

def test_non_integer_values():
    assert double_the_difference([1, 2.5, 3]) == 1

def test_mix_integers_and_floats():
    assert double_the_difference([1, 2.0, 3]) == 1

def test_single_odd_number():
    assert double_the_difference([1]) == 1

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81
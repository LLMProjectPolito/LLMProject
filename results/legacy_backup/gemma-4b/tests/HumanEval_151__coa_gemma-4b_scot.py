import pytest
import math


# Focus: Boundary Values
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
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `double_the_difference` calculates the sum of squares of odd integers in a list.
### We need to test boundary values: empty list, list with only negative numbers, list with only zeros, list with a single zero, list with a single odd number, list with a single negative odd number, and a list with a mix of positive and negative odd/even numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_list
### test_negative_numbers
### test_zero_list
### test_single_odd
### test_single_negative_odd
### test_mixed_numbers
### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `double_the_difference` calculates the sum of squares of odd integers in a list.
### We need to test boundary values: empty list, list with only negative numbers, list with only zeros, list with a single zero, list with a single odd number, list with a single negative odd number, and a list with a mix of positive and negative odd/even numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_list
### test_negative_numbers
### test_zero_list
### test_single_odd
### test_single_negative_odd
### test_mixed_numbers
### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `double_the_difference` calculates the sum of squares of odd integers in a list.
### We need to test boundary values: empty list, list with only negative numbers, list with only zeros, list with a single zero, list with a single odd number, list with a single negative odd number, and a list with a mix of positive and negative odd/even numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_list
### test_negative_numbers
### test_zero_list
### test_single_odd
### test_single_negative_odd
### test_mixed_numbers
### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `double_the_difference` calculates the sum of squares of odd integers in a list.
### We need to test boundary values: empty list, list with only negative numbers, list with only zeros, list with a single zero, list with a single odd number, list with a single negative odd number, and a list with a mix of positive and negative odd/even numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_list
### test_negative_numbers
### test_zero_list
### test_single_odd
### test_single_negative_odd
### test_mixed_numbers
### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `double_the_difference` calculates the sum of squares of odd integers in a list.
### We need to test boundary values: empty list, list with only negative numbers, list with only zeros, list with a single zero, list with a single odd number, list with a single negative odd number, and a list with a mix of positive and negative odd/even numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_list
### test_negative_numbers
### test_zero_list
### test_single_odd
### test_single_negative_odd
### test_mixed_numbers
### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `double_the_difference` calculates the sum of squares of odd integers in a list.
### We need to test boundary values: empty list, list with only negative numbers, list with only zeros, list with a single zero, list with a single odd number, list with a single negative odd number, and a list with a mix of positive and negative odd/even numbers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_list
### test_negative_numbers
### test_zero_list
### test_single_odd
### test_single_negative_odd
### test_mixed_numbers
### STEP 3: CODE - Write the high-quality pytest suite.
import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_zero_list():
    assert double_the_difference([0, 0, 0]) == 0

# Focus: Type Scenarios
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
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `double_the_difference` calculates the sum of squares of odd, positive integers in a list.
### Negative numbers, zero, and non-integer values should be ignored. An empty list should return 0.
### STEP 2: PLAN - List test functions names and scenarios.
### Test function 1: Empty list
### Test function 2: List with only even numbers
### Test function 3: List with mixed positive and negative odd numbers
### STEP 3: CODE - Write the high-quality pytest suite.

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_mixed_odd_negative_numbers():
    assert double_the_difference([1, 3, -2, 5, -7]) == 1 + 9 + 25 + 49 == 84

# Focus: Logic Branches
import pytest

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_all_positive_odd():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_double_the_difference_mixed_positive_and_negative():
    assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25

def test_double_the_difference_all_negative_and_zero():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_only_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_with_non_integers():
    assert double_the_difference([1.5, 3, 2]) == 9

def test_double_the_difference_with_negative_non_integers():
    assert double_the_difference([-1.5, -3, 2]) == 0
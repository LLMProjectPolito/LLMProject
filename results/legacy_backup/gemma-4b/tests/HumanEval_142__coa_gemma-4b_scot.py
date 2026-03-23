import pytest
import math


# Focus: Boundary Values
import pytest

def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total += num**3
    return total

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `sum_squares` calculates a sum based on the index of each element in the input list.
### Boundary values are indices 0, 3, and the length of the list.  We need to test these specifically.
### The function handles empty lists and lists with negative numbers.

### STEP 2: PLAN - List test functions names and scenarios.
### test_sum_squares_empty_list
### test_sum_squares_index_0
### test_sum_squares_index_3
### test_sum_squares_index_4

### STEP 3: CODE - Write the high-quality pytest suite.
def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_index_0():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_index_3():
    assert sum_squares([1, 2, 3, 4]) == 36

def test_sum_squares_index_4():
    assert sum_squares([1, 2, 3, 4, 5]) == 150

# Focus: Type Scenarios
import pytest

def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total += num**3
    return total

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `sum_squares` calculates a sum based on the index of each element in the input list.
### The index plays a crucial role in determining whether an element is squared or cubed.
### We need to test different index scenarios to ensure the function behaves as expected.
### STEP 2: PLAN - List test functions names and scenarios.
### test_sum_squares_empty_list
### test_sum_squares_multiple_of_3
### test_sum_squares_multiple_of_4_not_3
### STEP 3: CODE - Write the high-quality pytest suite.

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

# Focus: Logic Branches
import pytest

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_4_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 225
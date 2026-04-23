


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

# STEP 1: REASONING
# The function `sum_squares` calculates a sum based on the index of each element in a list.
# It squares elements at multiples of 3 and cubes elements at multiples of 4 (but not 3).
# The function should handle empty lists and lists with negative numbers correctly.
# We need to test various scenarios including empty lists, lists with positive and negative numbers, and lists with different index multiples.

# STEP 2: PLAN
# Test cases:
# 1. Empty list: [] - Expected output: 0
# 2. List with single element: [5] - Expected output: 25
# 3. List with multiples of 3: [1, 2, 3, 4, 5, 6] - Expected output: 91
# 4. List with multiples of 4 and 3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - Expected output: 385
# 5. List with negative numbers: [-1, -5, 2, -1, -5] - Expected output: 56
# 6. List with mixed positive and negative numbers: [-1, 2, -3, 4, -5, 6] - Expected output: 91
# 7. List with only multiples of 4: [4, 8, 12] - Expected output: 2304
# 8. List with only multiples of 3: [3, 6, 9] - Expected output: 126

# STEP 3: CODE
###
# Test Cases
def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element():
    assert sum_squares([5]) == 25

def test_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 91

def test_multiples_of_4_and_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == 56

def test_mixed_positive_and_negative():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == 91

def test_only_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 2304

def test_only_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 126

def test_example_1():
    assert sum_squares([1,2,3]) == 6

def test_example_2():
    assert sum_squares([]) == 0

def test_example_3():
    assert sum_squares([-1,-5,2,-1,-5]) == -126
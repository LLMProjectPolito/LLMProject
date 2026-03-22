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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `sum_squares` calculates a sum based on the elements of a list,
# applying different operations based on the index. The operations are:
# - If the index is a multiple of 3, square the element.
# - If the index is a multiple of 4 and not a multiple of 3, cube the element.
# The function should handle empty lists and lists with negative numbers correctly.
# The function should not modify the original list.

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Empty list: []
# 2. List with positive integers: [1, 2, 3]
# 3. List with negative integers: [-1, -5, 2, -1, -5]
# 4. List with mixed positive and negative integers: [1, -2, 3, -4, 5]
# 5. List with multiples of 3 and 4: [1, 2, 3, 4, 5, 6, 8, 9, 12]
# 6. List with only multiples of 4: [4, 8, 12, 16]
# 7. List with only multiples of 3: [3, 6, 9, 12]
# 8. List with a single element: [5]
# 9. List with a single negative element: [-5]

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_empty_list():
    assert sum_squares([]) == 0

def test_positive_integers():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_integers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_integers():
    assert sum_squares([1, -2, 3, -4, 5]) == 14

def test_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 8, 9, 12]) == 228

def test_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 420

def test_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 162

def test_single_element():
    assert sum_squares([5]) == 25

def test_single_negative_element():
    assert sum_squares([-5]) == -125
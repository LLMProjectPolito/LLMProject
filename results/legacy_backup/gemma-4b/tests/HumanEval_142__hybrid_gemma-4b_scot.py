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
# The function `sum_squares` calculates a sum based on the elements of a list, applying different transformations based on the index.
# The transformations are:
#   - If the index is a multiple of 3, the element is squared.
#   - If the index is a multiple of 4 and not a multiple of 3, the element is cubed.
#   - Otherwise, the element remains unchanged.
# The function returns the sum of the transformed elements.
# Edge cases: empty list, list with negative numbers.

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Empty list: []
# 2. List with positive integers: [1, 2, 3]
# 3. List with negative integers: [-1, -5, 2, -1, -5]
# 4. List with mixed positive and negative integers: [1, -2, 3, -4, 5]
# 5. List with multiples of 3 and 4: [3, 4, 9, 16]
# 6. List with only multiples of 4: [4, 8, 12]
# 7. List with only multiples of 3: [3, 6, 9]
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
    assert sum_squares([1, -2, 3, -4, 5]) == 136

def test_multiples_of_3_and_4():
    assert sum_squares([3, 4, 9, 16]) == 3 + 64 + 81 + 256 == 404

def test_only_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 64 + 512 + 1728 == 2304

def test_only_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 9 + 36 + 81 == 126

def test_single_element():
    assert sum_squares([5]) == 25

def test_single_negative_element():
    assert sum_squares([-5]) == -125
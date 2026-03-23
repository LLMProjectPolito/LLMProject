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
    new_lst = []
    for i in range(len(lst)):
        if i % 3 == 0:
            new_lst.append(lst[i]**2)
        elif i % 4 == 0 and i % 3 != 0:
            new_lst.append(lst[i]**3)
        else:
            new_lst.append(lst[i])
    return sum(new_lst)

# STEP 2: PLAN - List test functions names and scenarios.
# Test Cases:
# 1. Empty list
# 2. List with only multiples of 3
# 3. List with only multiples of 4 (and not 3)
# 4. List with multiples of both 3 and 4
# 5. List with no multiples of 3 or 4
# 6. List with negative numbers
# 7. List with mixed positive and negative numbers
# 8. Larger list to test performance
# 9. List with zero values

# STEP 3: CODE - Write the high-quality pytest suite.

def test_empty_list():
    assert sum_squares([]) == 0

def test_multiples_of_3():
    assert sum_squares([1, 2, 3]) == 1 + 2 + 9

def test_multiples_of_4_not_3():
    assert sum_squares([1, 2, 3, 4]) == 1 + 2 + 9 + 64

def test_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 64 + 5 + 36

def test_no_multiples_of_3_or_4():
    assert sum_squares([1, 2, 5, 7]) == 1 + 2 + 5 + 7

def test_negative_numbers():
    assert sum_squares([-1, -2, -3]) == -1 + -2 + 9

def test_mixed_numbers():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == 1 + 4 + 9 + 64 + 25 + 36

def test_larger_list():
    lst = list(range(1, 21))
    expected_sum = sum([x**2 if i % 3 == 0 else (x**3 if i % 4 == 0 and i % 3 != 0 else x) for i, x in enumerate(lst)])
    assert sum_squares(lst) == expected_sum

def test_zero_values():
    assert sum_squares([0, 0, 0]) == 0

def test_example_case_1():
    assert sum_squares([1,2,3]) == 6

def test_example_case_2():
    assert sum_squares([]) == 0

def test_example_case_3():
    assert sum_squares([-1,-5,2,-1,-5]) == -126



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
        else:
            total += num
    return total

# STEP 1: REASONING
# The function `sum_squares` modifies a list based on the index of each element.
# It squares elements at indices that are multiples of 3.
# It cubes elements at indices that are multiples of 4 but not multiples of 3.
# It leaves other elements unchanged.
# The function then returns the sum of all elements in the modified list.
# We need to test various scenarios including:
# - Empty list
# - List with only elements whose indices are multiples of 3
# - List with only elements whose indices are multiples of 4 but not 3
# - List with a mix of elements satisfying different conditions
# - List with negative numbers
# - List with zero
# - List with large numbers

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Checks the function's behavior with an empty list.
# - test_multiples_of_3: Checks the function's behavior with a list where only indices are multiples of 3.
# - test_multiples_of_4_not_3: Checks the function's behavior with a list where only indices are multiples of 4 but not 3.
# - test_mixed_indices: Checks the function's behavior with a list containing elements at indices that are multiples of 3, 4, and neither.
# - test_negative_numbers: Checks the function's behavior with a list containing negative numbers.
# - test_zero: Checks the function's behavior with a list containing zero.
# - test_large_numbers: Checks the function's behavior with a list containing large numbers.
# - test_example_1: Checks the first example provided in the docstring.
# - test_example_2: Checks the second example provided in the docstring.
# - test_example_3: Checks the third example provided in the docstring.

# STEP 3: CODE
class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_multiples_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 4 + 25 + 36

    def test_multiples_of_4_not_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 8

    def test_mixed_indices(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == (
            1**2 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9**2 + 10 + 11 + 12**2
        )

    def test_negative_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == (-1)**2 + (-5) + 2**2 + (-1)**3 + (-5)

    def test_zero(self):
        assert sum_squares([0, 1, 2, 3, 4]) == 0**2 + 1 + 2 + 3**2 + 4**3

    def test_large_numbers(self):
        assert sum_squares([100, 200, 300, 400]) == 100**2 + 200 + 300**2 + 400**3

    def test_example_1(self):
        assert sum_squares([1, 2, 3]) == 6

    def test_example_2(self):
        assert sum_squares([]) == 0

    def test_example_3(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == -126
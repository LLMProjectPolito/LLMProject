


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
# The modifications are squaring if the index is a multiple of 3, cubing if the index is a multiple of 4 but not 3, and no change otherwise.
# The function then returns the sum of the modified list.
# We need to test various scenarios including:
# - Empty list
# - List with only positive numbers
# - List with only negative numbers
# - List with mixed positive and negative numbers
# - Lists with indices that are multiples of 3, 4, both, and neither.
# - Edge cases with large numbers.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Checks the function's behavior with an empty list.
# - test_positive_numbers: Checks the function with a list of positive numbers.
# - test_negative_numbers: Checks the function with a list of negative numbers.
# - test_mixed_numbers: Checks the function with a list of mixed positive and negative numbers.
# - test_multiple_of_3: Checks the function with a list where some indices are multiples of 3.
# - test_multiple_of_4: Checks the function with a list where some indices are multiples of 4.
# - test_multiple_of_both: Checks the function with a list where some indices are multiples of both 3 and 4.
# - test_no_multiples: Checks the function with a list where no indices are multiples of 3 or 4.
# - test_large_numbers: Checks the function with a list containing large numbers.

# STEP 3: CODE
class TestSumSquares:
    def test_empty_list(self):
        assert sum_squares([]) == 0

    def test_positive_numbers(self):
        assert sum_squares([1, 2, 3, 4, 5]) == 1**2 + 2 + 3**2 + 4**3 + 5 == 1 + 2 + 9 + 64 + 5 == 81

    def test_negative_numbers(self):
        assert sum_squares([-1, -2, -3, -4, -5]) == (-1)**2 + (-2) + (-3)**2 + (-4)**3 + (-5) == 1 - 2 + 9 - 64 - 5 == -61

    def test_mixed_numbers(self):
        assert sum_squares([-1, -5, 2, -1, -5]) == (-1)**2 + (-5) + 2 + (-1)**2 + (-5)**3 == 1 - 5 + 2 + 1 - 125 == -126

    def test_multiple_of_3(self):
        assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 3**2 + 4 + 5 + 6**2 == 1 + 2 + 9 + 4 + 5 + 36 == 57

    def test_multiple_of_4(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 4**3 + 5 + 6 + 7 + 8**3 == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512 == 599

    def test_multiple_of_both(self):
        assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]) == 1 + 2 + 3**2 + 4**3 + 5 + 6 + 7 + 8**3 + 9**2 + 12**2 == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 81 + 144 == 831

    def test_no_multiples(self):
        assert sum_squares([1, 2, 5, 7, 10]) == 1 + 2 + 5 + 7 + 10 == 25

    def test_large_numbers(self):
        assert sum_squares([1000, 2000, 3000, 4000, 5000]) == 1000**2 + 2000 + 3000**2 + 4000**3 + 5000 == 1000000 + 2000 + 9000000 + 64000000 + 5000 == 74000000 + 10000 + 2000 == 74012000
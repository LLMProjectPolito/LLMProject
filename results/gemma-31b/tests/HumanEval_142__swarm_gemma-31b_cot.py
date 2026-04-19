


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
import math

@pytest.mark.parametrize("input_list, expected", [
    ([-2] * 13, -10),               # Tests overlap of multiples of 3 and 4 with -2
    ([-2, -2, -2, -2, -2], -4),     # Tests edge cases for indices 0-4 with -2
    ([-1] * 13, -3),                # Tests LCM and negative logic with -1
])
def test_sum_squares_negative_scenarios(input_list, expected):
    """
    Tests the sum_squares function with negative numbers to verify power logic:
    - Indices that are multiples of 3 (including 0) should be squared.
    - Indices that are multiples of 4 (but not 3) should be cubed.
    - Other indices remain unchanged.
    """
    assert sum_squares(input_list) == expected



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
    ([2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2], 42),
    ([-2] * 13, -8),
    ([-2, 0, 0, -2, -2, 0, 0, 0, -2, 0, 0, 0, -2], -4),
])
def test_sum_squares_logic(input_list, expected):
    """
    Tests the sum_squares function for:
    - Index multiples of 3 (squared)
    - Index multiples of 4 but not 3 (cubed)
    - Priority of 3 over 4
    - Handling of negative numbers and zeros
    """
    assert sum_squares(input_list) == expected
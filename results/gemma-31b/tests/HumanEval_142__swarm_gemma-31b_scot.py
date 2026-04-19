


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

@pytest.mark.parametrize("lst, expected", [
    # Tests overlapping indices (0, 12), priority of 3 over 4, and negative numbers
    ([-2, 0, 0, -3, -4, 0, -5, 0, -2, 0, 0, 0, -6], 2),
    # Tests priority of multiple-of-3 rule over multiple-of-4 rule with constant values
    ([2] * 13, 48),
    # Tests boundary indices and specific cubing at index 4 and 8 with sparse values
    ([2, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2], 28),
], ids=["overlapping_and_negatives", "lcm_and_priority", "overlap_and_boundaries"])
def test_sum_squares(lst, expected):
    assert sum_squares(lst) == expected
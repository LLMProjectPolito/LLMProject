import pytest
import math

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

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3], 6),
    ([], 0),
    ([-1, -5, 2, -1, -5], -126),
    ([1, 2, 3, 4, 5, 6], 145),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 285),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 385),
    ([1], 1),
    ([2], 4),
    ([3], 9),
    ([4], 64),
    ([5], 125),
    ([6], 36),
    ([7], 49),
    ([8], 512),
    ([9], 81),
    ([10], 100),
])
def test_sum_squares(lst, expected):
    assert sum_squares(lst) == expected
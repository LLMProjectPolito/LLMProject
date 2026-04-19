


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
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    """
    total = 0
    for i in range(len(lst)):
        val = lst[i]
        if i % 3 == 0:
            total += val ** 2
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total

@pytest.mark.parametrize("lst, expected", [
    # Provided examples
    ([1, 2, 3], 6),               # idx 0: 1^2=1, idx 1: 2, idx 2: 3 -> 1+2+3=6
    ([], 0),                      # Empty list
    ([-1, -5, 2, -1, -5], -126),  # idx 0: (-1)^2=1, idx 1: -5, idx 2: 2, idx 3: (-1)^2=1, idx 4: (-5)^3=-125 -> 1-5+2+1-125 = -126
    
    # Edge Case: Single element (Index 0 is multiple of 3)
    ([2], 4),                     # 2^2 = 4
    ([0], 0),                     # 0^2 = 0
    ([-2], 4),                    # (-2)^2 = 4
    
    # Edge Case: Index 0 vs Index 4 (Multiple of 3 vs Multiple of 4)
    # idx 0: 2^2=4, idx 1: 1, idx 2: 1, idx 3: 2^2=4, idx 4: 2^3=8
    ([2, 1, 1, 2, 2], 18),        # 4 + 1 + 1 + 4 + 8 = 18
    
    # Edge Case: Index 12 (Multiple of both 3 and 4)
    # Should be squared because it is a multiple of 3
    ([1] * 13, 13),               # 5 squared, 2 cubed, 6 normal = 5+2+6 = 13
    ([0] * 12 + [2], 4),          # Only index 12 is non-zero: 2^2 = 4
    
    # Testing with larger numbers and negatives
    # idx 0: (-2)^2=4, idx 1: 10, idx 2: 10, idx 3: 3^2=9, idx 4: (-2)^3=-8
    ([-2, 10, 10, 3, -2], 25),    # 4 + 10 + 10 + 9 - 8 = 25
    
    # Basic list processing (formerly test_sum_squares_no_multiples)
    # idx 0: 3^2=9, idx 1: 1, idx 2: 1
    ([3, 1, 1], 11),              # 9 + 1 + 1 = 11
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected
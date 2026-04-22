


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

@pytest.mark.parametrize("lst, expected", [
    ([], 0),                                      # Empty list
    ([1, 2, 3], 6),                               # Docstring example 1: idx 0 (sq) -> 1+2+3=6
    ([-1, -5, 2, -1, -5], -126),                  # Docstring example 3: idx 0 (sq), 3 (sq), 4 (cube) -> 1-5+2+1-125=-126
    ([5], 25),                                    # Single element: idx 0 (sq) -> 5^2=25
    ([1, 1, 1, 1, 2], 12),                        # Index 4 is multiple of 4 and not 3: 1+1+1+1+2^3=12
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 16), # Index 12 is multiple of 3 and 4: 12*1 + 2^2=16
    ([10, 10, 10, 10, 10], 1120),                 # Mixed: idx 0(sq), 1, 2, 3(sq), 4(cube) -> 100+10+10+100+1000
    ([0, 0, 0, 0], 0),                            # Zeros
    ([-2, -2, -2, -2, -2], -4),                   # Negative logic: idx 0(sq), 1, 2, 3(sq), 4(cube) -> 4-2-2+4-8=-4
])
def test_sum_squares(lst, expected):
    """
    Tests the sum_squares function with various edge cases, 
    docstring examples, and index-specific logic rules.
    """
    # Assuming sum_squares is defined in the same module or imported
    from solution import sum_squares 
    assert sum_squares(lst) == expected
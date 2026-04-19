


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
    ([1, 2, 3], 6),                               # Example 1: i=0(sq), i=1, i=2
    ([-1, -5, 2, -1, -5], -126),                  # Example 2: i=0(sq), i=1, i=2, i=3(sq), i=4(cube)
    ([2], 4),                                     # Single element at index 0 (multiple of 3)
    ([0, 0, 0, 2], 4),                            # Index 3 is multiple of 3: 2^2 = 4
    ([0, 0, 0, 0, 2], 8),                         # Index 4 is multiple of 4 (not 3): 2^3 = 8
    ([0, 0, 0, 0, 0, 0, 2], 4),                   # Index 6 is multiple of 3: 2^2 = 4
    ([0, 0, 0, 0, 0, 0, 0, 0, 2], 8),             # Index 8 is multiple of 4 (not 3): 2^3 = 8
    ([0] * 12 + [2], 4),                          # Index 12 is multiple of 3: 2^2 = 4
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13), # All 1s, sum should be length
    ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 48), # Mixed powers of 2
    ([-2, -2, -2, -2, -2], -22),                  # i=0:4, i=1:-2, i=2:-2, i=3:4, i=4:-8 -> 4-2-2+4-8 = -4? 
                                                  # Wait: i=0:(-2)^2=4, i=1:-2, i=2:-2, i=3:(-2)^2=4, i=4:(-2)^3=-8. 
                                                  # Sum: 4-2-2+4-8 = -4.
])

def test_sum_squares_parametrized(lst, expected):
    # Correcting the manual calculation for the last case in the list above
    # Let's re-verify [-2, -2, -2, -2, -2]:
    # i=0: (-2)^2 = 4
    # i=1: -2
    # i=2: -2
    # i=3: (-2)^2 = 4
    # i=4: (-2)^3 = -8
    # Total: 4 - 2 - 2 + 4 - 8 = -4
    pass

# Redefining the test cases clearly to avoid manual calculation errors in the parametrize block
@pytest.mark.parametrize("lst, expected", [
    ([], 0),
    ([1, 2, 3], 6),
    ([-1, -5, 2, -1, -5], -126),
    ([2], 4),
    ([0, 0, 0, 2], 4),
    ([0, 0, 0, 0, 2], 8),
    ([0, 0, 0, 0, 0, 0, 2], 4),
    ([0, 0, 0, 0, 0, 0, 0, 0, 2], 8),
    ([0] * 12 + [2], 4),
    ([1] * 13, 13),
    ([2] * 13, 48),
    ([-2, -2, -2, -2, -2], -4),
])
def test_sum_squares(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_large_numbers():
    # Test with larger integers to ensure power operations work
    lst = [10, 0, 0, 10, 10] 
    # i=0: 10^2 = 100
    # i=1: 0
    # i=2: 0
    # i=3: 10^2 = 100
    # i=4: 10^3 = 1000
    # Sum: 1200
    assert sum_squares(lst) == 1200
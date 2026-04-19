


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
    ([1, 2, 3], 6),
    ([], 0),
    ([-1, -5, 2, -1, -5], -126),
    ([0, 0, 0, 0, 0], 0),
    ([2], 4),  # Index 0: 2^2 = 4
    ([1, 1, 1, 2], 7),  # Index 0: 1^2=1, Index 3: 2^2=4. Sum: 1+1+1+4 = 7
    ([1, 1, 1, 1, 2], 12),  # Index 0: 1^2=1, Index 3: 1^2=1, Index 4: 2^3=8. Sum: 1+1+1+1+8 = 12
])
def test_sum_squares_basic_and_examples(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_index_priority():
    """
    Test that index 12 (multiple of both 3 and 4) is squared, not cubed.
    """
    # Create a list of 13 ones.
    # Indices that are multiples of 3: 0, 3, 6, 9, 12 (5 elements) -> 1^2 = 1
    # Indices that are multiples of 4 and NOT 3: 4, 8 (2 elements) -> 1^3 = 1
    # Other indices: 1, 2, 5, 7, 10, 11 (6 elements) -> 1
    # Total sum should be 13.
    lst = [1] * 13
    assert sum_squares(lst) == 13

def test_sum_squares_complex_calculation():
    """
    Test a specific sequence to verify all rules.
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Idx 0: 1^2 = 1
    Idx 1: 2
    Idx 2: 3
    Idx 3: 4^2 = 16
    Idx 4: 5^3 = 125
    Idx 5: 6
    Idx 6: 7^2 = 49
    Idx 7: 8
    Idx 8: 9^3 = 729
    Idx 9: 10^2 = 100
    Idx 10: 11
    Idx 11: 12
    Idx 12: 13^2 = 169
    Sum: 1+2+3+16+125+6+49+8+729+100+11+12+169 = 1131
    """
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert sum_squares(lst) == 1131

def test_sum_squares_negative_cubes():
    """
    Verify that negative numbers at index 4 (multiple of 4, not 3) remain negative when cubed.
    """
    # Index 0: (-2)^2 = 4
    # Index 1: 1
    # Index 2: 1
    # Index 3: 1^2 = 1
    # Index 4: (-2)^3 = -8
    lst = [-2, 1, 1, 1, -2]
    assert sum_squares(lst) == (4 + 1 + 1 + 1 - 8) # -1

def test_sum_squares_large_integers():
    """
    Test with larger integers to ensure no overflow issues (Python handles this naturally).
    """
    lst = [100, 1, 1, 100, 100]
    # Idx 0: 100^2 = 10000
    # Idx 1: 1
    # Idx 2: 1
    # Idx 3: 100^2 = 10000
    # Idx 4: 100^3 = 1000000
    # Sum: 1010002
    assert sum_squares(lst) == 1010002



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
    ([], 0),
    ([1, 2, 3], 6),
    ([-1, -5, 2, -1, -5], -126),
    ([2], 4),  # Index 0: 2^2 = 4
    ([0, 0, 0, 0], 0),
    ([1, 1, 1, 1, 1], 1 + 1 + 1 + 1**2 + 1**3), # idx 0: 1^2, idx 1: 1, idx 2: 1, idx 3: 1^2, idx 4: 1^3 = 5
])
def test_sum_squares_basic(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_multiples_of_3():
    # Indices 0, 3, 6 should be squared
    # [2, 1, 1, 2, 1, 1, 2] -> [4, 1, 1, 4, 1, 1, 4] -> sum = 16
    assert sum_squares([2, 1, 1, 2, 1, 1, 2]) == 16

def test_sum_squares_multiples_of_4_not_3():
    # Indices 4, 8 should be cubed
    # Index 0 is multiple of 3, so squared.
    # [1, 0, 0, 0, 2, 0, 0, 0, 2] 
    # idx 0: 1^2=1, idx 4: 2^3=8, idx 8: 2^3=8. Others 0.
    assert sum_squares([1, 0, 0, 0, 2, 0, 0, 0, 2]) == 17

def test_sum_squares_both_3_and_4():
    # Index 12 is a multiple of both 3 and 4. 
    # Rule: "square... if index is multiple of 3 AND cube... if index is multiple of 4 AND NOT a multiple of 3"
    # Therefore, index 12 must be squared.
    lst = [0] * 13
    lst[12] = 3
    # idx 0: 0^2=0, idx 3: 0^2=0, idx 4: 0^3=0, idx 6: 0^2=0, idx 8: 0^3=0, idx 9: 0^2=0, idx 12: 3^2=9
    assert sum_squares(lst) == 9

def test_sum_squares_negative_numbers():
    # idx 0: (-2)^2 = 4
    # idx 1: -1
    # idx 2: -1
    # idx 3: (-2)^2 = 4
    # idx 4: (-2)^3 = -8
    # Sum: 4 - 1 - 1 + 4 - 8 = -2
    assert sum_squares([-2, -1, -1, -2, -2]) == -2

def test_sum_squares_large_list():
    # Test a range to ensure logic holds over many indices
    lst = [1] * 20
    total = 0
    for i in range(20):
        if i % 3 == 0:
            total += 1**2
        elif i % 4 == 0:
            total += 1**3
        else:
            total += 1
    assert sum_squares(lst) == total



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

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3], 6),
        ([], 0),
        ([-1, -5, 2, -1, -5], -126),
        ([1, 2, 3, 4, 5, 6], 156),
        ([0, 0, 0], 0),
        ([1, 0, 1, 0, 1], 3),
        ([-1, 1, -1, 1], 0),
        ([2, 4, 6, 8, 10], 200),
        ([10, 20, 30, 40, 50], 1500),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 153),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 738),
        ([100, 200, 300, 400, 500], 1500000),
        ([-1, -2, -3, -4, -5], -144),
    ],
)
def test_sum_squares_basic(lst, expected):
    assert sum_squares(lst) == expected

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1], 1),
        ([2], 2),
        ([3], 3),
        ([4], 4),
        ([5], 5),
    ],
)
def test_sum_squares_single_element(lst, expected):
    assert sum_squares(lst) == expected

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 1, 1, 1], 4),
        ([2, 2, 2, 2], 8),
        ([3, 3, 3, 3], 12),
        ([4, 4, 4, 4], 16),
    ],
)
def test_sum_squares_all_same(lst, expected):
    assert sum_squares(lst) == expected

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 1, 2, 3], 6),
        ([1, 2, 3, 1, 2, 3, 4], 156),
    ],
)
def test_sum_squares_repeated_elements(lst, expected):
    assert sum_squares(lst) == expected

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, -1, 1, -1], 0),
        ([-1, 1, -1, 1], 0),
    ],
)
def test_sum_squares_alternating_signs(lst, expected):
    assert sum_squares(lst) == expected

@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 153),
        ([1,2,3,4,5,6,7,8,9,10,11,12], 738),
    ]
)
def test_sum_squares_larger_lists(lst, expected):
    assert sum_squares(lst) == expected
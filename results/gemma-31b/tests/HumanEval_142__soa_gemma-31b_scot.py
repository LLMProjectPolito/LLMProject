


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

def test_sum_squares_empty():
    """Test with an empty list."""
    assert sum_squares([]) == 0

def test_sum_squares_example_1():
    """Test with the first provided example: [1, 2, 3]."""
    # idx 0: 1^2 = 1
    # idx 1: 2
    # idx 2: 3
    # Sum: 1 + 2 + 3 = 6
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_example_3():
    """Test with the third provided example: [-1, -5, 2, -1, -5]."""
    # idx 0: (-1)^2 = 1
    # idx 1: -5
    # idx 2: 2
    # idx 3: (-1)^2 = 1
    # idx 4: (-5)^3 = -125
    # Sum: 1 - 5 + 2 + 1 - 125 = -126
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """Test with a single element (index 0 is a multiple of 3)."""
    assert sum_squares([2]) == 4  # 2^2
    assert sum_squares([-3]) == 9 # (-3)^2

def test_sum_squares_index_4_logic():
    """Test that index 4 is cubed and not squared."""
    # idx 0: 0^2 = 0
    # idx 1: 0
    # idx 2: 0
    # idx 3: 0^2 = 0
    # idx 4: 2^3 = 8
    assert sum_squares([0, 0, 0, 0, 2]) == 8

def test_sum_squares_index_12_logic():
    """Test that index 12 (multiple of both 3 and 4) is squared, not cubed."""
    # Create list of 13 zeros, last element is 2
    lst = [0] * 12 + [2]
    # idx 12 is multiple of 3 -> 2^2 = 4
    assert sum_squares(lst) == 4

def test_sum_squares_zeros():
    """Test with a list of zeros."""
    assert sum_squares([0, 0, 0, 0, 0, 0]) == 0

@pytest.mark.parametrize("lst, expected", [
    ([2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2], 42),
    # idx 0: 2^2=4
    # idx 1: 1
    # idx 2: 1
    # idx 3: 2^2=4
    # idx 4: 2^3=8
    # idx 5: 1
    # idx 6: 2^2=4
    # idx 7: 1
    # idx 8: 2^3=8
    # idx 9: 2^2=4
    # idx 10: 1
    # idx 11: 1
    # idx 12: 2^2=4
    # Total: 4+1+1+4+8+1+4+1+8+4+1+1+4 = 42
])
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected

def test_sum_squares_negative_cubes():
    """Test that negative numbers at index 4, 8 etc are cubed correctly."""
    # idx 0: (-2)^2 = 4
    # idx 1: 0
    # idx 2: 0
    # idx 3: 0^2 = 0
    # idx 4: (-2)^3 = -8
    assert sum_squares([-2, 0, 0, 0, -2]) == -4
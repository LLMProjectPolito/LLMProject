


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
    ([], 0),                                # Empty list
    ([1, 2, 3], 6),                        # Example 1: 1^2 + 2 + 3 = 6
    ([-1, -5, 2, -1, -5], -126),           # Example 3: (-1)^2 + (-5) + 2 + (-1)^2 + (-5)^3 = 1-5+2+1-125 = -126
])
def test_sum_squares_basic_examples(lst, expected):
    """Test the function with basic examples provided in the requirements."""
    assert sum_squares(lst) == expected

@pytest.mark.parametrize("lst, expected", [
    ([2], 4),      # 2^2 = 4
    ([-3], 9),     # (-3)^2 = 9
    ([0], 0),      # 0^2 = 0
])
def test_sum_squares_index_zero(lst, expected):
    """Verify that index 0 is treated as a multiple of 3 and squared."""
    assert sum_squares(lst) == expected

@pytest.mark.parametrize("lst, expected", [
    ([2, 2, 2, 2, 2], 20), 
    # idx 0: 2^2=4, idx 1: 2, idx 2: 2, idx 3: 2^2=4, idx 4: 2^3=8 -> 4+2+2+4+8 = 20
    
    ([1, 1, 1, 1, 2, 1, 1, 1, 2], 23),
    # idx 0: 1^2=1, 1: 1, 2: 1, 3: 1^2=1, 4: 2^3=8, 5: 1, 6: 1^2=1, 7: 1, 8: 2^3=8 -> 1+1+1+1+8+1+1+1+8 = 23
    
    ([1] * 12 + [3], 21),
    # idx 0, 3, 6, 9, 12 are squared: 1^2, 1^2, 1^2, 1^2, 3^2 = 13
    # idx 4, 8 are cubed: 1^3, 1^3 = 2
    # idx 1, 2, 5, 7, 10, 11 are unchanged: 6 * 1 = 6
    # Total: 13 + 2 + 6 = 21
])
def test_sum_squares_logic_rules(lst, expected):
    """Verify the priority of index rules: Multiple of 3 (sq) > Multiple of 4 (cb) > None."""
    assert sum_squares(lst) == expected

@pytest.mark.parametrize("lst, expected", [
    ([0, 0, 0, 0, 0], 0),                  # All zeros
    ([2, 1, 1, 2, -2], 2),                 # Negative cubed: 2^2 + 1 + 1 + 2^2 + (-2)^3 = 4+1+1+4-8 = 2
    ([-2, 0, 0, 0, -2], -4),               # Negative sq and cb: (-2)^2 + 0 + 0 + 0 + (-2)^3 = 4 - 8 = -4
])
def test_sum_squares_mathematical_properties(lst, expected):
    """Ensure correct handling of zeros and negative numbers during power operations."""
    assert sum_squares(lst) == expected

@pytest.mark.parametrize("lst, expected", [
    ([100, 0, 0, 0, 10], 11000),           # 100^2 + 0 + 0 + 0 + 10^3 = 10000 + 1000 = 11000
    ([10, 10, 10, 10, 10], 1220),          # 10^2 + 10 + 10 + 10^2 + 10^3 = 100 + 10 + 10 + 100 + 1000 = 1220
])
def test_sum_squares_large_values(lst, expected):
    """Test with larger integers to ensure stability."""
    assert sum_squares(lst) == expected
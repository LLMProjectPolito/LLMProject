


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

def test_docstring_examples():
    """Test the examples provided in the function docstring."""
    assert sum_squares([1, 2, 3]) == 6  # idx 0: 1^2=1; idx 1: 2; idx 2: 3 -> 1+2+3=6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126 
    # idx 0: (-1)^2=1; idx 1: -5; idx 2: 2; idx 3: (-1)^2=1; idx 4: (-5)^3=-125 
    # Sum: 1 - 5 + 2 + 1 - 125 = -126

def test_empty_list():
    """Ensure an empty list returns 0."""
    assert sum_squares([]) == 0

def test_index_zero():
    """Index 0 is a multiple of 3, so it should be squared."""
    # [2] -> idx 0 is multiple of 3 -> 2^2 = 4
    assert sum_squares([2]) == 4
    # [-3] -> idx 0 is multiple of 3 -> (-3)^2 = 9
    assert sum_squares([-3]) == 9

def test_multiple_of_3_logic():
    """Test that indices 3, 6, 9 are squared."""
    # Indices: 0(sq), 1, 2, 3(sq), 4(cu), 5, 6(sq)
    # Values:  2,    1, 1, 2,    1,    1, 2
    # Result:  4 + 1 + 1 + 4 + 1 + 1 + 4 = 16
    lst = [2, 1, 1, 2, 1, 1, 2]
    assert sum_squares(lst) == 16

def test_multiple_of_4_logic():
    """Test that indices 4, 8 are cubed (and not multiples of 3)."""
    # Indices: 0(sq), 1, 2, 3(sq), 4(cu)
    # Values:  1,    1, 1, 1,    2
    # Result:  1^2 + 1 + 1 + 1^2 + 2^3 = 1 + 1 + 1 + 1 + 8 = 12
    lst = [1, 1, 1, 1, 2]
    assert sum_squares(lst) == 12

def test_precedence_12():
    """Index 12 is a multiple of both 3 and 4. It should be squared."""
    # Create a list of 13 elements (0 to 12)
    # All elements = 1 except index 12 = 2
    lst = [1] * 12 + [2]
    # Indices 0, 3, 6, 9 are squared: 1^2 * 4 = 4
    # Indices 4, 8 are cubed: 1^3 * 2 = 2
    # Indices 1, 2, 5, 7, 10, 11 are unchanged: 1 * 6 = 6
    # Index 12 is multiple of 3 -> squared: 2^2 = 4
    # Total: 4 + 2 + 6 + 4 = 16
    assert sum_squares(lst) == 16

def test_no_modification():
    """Test that indices not divisible by 3 or 4 remain unchanged."""
    # Indices: 0(sq), 1, 2
    # Values:  1,    5, 5
    # Result:  1^2 + 5 + 5 = 11
    assert sum_squares([1, 5, 5]) == 11

def test_negative_integers():
    """Verify that negative numbers are handled correctly by powers."""
    # Index 0: -2 -> (-2)^2 = 4
    # Index 1: -2 -> -2
    # Index 2: -2 -> -2
    # Index 3: -2 -> (-2)^2 = 4
    # Index 4: -2 -> (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4

@pytest.mark.parametrize("input_lst, expected", [
    ([0, 0, 0, 0, 0], 0),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1], 9), # 0(1), 1(1), 2(1), 3(1), 4(1), 5(1), 6(1), 7(1), 8(1) -> all 1s
])
def test_parameterized_cases(input_lst, expected):
    """General cases using parametrization."""
    assert sum_squares(input_lst) == expected
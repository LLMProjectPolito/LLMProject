


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

def test_empty_list():
    """Verify that an empty list returns 0."""
    assert sum_squares([]) == 0

@pytest.mark.parametrize("input_lst, expected_output", [
    ([1, 2, 3], 6),
    ([-1, -5, 2, -1, -5], -126),
])
def test_provided_examples(input_lst, expected_output):
    """Verify the examples provided in the docstring."""
    assert sum_squares(input_lst) == expected_output

def test_index_zero_is_squared():
    """Verify index 0 is squared (0 is a multiple of 3)."""
    # Index 0: 3^2 = 9. Sum = 9.
    assert sum_squares([3]) == 9

def test_index_four_is_cubed():
    """Verify index 4 is cubed (multiple of 4 and not 3)."""
    # Indices: 0(sq), 1(no), 2(no), 3(sq), 4(cube)
    # Values:  0,    0,    0,    0,    2
    # Result:  0,    0,    0,    0,    8
    assert sum_squares([0, 0, 0, 0, 2]) == 8

def test_index_twelve_priority():
    """Verify index 12 is squared (Rule 1) and not cubed (Rule 2)."""
    # Index 12 is a multiple of both 3 and 4. 
    # Rule 1 (multiple of 3) should take precedence.
    # 2^2 = 4; 2^3 = 8.
    lst = [0] * 12 + [2]
    assert sum_squares(lst) == 4

def test_negative_numbers():
    """Verify mathematical correctness with negative integers."""
    # Indices: 0(sq), 1(no), 2(no), 3(sq), 4(cube)
    # Values:  -2,   -2,   -2,   -2,   -2
    # Result:  4,    -2,   -2,   4,    -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert sum_squares([-2, -2, -2, -2, -2]) == -4

def test_large_numbers():
    """Verify handling of large integer values."""
    val = 10**6
    # Index 0: (10^6)^2 = 10^12
    # Index 1: 10^6
    # Index 2: 10^6
    # Sum: 1,000,002,000,000
    assert sum_squares([val, val, val]) == (val**2 + 2 * val)

def test_comprehensive_logic():
    """Verify a sequence covering all rules and index types."""
    # Indices: 0(sq), 1(no), 2(no), 3(sq), 4(cube), 5(no), 6(sq), 7(no), 8(cube), 9(sq), 10(no), 11(no), 12(sq)
    # Values:  2,    2,    2,    2,    2,    2,    2,    2,    2,    2,    2,    2,    2
    # Calc:    4,    2,    2,    4,    8,    2,    4,    2,    8,    4,    2,    2,    4
    # Sum: 4+2+2+4+8+2+4+2+8+4+2+2+4 = 48
    lst = [2] * 13
    assert sum_squares(lst) == 48

def test_no_side_effects():
    """Ensure the function does not mutate the original input list."""
    original = [1, 2, 3, 4, 5]
    original_copy = list(original)
    sum_squares(original)
    assert original == original_copy, "The function mutated the input list!"

def test_all_zeros():
    """Verify that a list of zeros returns zero."""
    assert sum_squares([0, 0, 0, 0]) == 0
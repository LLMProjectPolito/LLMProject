


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

@pytest.mark.parametrize("input_lst, expected", [
    ([], 0),              # Empty list
    ([5], 25),            # Single element (index 0: 5^2)
    ([0, 0, 0, 0], 0),    # All zeros
])
def test_edge_cases(input_lst, expected):
    """Verifies behavior for boundary inputs like empty, single, or zero-filled lists."""
    assert sum_squares(input_lst) == expected

@pytest.mark.parametrize("scenario, input_lst, expected", [
    ("identity", [0, 10, 20, 0, 0, 30], 60),
    ("square", [2, 1, 1, 3, 1, 1, 4], 33),
    ("cube", [2, 1, 1, 2, 3], 37),
    ("precedence_rule", [0]*12 + [2], 4),  # Index 12 is multiple of 3 and 4; must square (2^2=4)
    ("full_sequence_stress", [10]*13, 2560), # Comprehensive check of all branches up to index 12
])
def test_logic_branches(scenario, input_lst, expected):
    """
    Tests specific transformation rules:
    - Identity: Indices not divisible by 3 or 4.
    - Square: Indices divisible by 3.
    - Cube: Indices divisible by 4 (but not 3).
    - Precedence: Ensures index 12 is squared, not cubed.
    """
    assert sum_squares(input_lst) == expected

@pytest.mark.parametrize("scenario, input_lst, expected", [
    ("simple_negatives", [-2, -2, -2, -2, -2], -4),
    ("complex_negatives", [-2, -3, 0, -4, -5], -108),
    ("large_integers", [10**6, 10**6], 1000001000000),
])
def test_mathematical_robustness(scenario, input_lst, expected):
    """Verifies mathematical correctness with negative numbers and large integers."""
    assert sum_squares(input_lst) == expected

@pytest.mark.parametrize("input_lst, expected", [
    ([1, 2, 3], 6),
    ([], 0),
    ([-1, -5, 2, -1, -5], -126),
])
def test_docstring_examples(input_lst, expected):
    """Validates the function against the specific examples provided in the docstring."""
    assert sum_squares(input_lst) == expected
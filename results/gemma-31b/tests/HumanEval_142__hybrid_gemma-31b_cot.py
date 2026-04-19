


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
    ([], 0),                   # Empty list
    ([0], 0),                  # Single zero
    ([0, 0, 0, 0, 0], 0),      # Multiple zeros
])
def test_sum_squares_zeros_and_empty(lst, expected):
    """Test that empty lists and lists of zeros return 0."""
    assert sum_squares(lst) == expected

@pytest.mark.parametrize("lst, expected", [
    ([5], 25),                 # Index 0: 5^2 = 25
    ([-2], 4),                 # Index 0: (-2)^2 = 4
])
def test_sum_squares_single_element(lst, expected):
    """Test a single element (index 0 is always a multiple of 3)."""
    assert sum_squares(lst) == expected

def test_sum_squares_provided_examples():
    """Verify the examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

@pytest.mark.parametrize("lst, expected", [
    ([2], 4),               # Index 0: 2^2 = 4
    ([2, 3], 7),            # Index 0: 4, Index 1: 3 -> 7
    ([2, 3, 4], 11),        # Index 0: 4, Index 1: 3, Index 2: 4 -> 11
    ([2, 3, 4, 5], 36),     # Index 0: 4, Index 1: 3, Index 2: 4, Index 3: 5^2=25 -> 36
    ([2, 3, 4, 5, 6], 252), # Index 0: 4, Index 1: 3, Index 2: 4, Index 3: 25, Index 4: 6^3=216 -> 252
])
def test_sum_squares_small_lists(lst, expected):
    """Test various small list lengths to verify boundary conditions for indices 0, 3, and 4."""
    assert sum_squares(lst) == expected

def test_sum_squares_index_priority():
    """
    Verify that indices which are multiples of both 3 and 4 (e.g., index 12) 
    are squared, not cubed, as per the requirement 'multiple of 3' priority.
    """
    # Create a list of length 13 (indices 0 to 12)
    # We use 0s for most elements to isolate index 12
    lst = [0] * 13
    lst[12] = 2
    # Index 12 is a multiple of 3 and 4. 
    # Rule: if index % 3 == 0 -> square. 2^2 = 4.
    assert sum_squares(lst) == 4

@pytest.mark.parametrize("lst, expected", [
    ([-2, -2, -2, -2, -2], -4), # 0:4, 1:-2, 2:-2, 3:4, 4:-8 -> Sum: -4
    ([-2, 1, 1, -2, -2], 2),    # 0:4, 1:1, 2:1, 3:4, 4:-8 -> Sum: 2
])
def test_sum_squares_negative_logic(lst, expected):
    """Test negative numbers specifically for squaring (positive) and cubing (negative)."""
    assert sum_squares(lst) == expected

def test_sum_squares_complex_sequence():
    """Test a longer sequence to ensure all logic branches are hit repeatedly."""
    # Indices: 0(S), 1(N), 2(N), 3(S), 4(C), 5(N), 6(S), 7(N), 8(C), 9(S), 10(N), 11(N), 12(S)
    # S = Square, C = Cube, N = No change
    lst = [2] * 13 
    # Squares: idx 0, 3, 6, 9, 12 (5 elements) -> 5 * (2^2) = 20
    # Cubes: idx 4, 8 (2 elements) -> 2 * (2^3) = 16
    # Same: idx 1, 2, 5, 7, 10, 11 (6 elements) -> 6 * 2 = 12
    # Total: 20 + 16 + 12 = 48
    assert sum_squares(lst) == 48

def test_sum_squares_large_numbers():
    """Test with larger integers to ensure no overflow issues."""
    # Indices: 0(sq), 1(as-is), 2(as-is), 3(sq), 4(cube)
    # Values: 100, 100, 100, 100, 100
    # Calc: 100^2 + 100 + 100 + 100^2 + 100^3 = 10000 + 100 + 100 + 10000 + 1000000 = 1020200
    lst = [100] * 5 
    assert sum_squares(lst) == 1020200



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

def test_sum_squares_provided_examples():
    """Tests the examples provided in the docstring."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_single_element():
    """
    Tests a single element list. 
    Index 0 is a multiple of 3, so it should be squared.
    """
    assert sum_squares([2]) == 4  # 2^2
    assert sum_squares([-3]) == 9 # (-3)^2
    assert sum_squares([0]) == 0  # 0^2

def test_sum_squares_index_logic():
    """
    Tests specific index rules:
    - Index 0: Multiple of 3 -> Square
    - Index 3: Multiple of 3 -> Square
    - Index 4: Multiple of 4 (not 3) -> Cube
    - Index 12: Multiple of 3 and 4 -> Square (priority to 3)
    """
    # Index 0: 2^2=4; Index 1: 1; Index 2: 1; Index 3: 2^2=4; Index 4: 2^3=8
    # Sum: 4 + 1 + 1 + 4 + 8 = 18
    assert sum_squares([2, 1, 1, 2, 2]) == 18

def test_sum_squares_overlap_3_and_4():
    """
    Tests index 12, which is a multiple of both 3 and 4.
    According to the rules, it should be squared because it is a multiple of 3.
    """
    # Create a list of 13 zeros, with the last element being 2
    lst = [0] * 12 + [2] 
    # Index 12 is a multiple of 3 -> 2^2 = 4
    assert sum_squares(lst) == 4

def test_sum_squares_no_multiples():
    """Tests a list where indices 1, 2, 5, 7 etc. remain unchanged."""
    # Index 0: 2^2=4; Index 1: 10; Index 2: 10
    assert sum_squares([2, 10, 10]) == 24

def test_sum_squares_negative_numbers():
    """Tests how negative numbers are handled by squaring and cubing."""
    # Index 0: (-2)^2 = 4
    # Index 1: -1
    # Index 2: -1
    # Index 3: (-2)^2 = 4
    # Index 4: (-2)^3 = -8
    # Sum: 4 - 1 - 1 + 4 - 8 = -2
    assert sum_squares([-2, -1, -1, -2, -2]) == -2

def test_sum_squares_floats():
    """Tests that the function handles floating-point numbers correctly."""
    # Index 0: 1.5^2 = 2.25
    assert sum_squares([1.5]) == 2.25
    # Index 0: 1.0^2=1; Index 1: 2.0; Index 2: 3.0; Index 3: 2.0^2=4; Index 4: 2.0^3=8
    # Sum: 1 + 2 + 3 + 4 + 8 = 18.0
    assert sum_squares([1.0, 2.0, 3.0, 2.0, 2.0]) == 18.0

def test_sum_squares_large_values():
    """Tests the function with large integers to ensure precision/performance."""
    large_val = 10**6
    # Index 0: (10^6)^2 = 10^12
    assert sum_squares([large_val]) == 10**12

def test_sum_squares_invalid_types():
    """Tests that the function handles invalid input types gracefully."""
    # Test passing None instead of a list
    with pytest.raises(TypeError):
        sum_squares(None)
    
    # Test passing a string instead of a list
    with pytest.raises(TypeError):
        sum_squares("not a list")
        
    # Test passing a list containing invalid types (e.g., strings)
    with pytest.raises(TypeError):
        sum_squares([1, "two", 3])
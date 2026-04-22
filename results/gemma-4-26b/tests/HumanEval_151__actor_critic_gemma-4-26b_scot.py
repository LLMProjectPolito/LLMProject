
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''

import pytest

def test_docstring_examples():
    """Verifies the specific examples provided in the function docstring."""
    # Corrected notation from ^ to **
    assert double_the_difference([1, 3, 2, 0]) == 10  # 1**2 + 3**2
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81       # 9**2
    assert double_the_difference([0]) == 0

def test_empty_list():
    """Tests that an empty list returns 0."""
    assert double_the_difference([]) == 0

@pytest.mark.parametrize("input_list, expected", [
    ([1, 3, 5], 35),            # Positive odds: 1 + 9 + 25
    ([2, 4, 6], 0),             # Positive evens
    ([-1, -3, -5], 0),          # Negative odds
    ([-2, -4, -6], 0),          # Negative evens
    ([0, 2, 4], 0),             # Zero and evens
    ([1, 1, 1], 3),             # Duplicate valid integers
    ([1, 3, 5, 7], 84),         # Larger set of positive odds
])
def test_filtering_logic(input_list, expected):
    """
    Ensures only positive odd integers are squared and summed.
    Note: The function name 'double_the_difference' is a semantic mismatch 
    for this logic, but tests follow the actual implementation requirements.
    """
    assert double_the_difference(input_list) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([1.0, 3.0, 5.0], 0),       # Floats are not integers
    ([1, 3.5, 5], 26),          # Mixed: 1**2 + 5**2
    ([None, "1", "apple"], 0),  # Non-numeric types
    ([True, 3], 9),             # Booleans should be ignored (not treated as 1)
    ([False, 1], 1),            # Booleans should be ignored (not treated as 0)
    ([1, "3", None, True], 1),  # Mixed: only 1 is a strict positive odd integer
])
def test_type_safety(input_list, expected):
    """
    Tests robustness against non-integer types.
    Ensures booleans and floats are not treated as valid integers.
    """
    assert double_the_difference(input_list) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([float('inf'), 3, float('nan')], 9), # inf and nan should be ignored
    ([float('-inf'), 1], 1),              # -inf should be ignored
])
def test_special_floats(input_list, expected):
    """Tests that special float values do not crash the function and are ignored."""
    assert double_the_difference(input_list) == expected

@pytest.mark.parametrize("non_iterable", [
    None,
    123,
    45.6,
    True
])
def test_non_iterable_input(non_iterable):
    """Tests that passing a non-iterable input raises a TypeError."""
    with pytest.raises(TypeError):
        double_the_difference(non_iterable)

def test_large_values():
    """Tests the function with very large integers to ensure correctness."""
    large_odd = 10**15 + 1
    expected = large_odd**2
    assert double_the_difference([large_odd]) == expected
    assert double_the_difference([large_odd, 2, -large_odd]) == expected
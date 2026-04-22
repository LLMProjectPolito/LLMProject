


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

def transform_and_sum(lst):
    """
    Takes an iterable of numbers. 
    - Squares the element if its index is a multiple of 3.
    - Cubes the element if its index is a multiple of 4 and NOT a multiple of 3.
    - Returns the sum of all processed entries.
    """
    if lst is None:
        raise TypeError("Input must be an iterable, not None")
    
    total = 0
    for i, val in enumerate(lst):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Elements must be numeric, found {type(val).__name__}")
            
        if i % 3 == 0:
            total += val ** 2
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total

### Refined Tests (Pytest):

def test_transform_and_sum_empty():
    """Tests that an empty list returns 0."""
    assert transform_and_sum([]) == 0

def test_transform_and_sum_provided_examples():
    """Tests the specific examples provided in the docstring."""
    assert transform_and_sum([1, 2, 3]) == 6
    assert transform_and_sum([-1, -5, 2, -1, -5]) == -126

def test_transform_and_sum_multiples_of_3():
    """Tests that elements at indices 0, 3, 6, etc., are squared."""
    # idx 0: 2^2 = 4
    # idx 1: 2
    # idx 2: 2
    # idx 3: 2^2 = 4
    # Sum: 4 + 2 + 2 + 4 = 12
    assert transform_and_sum([2, 2, 2, 2]) == 12

def test_transform_and_sum_multiples_of_4_not_3():
    """Tests that elements at indices 4, 8, etc., are cubed (and not squared)."""
    # idx 0 (mult 3): 2^2 = 4
    # idx 1: 2
    # idx 2: 2
    # idx 3 (mult 3): 2^2 = 4
    # idx 4 (mult 4): 2^3 = 8
    # idx 5: 2
    # idx 6 (mult 3): 2^2 = 4
    # idx 7: 2
    # idx 8 (mult 4): 2^3 = 8
    # Sum: 4 + 2 + 2 + 4 + 8 + 2 + 4 + 2 + 8 = 36
    assert transform_and_sum([2] * 9) == 36

def test_transform_and_sum_overlap_logic():
    """Tests the priority rule: index 12 (mult of 3 and 4) should be squared."""
    # Indices: 0(sq), 1, 2, 3(sq), 4(cu), 5, 6(sq), 7, 8(cu), 9(sq), 10, 11, 12(sq)
    # Using 2s: 4+2+2+4+8+2+4+2+8+4+2+2+4 = 48
    lst = [2] * 13
    assert transform_and_sum(lst) == 48

def test_transform_and_sum_negatives():
    """Tests the function with negative integers."""
    # idx 0: (-2)^2 = 4
    # idx 1: -2
    # idx 2: -2
    # idx 3: (-2)^2 = 4
    # idx 4: (-2)^3 = -8
    # Sum: 4 - 2 - 2 + 4 - 8 = -4
    assert transform_and_sum([-2, -2, -2, -2, -2]) == -4

def test_transform_and_sum_floats():
    """Tests that the function handles floating-point numbers correctly."""
    # idx 0: 1.5^2 = 2.25
    # idx 1: 2.5
    # idx 2: 3.5
    # Sum: 2.25 + 2.5 + 3.5 = 8.25
    assert transform_and_sum([1.5, 2.5, 3.5]) == 8.25

def test_transform_and_sum_tuples():
    """Tests that the function accepts other iterables like tuples."""
    assert transform_and_sum((1, 2, 3)) == 6

def test_transform_and_sum_invalid_inputs():
    """Tests that the function raises appropriate errors for invalid inputs."""
    # Test None input
    with pytest.raises(TypeError):
        transform_and_sum(None)
    
    # Test string input (iterating over a string yields characters, which aren't numeric)
    with pytest.raises(TypeError):
        transform_and_sum("abc")

    # Test list containing non-numeric types
    with pytest.raises(TypeError):
        transform_and_sum([1, "two", 3])
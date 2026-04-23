


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
import math

def test_sum_squares_empty():
    """Test that an empty list returns 0."""
    assert sum_squares([]) == 0

@pytest.mark.parametrize("input_list, expected_output, description", [
    ([1, 2, 3], 6, "Docstring example 1: idx 0 squared (1), idx 1 (2), idx 2 (3). Sum: 1+2+3=6"),
    ([-1, -5, 2, -1, -5], -126, "Docstring example 2: idx 0 sq (1), idx 1 (-5), idx 2 (2), idx 3 sq (1), idx 4 cube (-125). Sum: -126"),
    ([2], 4, "Index 0 is a multiple of 3, should be squared (2^2=4)"),
    ([1, 1, 1, 2], 7, "Index 3 is a multiple of 3, should be squared (2^2=4). Sum: 1+1+1+4=7"),
    ([1, 1, 1, 1, 2], 12, "Index 4 is a multiple of 4 and not 3, should be cubed (2^3=8). Sum: 1+1+1+1+8=12"),
    ([1]*12 + [2], 16, "Index 12 is a multiple of 3 and 4, should be squared (2^2=4). Sum: 12*1 + 4 = 16"),
    ([1, 2], 3, "Index 1 is neither multiple of 3 nor 4, should remain 2. Sum: 1^2 + 2 = 3"),
])
def test_sum_squares_index_logic(input_list, expected_output, description):
    """Test the specific mathematical rules applied to different indices."""
    assert sum_squares(input_list) == expected_output

def test_sum_squares_zeros():
    """Test that a list of zeros returns 0."""
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_large_values():
    """Test with very large integers to ensure no unexpected behavior."""
    val = 10**6
    input_list = [val, val, val, val]
    expected = (val**2) + val + val + (val**2)
    assert sum_squares(input_list) == expected

def test_sum_squares_floats():
    """Test that floating-point numbers are handled correctly."""
    input_list = [1.1, 2.2, 3.3, 4.4]
    # idx 0: 1.1^2 = 1.21
    # idx 1: 2.2
    # idx 2: 3.3
    # idx 3: 4.4^2 = 19.36
    # Sum: 1.21 + 2.2 + 3.3 + 19.36 = 26.07
    assert sum_squares(input_list) == pytest.approx(26.07)

def test_sum_squares_non_finite():
    """Test how the function handles infinity and NaN."""
    assert sum_squares([float('inf'), 1]) == float('inf')
    assert math.isnan(sum_squares([float('nan'), 1]))

def test_sum_squares_other_iterables():
    """Test that the function works with various iterable types, not just lists."""
    # Tuple
    assert sum_squares((1, 2, 3)) == 6
    # Range
    # range(4) -> [0, 1, 2, 3]
    # idx 0: 0^2=0, idx 1: 1, idx 2: 2, idx 3: 3^2=9. Sum: 12
    assert sum_squares(range(4)) == 12
    # Generator
    gen = (x for x in [1, 2, 3])
    assert sum_squares(gen) == 6

@pytest.mark.parametrize("invalid_container", [
    None,
    123,
    "not an iterable",
])
def test_sum_squares_invalid_container(invalid_container):
    """Test that non-iterable containers raise a TypeError."""
    with pytest.raises(TypeError):
        sum_squares(invalid_container)

@pytest.mark.parametrize("invalid_elements", [
    [1, "two", 3],
    [1, None, 3],
    ["a", "b", "c"],
])
def test_sum_squares_invalid_elements(invalid_elements):
    """Test that iterables containing non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError):
        sum_squares(invalid_elements)

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# Assuming the function is in a file named solution.py
# from solution import even_odd_count

@pytest.mark.parametrize("num, expected", [
    # --- Happy Path: Positive Integers ---
    (123, (1, 2)),    # Example from docstring
    (246, (3, 0)),    # All even
    (135, (0, 3)),    # All odd
    (10, (1, 1)),     # Mixed with zero
    
    # --- Happy Path: Negative Integers ---
    (-12, (1, 1)),    # Example from docstring (ensures sign is ignored)
    (-444, (3, 0)),   # All even negative
    (-7, (0, 1)),     # Single digit negative odd
    (-2468, (4, 0)),  # Multi-digit negative even
    
    # --- Edge Case: Zero ---
    (0, (1, 0)),      # Zero is an even digit
    
    # --- Edge Case: Large Numbers ---
    (1000000000, (10, 0)), # Large number of even digits
    (9999999999, (0, 10)), # Large number of odd digits
    
    # --- Edge Case: Single Digits ---
    (1, (0, 1)),
    (2, (1, 0)),
    (8, (1, 0)),
    (9, (0, 1)),
])
def test_even_odd_count_logic(num, expected):
    """Tests standard logic, negative numbers, and zero."""
    assert even_odd_count(num) == expected

def test_even_odd_count_type_safety():
    """
    Tests how the function handles non-integer inputs.
    A robust implementation should ideally raise a TypeError 
    if the input is not an integer.
    """
    with pytest.raises(TypeError):
        even_odd_count("123")  # String input
        
    with pytest.raises(TypeError):
        even_odd_count(12.3)   # Float input
        
    with pytest.raises(TypeError):
        even_odd_count(None)   # None input

def test_even_odd_count_extreme_values():
    """Tests behavior with extremely large integers (Python handles arbitrary precision)."""
    large_num = 2**64
    # 2**64 is 18446744073709551616
    # Let's manually count or just ensure it doesn't crash and returns a tuple
    result = even_odd_count(large_num)
    assert isinstance(result, tuple)
    assert len(result) == 2
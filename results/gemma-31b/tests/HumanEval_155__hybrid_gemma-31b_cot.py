
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    # Edge Case: Zero
    (0, (1, 0)),
    (-0, (1, 0)),
    
    # Single digit numbers (Positive & Negative)
    (1, (0, 1)),
    (2, (1, 0)),
    (9, (0, 1)),
    (8, (1, 0)),
    (-1, (0, 1)),
    (-2, (1, 0)),
    (-9, (0, 1)),
    (-8, (1, 0)),
    
    # Basic mixed cases (Positive & Negative)
    (123, (1, 2)),
    (456, (2, 1)),
    (123456, (3, 3)),
    (-12, (1, 1)),
    (-123, (1, 2)),
    (-456, (2, 1)),
    
    # Numbers with all even digits
    (2468, (4, 0)),
    (-2046, (4, 0)),
    (888, (3, 0)),
    (2000, (4, 0)),
    (2222222222, (10, 0)),
    
    # Numbers with all odd digits
    (13579, (0, 5)),
    (-135, (0, 3)),
    (777, (0, 3)),
    (1111111111, (0, 10)),
    
    # Mixed digits including zeros
    (10203, (3, 2)),    # 0, 2, 0 are even; 1, 3 are odd
    (-1010, (2, 2)),    # 0, 0 are even; 1, 1 are odd
    (1000000000, (9, 1)), # nine 0s (even), one 1 (odd)
    
    # Large numbers
    (1234567890, (5, 5)),
    (-9876543210, (5, 5)),
    (1111122222, (5, 5)),
])
def test_even_odd_count_logic(num, expected):
    """
    Comprehensive test for even_odd_count covering zero, single digits, 
    all-even, all-odd, mixed, and large integers.
    """
    assert even_odd_count(num) == expected

def test_even_odd_count_type_integrity():
    """
    Ensure the function always returns a tuple of exactly two integers.
    """
    test_inputs = [0, -123, 456, 10**10]
    for val in test_inputs:
        result = even_odd_count(val)
        assert isinstance(result, tuple), f"Expected tuple for input {val}, got {type(result)}"
        assert len(result) == 2, f"Expected tuple length 2 for input {val}, got {len(result)}"
        assert all(isinstance(i, int) for i in result), f"Expected tuple elements to be ints for input {val}"

def test_extremely_large_integer():
    """
    Verify the function handles very large integers (beyond standard 64-bit) correctly.
    """
    # 100 ones and 100 twos
    large_num = int('1' * 100 + '2' * 100)
    assert even_odd_count(large_num) == (100, 100)
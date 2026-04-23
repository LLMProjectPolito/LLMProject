
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert to absolute value to handle negative signs, then to string to iterate over digits
    digits = str(abs(num))
    even_count = 0
    odd_count = 0
    
    for digit in digits:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return (even_count, odd_count)

@pytest.mark.parametrize("num, expected", [
    # Provided examples
    (123, (1, 2)),
    (-12, (1, 1)),
    
    # Single digit cases
    (0, (1, 0)),    # 0 is even
    (2, (1, 0)),    # Even
    (8, (1, 0)),    # Even
    (1, (0, 1)),    # Odd
    (7, (0, 1)),    # Odd
    (9, (0, 1)),    # Odd
    
    # Negative numbers
    (-5, (0, 1)),
    (-246, (3, 0)),
    (-1357, (0, 4)),
    
    # All even digits
    (2468, (4, 0)),
    
    # All odd digits
    (13579, (0, 5)),
    
    # Mixed digits
    (1024, (3, 1)), # 0, 2, 4 are even; 1 is odd
    (98765, (2, 3)), # 8, 6 are even; 9, 7, 5 are odd
    
    # Large numbers
    (1234567890, (5, 5)),
    (1000000000, (9, 1)), # Nine 0s (even), one 1 (odd)
    (10**100, (100, 1)),  # 1 followed by 100 zeros (Python arbitrary-precision)
])
def test_even_odd_count(num, expected):
    """Tests various integer inputs including positive, negative, zero, and large numbers."""
    assert even_odd_count(num) == expected

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    1.5,
])
def test_invalid_types(invalid_input):
    """Tests how the function handles non-integer inputs (e.g., float, str, or None)."""
    # abs(None) or abs("str") raises TypeError; int(".") for floats raises ValueError
    with pytest.raises((TypeError, ValueError)):
        even_odd_count(invalid_input)
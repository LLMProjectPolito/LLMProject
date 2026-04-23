
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

# Note: specialFilter implementation is assumed to be imported or defined above

def test_special_filter_docstring_examples():
    """Sanity check: Ensures the function meets the provided docstring requirements."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_edge_cases():
    """Tests fundamental edge cases: empty lists, negatives, and the magnitude boundary."""
    assert specialFilter([]) == 0
    # Negatives are excluded because they are not > 10
    assert specialFilter([-11, -13, -15, -31, -33]) == 0
    # Numbers <= 10 are excluded even if digits are odd
    assert specialFilter([1, 3, 5, 7, 9]) == 0
    assert specialFilter([10]) == 0
    # The first valid number > 10 with odd digits
    assert specialFilter([11]) == 1

@pytest.mark.parametrize("nums, expected", [
    # --- Digit Parity Logic ---
    ([22, 44, 66, 88], 0),          # Both digits even
    ([21, 43, 87, 65], 0),          # First digit even, last digit odd
    ([12, 34, 56, 78], 0),          # First digit odd, last digit even
    ([13, 35, 57, 79], 4),          # Both digits odd (Valid)
    
    # --- Multi-digit / Large Number Logic ---
    ([101, 303, 505, 707, 909], 5), # Large numbers, all valid (1/odd, last/odd)
    ([1001, 1003, 1002, 1004], 2),  # Multi-digit check (1001 and 1003 are valid)
    ([13579, 33333, 24680], 2),     # Large numbers (13579 and 33333 are valid)
    
    # --- Mixed Complexity ---
    ([11, 13, 15, 12, 14, 16], 3),  # Mixed valid and even-ending
    ([11, 22, 33, 44, 55], 3),      # Alternating valid/invalid
    ([13, 24, 35, 46, 57, 68, 79, 80], 4), # Mixed valid and even-ending
])
def test_special_filter_logic_combinations(nums, expected):
    """
    Comprehensive parameterization covering:
    1. First digit even/odd
    2. Last digit even/odd
    3. Multi-digit parity (e.g., 1001)
    4. Large number constraints
    """
    assert specialFilter(nums) == expected
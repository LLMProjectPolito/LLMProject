
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

def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    '''
    total = 0
    for x in lst:
        # Filter for integers only (excluding booleans), then non-negative, then odd
        if isinstance(x, int) and not isinstance(x, bool):
            if x >= 0 and x % 2 != 0:
                total += x**2
    return total

class TestDoubleTheDifference:
    """Superior test suite merging functional, edge, and type-stability cases."""

    @pytest.mark.parametrize("input_list, expected", [
        # Standard cases
        ([1, 3, 2, 0], 10),           # 1^2 + 3^2 = 10
        ([-1, -2, 0], 0),             # Negatives and zero ignored
        ([9, -2], 81),                # 9^2 = 81
        ([0], 0),                     # Zero is even
        ([], 0),                      # Empty list
        ([1, 3, 5], 35),              # 1 + 9 + 25 = 35
        ([2, 4, 6, 8, 10], 0),        # All even positive integers
        ([-1, -3, -5, -2, -4], 0),    # All negative numbers
        
        # Type handling (Ignore non-integers)
        ([1, 2.5, 3], 10),            # Float ignored
        ([1, "3", 5], 26),            # String ignored
        ([7, None, 3], 58),           # None ignored
        ([1.0, 3.0, 5.5, 2.1], 0),    # Floats that look like ints ignored
        ([True, 1, 3], 10),           # Booleans ignored (True is 1, but not strictly int)
        ([1, "3", None, 3, True, False], 10), # Mixed types: 1^2 + 3^2
        
        # Large numbers and mixed valid/invalid
        ([101], 10201),               # 101^2
        ([101, 103], 20810),          # 10201 + 10609
        ([7, -7, 2.0, 11, "hello", -3], 170), # 7^2 + 11^2 = 49 + 121 = 170
    ])
    def test_functional_cases(self, input_list, expected):
        """Test a wide range of functional inputs including types and edge cases."""
        assert double_the_difference(input_list) == expected

    def test_all_invalid_input(self):
        """Test list containing only invalid elements to ensure it returns 0."""
        assert double_the_difference(["a", "b", 2.2, -1, -3, None, False]) == 0

    def test_mixed_extreme_cases(self):
        """Test a comprehensive mix of all conditions in one list."""
        # 1^2 + 7^2 = 1 + 49 = 50
        mixed_list = [1, -1, 2, -2, 7, 8, -8, 3.14, "odd", None, 0, True]
        assert double_the_difference(mixed_list) == 50

    def test_type_stability(self):
        """Ensure the function consistently returns an integer."""
        assert isinstance(double_the_difference([]), int)
        assert isinstance(double_the_difference([1.1, 2.2]), int)
        assert isinstance(double_the_difference(["a", None]), int)
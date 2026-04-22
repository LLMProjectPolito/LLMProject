


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

def sum_squares(lst):
    """
    Calculates the sum of a list of integers based on index-based transformations:
    - If the index is a multiple of 3, the element is squared.
    - If the index is a multiple of 4 and NOT a multiple of 3, the element is cubed.
    - Otherwise, the element remains unchanged.
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val ** 2
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total

class TestSumSquares:
    """Superior test suite for sum_squares covering edge cases, logic precedence, and mathematical properties."""

    @pytest.mark.parametrize("lst, expected", [
        ([], 0),                                     # Empty list
        ([5], 25),                                   # Single element (index 0 is multiple of 3)
        ([0, 0, 0, 0, 0], 0),                        # List of zeros
        ([1, 2, 3], 6),                              # Small list: [1^2, 2, 3]
        ([1, 1, 1, 1], 4),                           # Identical elements: [1^2, 1, 1, 1^2]
        ([-1, -5, 2, -1, -5], -126),                 # Mixed signs: [(-1)^2, -5, 2, (-1)^2, (-5)^3]
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 1231), # Complex sequence
    ])
    def test_standard_scenarios(self, lst, expected):
        """Tests various input scenarios including empty, small, and mixed lists using parametrization."""
        assert sum_squares(lst) == expected

    def test_precedence_logic(self):
        """
        Verifies the specific requirement: 'cube ... if its index is a multiple of 4 AND NOT a multiple of 3'.
        Index 12 is a multiple of both 3 and 4; it must be squared (3-rule) rather than cubed (4-rule).
        """
        # Input: 13 elements of value 2
        # idx 0 (sq): 4 | idx 1: 2 | idx 2: 2 | idx 3 (sq): 4 | idx 4 (cube): 8 | idx 5: 2
        # idx 6 (sq): 4 | idx 7: 2 | idx 8 (cube): 8 | idx 9 (sq): 4 | idx 10: 2 | idx 11: 2
        # idx 12 (sq): 4
        # Sum: 4+2+2+4+8+2+4+2+8+4+2+2+4 = 48
        lst = [2] * 13
        assert sum_squares(lst) == 48

    def test_negative_number_behavior(self):
        """Ensures squaring results in positive numbers and cubing preserves the negative sign."""
        # idx 0 (sq): (-2)^2 = 4
        # idx 1 (same): -2
        # idx 2 (same): -2
        # idx 3 (sq): (-2)^2 = 4
        # idx 4 (cube): (-2)^3 = -8
        # idx 5 (same): -2
        # idx 6 (sq): (-2)^2 = 4
        # idx 7 (same): -2
        # Total: 4 - 2 - 2 + 4 - 8 - 2 + 4 - 2 = -4
        lst = [-2] * 8
        assert sum_squares(lst) == -4

    def test_large_integers(self):
        """Ensures the function handles larger integers correctly without precision loss."""
        # idx 0: 100^2 = 10000 | idx 1: 100 | idx 2: 100 | idx 3: 100^2 = 10000
        lst = [100, 100, 100, 100]
        assert sum_squares(lst) == 20200
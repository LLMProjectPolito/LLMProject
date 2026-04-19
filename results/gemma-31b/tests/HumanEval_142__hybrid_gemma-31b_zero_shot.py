


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
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    """
    total = 0
    for i in range(len(lst)):
        val = lst[i]
        if i % 3 == 0:
            total += val ** 2
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total

class TestSumSquares:
    """Comprehensive test suite for sum_squares function."""

    @pytest.mark.parametrize("lst, expected", [
        ([], 0),                                      # Empty list
        ([1, 2, 3], 6),                               # Example 1: 1^2 + 2 + 3 = 6
        ([-1, -5, 2, -1, -5], -126),                  # Example 2: 1 - 5 + 2 + 1 - 125 = -126
        ([2], 4),                                     # Single element: index 0 is mult of 3 -> 2^2 = 4
        ([0, 0, 0, 0, 0], 0),                         # All zeros
        ([1, 1, 1, 1, 1, 1, 1], 7),                   # All ones: 1+1+1+1+1+1+1 = 7
        ([2, 2, 2, 2, 2], 20),                        # 2^2 + 2 + 2 + 2^2 + 2^3 = 4+2+2+4+8 = 20
        ([2] * 6, 22),                                # 2^2 + 2 + 2 + 2^2 + 2^3 + 2 = 4+2+2+4+8+2 = 22
    ])
    def test_standard_cases(self, lst, expected):
        """Tests standard inputs, provided examples, and basic edge cases."""
        assert sum_squares(lst) == expected

    def test_index_priority(self):
        """
        Verify that indices that are multiples of both 3 and 4 (e.g., 0, 12) 
        are squared, not cubed, as per the 'if/elif' priority.
        """
        # Index 12: 2^2 = 4. If it were cubed, it would be 8.
        lst = [0] * 12 + [2]
        assert sum_squares(lst) == 4
        
        # Index 0: (-3)^2 = 9. If it were cubed, it would be -27.
        assert sum_squares([-3]) == 9

    def test_negative_numbers_and_signs(self):
        """Test that squaring removes negative signs and cubing preserves them."""
        # idx 0: (-2)^2 = 4
        # idx 1: -1 (id)
        # idx 2: -1 (id)
        # idx 3: (-2)^2 = 4
        # idx 4: (-2)^3 = -8
        # Total: 4 - 1 - 1 + 4 - 8 = -2
        lst = [-2, -1, -1, -2, -2]
        assert sum_squares(lst) == -2

    def test_no_modifications_needed(self):
        """Test indices that should remain unchanged (1, 2, 5, 7, 10, 11)."""
        # lst[0]: 1^2 = 1
        # lst[1]: 5 (id)
        # lst[2]: 5 (id)
        # lst[3]: 1^2 = 1
        # lst[4]: 1^3 = 1
        # lst[5]: 5 (id)
        # Total: 1 + 5 + 5 + 1 + 1 + 5 = 18
        lst = [1, 5, 5, 1, 1, 5]
        assert sum_squares(lst) == 18

    def test_large_integers(self):
        """Test with larger integers to ensure power operations are handled correctly."""
        # idx 0: 100^2 = 10000
        # idx 4: 10^3 = 1000
        # Others: 0
        lst = [100] + [0] * 3 + [10] + [0] * 100
        assert sum_squares(lst) == 11000
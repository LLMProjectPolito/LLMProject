


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

# Note: sum_squares is assumed to be imported from your source module

class TestSumSquares:
    """
    A comprehensive test suite for the sum_squares function.
    Rules:
    - Index 0: Multiple of 3 -> Square
    - Index i is multiple of 3 -> Square
    - Index i is multiple of 4 (and NOT 3) -> Cube
    - Otherwise -> Unchanged
    - Priority: Square (multiple of 3) takes precedence over Cube (multiple of 4).
    """

    # --- 1. Edge Cases ---

    def test_empty_list(self):
        """Tests that an empty list returns 0."""
        assert sum_squares([]) == 0

    def test_all_zeros(self):
        """Tests that a list of zeros returns zero."""
        assert sum_squares([0, 0, 0, 0, 0]) == 0

    def test_single_element(self):
        """Tests single element lists, specifically index 0 (multiple of 3)."""
        assert sum_squares([5]) == 25  # 5^2
        assert sum_squares([0]) == 0   # 0^2
        assert sum_squares([-3]) == 9  # (-3)^2

    # --- 2. Core Logic & Rule Precedence ---

    def test_provided_examples(self):
        """Tests the specific examples provided in the function docstring."""
        assert sum_squares([1, 2, 3]) == 6
        assert sum_squares([-1, -5, 2, -1, -5]) == -126

    def test_rule_precedence_priority(self):
        """
        Tests that the 'Multiple of 3' (Square) rule takes precedence 
        over the 'Multiple of 4' (Cube) rule at index 12.
        """
        # Index 12 is a multiple of both 3 and 4.
        # We create a list of 13 elements (0-12).
        # We set index 12 to 3. If it squares: 3^2 = 9. If it cubes: 3^3 = 27.
        test_list = [1] * 13
        test_list[12] = 3
        
        # Calculation:
        # idx 0 (sq): 1, idx 3 (sq): 1, idx 4 (cu): 1, idx 6 (sq): 1, 
        # idx 8 (cu): 1, idx 9 (sq): 1, idx 12 (sq): 9.
        # All other indices are 1.
        # Sum: (1*12) + 9 = 21
        assert sum_squares(test_list) == 21

    def test_complex_sequence(self):
        """Tests a long sequence to ensure all index rules trigger correctly."""
        # Indices: 0(sq), 1, 2, 3(sq), 4(cu), 5, 6(sq), 7, 8(cu), 9(sq), 10, 11, 12(sq)
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # Calculation:
        # 0: 1^2=1 | 1: 2 | 2: 3 | 3: 4^2=16 | 4: 5^3=125 | 5: 6 | 6: 7^2=49 | 7: 8 | 8: 9^3=729 | 9: 10^2=100 | 10: 11 | 11: 12 | 12: 13^2=169
        # Sum: 1+2+3+16+125+6+49+8+729+100+11+12+169 = 1231
        expected_sum = 1231
        assert sum_squares(input_list) == expected_sum

    # --- 3. Mathematical Properties ---

    @pytest.mark.parametrize("input_list, expected_output", [
        ([1, 1, 1], 3),           # idx 0 is sq: 1+1+1=3
        ([2, 2, 2, 2], 12),       # idx 0 is sq (4), idx 3 is sq (4): 4+2+2+4=12
        ([1, 2, 1, 2, 2], 16),    # idx 0(sq:1), idx 1(2), idx 2(1), idx 3(sq:4), idx 4(cu:8) -> 16
        ([-2, -2, -2, -2], 4),    # idx 0: (-2)^2=4, idx 1: -2, idx 2: -2, idx 3: (-2)^2=4 -> 4
    ])
    def test_parametrized_combinations(self, input_list, expected_output):
        """Clean, corrected parameter testing for various index combinations."""
        assert sum_squares(input_list) == expected_output

    def test_negative_number_handling(self):
        """
        Verifies that squaring negative numbers results in positive values,
        while cubing negative numbers remains negative.
        """
        # idx 0: (-2)^2 = 4 (Square)
        # idx 1: -3 (Unchanged)
        # idx 2: -4 (Unchanged)
        # idx 3: (-5)^2 = 25 (Square)
        # idx 4: (-6)^3 = -216 (Cube)
        # Sum: 4 - 3 - 4 + 25 - 216 = -194
        assert sum_squares([-2, -3, -4, -5, -6]) == -194
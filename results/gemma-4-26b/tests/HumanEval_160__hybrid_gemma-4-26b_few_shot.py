
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

import pytest

# Note: do_algebra is assumed to be imported from your implementation module

class TestDoAlgebra:
    """
    A comprehensive test suite for the do_algebra function, 
    covering single operations, PEMDAS precedence, complex chains, 
    and mathematical edge cases.
    """

    @pytest.mark.parametrize("operators, operands, expected", [
        (['+'], [10, 5], 15),
        (['-'], [10, 5], 5),
        (['*'], [10, 5], 50),
        (['//'], [10, 3], 3),
        (['**'], [2, 3], 8),
    ])
    def test_single_operations(self, operators, operands, expected):
        """Tests the function with exactly one operator and two operands."""
        assert do_algebra(operators, operands) == expected

    @pytest.mark.parametrize("operators, operands, expected", [
        # --- Multiplication vs Addition ---
        (['+', '*'], [2, 3, 4], 14),      # 2 + (3 * 4) = 14
        (['*', '+'], [2, 3, 4], 10),      # (2 * 3) + 4 = 10
        
        # --- Addition vs Subtraction (Left-to-Right) ---
        (['+', '-'], [10, 5, 2], 13),     # (10 + 5) - 2 = 13
        (['-', '+'], [10, 5, 2], 7),      # (10 - 5) + 2 = 7
        
        # --- Exponentiation (Highest Precedence) ---
        (['+', '**'], [2, 3, 2], 11),     # 2 + (3 ** 2) = 11
        (['**', '+'], [3, 2, 5], 14),     # (3 ** 2) + 5 = 14
        (['*', '**'], [2, 3, 2], 18),     # 2 * (3 ** 2) = 18
        (['**', '*'], [2, 3, 2], 16),     # (2 ** 3) * 2 = 16
        
        # --- Floor Division Precedence ---
        (['*', '//'], [10, 2, 5], 0),     # 10 * (2 // 5) = 10 * 0 = 0
        (['//', '*'], [10, 2, 5], 25),    # (10 // 2) * 5 = 25
        (['-', '//'], [10, 3, 2], 9),     # 10 - (3 // 2) = 10 - 1 = 9
        (['//', '-'], [10, 3, 2], 1),     # (10 // 3) - 2 = 3 - 2 = 1
    ])
    def test_operator_precedence(self, operators, operands, expected):
        """Tests that the function respects standard mathematical order of operations (PEMDAS)."""
        assert do_algebra(operators, operands) == expected

    @pytest.mark.parametrize("operators, operands, expected", [
        # 2 + 3 * 4 - 5 = 9
        (['+', '*', '-'], [2, 3, 4, 5], 9),
        
        # 2 ** 3 // 2 + 10 -> 8 // 2 + 10 = 14
        (['**', '//', '+'], [2, 3, 2, 10], 14),
        
        # 10 - 2 * 3 ** 2 // 6 -> 10 - (2 * 9 // 6) -> 10 - 3 = 7
        (['-', '*', '**', '//'], [10, 2, 3, 2, 6], 7),
        
        # 2 + 3 * 4 - 5 // 2 ** 3 -> 2 + 12 - (5 // 8) -> 14 - 0 = 14
        (['+', '*', '-', '//', '**'], [2, 3, 4, 5, 2, 3], 14),
    ])
    def test_complex_chains(self, operators, operands, expected):
        """Tests long chains of mixed operators to ensure cumulative precedence logic."""
        assert do_algebra(operators, operands) == expected

    @pytest.mark.parametrize("operators, operands, expected", [
        # Zeroes
        (['*', '+'], [0, 5, 5], 5),       # (0 * 5) + 5 = 5
        (['+', '*'], [5, 0, 5], 5),       # 5 + (0 * 5) = 5
        (['**'], [5, 0], 1),              # 5^0 = 1
        (['**'], [0, 5], 0),              # 0^5 = 0
        (['//'], [1, 10], 0),             # 1 // 10 = 0
        
        # Negative Results
        (['-'], [5, 10], -5),             # 5 - 10 = -5
        (['*', '-'], [2, 3, 20], -14),    # (2 * 3) - 20 = -14
        (['**', '-'], [5, 0, 2], -1),     # (5**0) - 2 = 1 - 2 = -1
        
        # Repetition
        (['+', '+', '+'], [1, 1, 1, 1], 4),
        (['*', '*', '*'], [2, 2, 2, 2], 16),
        
        # Large Numbers
        (['*', '*'], [100, 100, 100], 1000000),
        (['**'], [10, 4], 10000),
    ])
    def test_edge_cases(self, operators, operands, expected):
        """Tests behavior with zero, negative results, repetition, and large numbers."""
        assert do_algebra(operators, operands) == expected
import pytest
from your_module import do_algebra  # Replace your_module

class TestDoAlgebra:
    """
    Comprehensive pytest suite for the do_algebra function.
    """

    def test_addition_only(self):
        """Tests a simple addition expression."""
        operators = ['+']
        operands = [2, 3]
        assert do_algebra(operators, operands) == 5

    def test_subtraction_only(self):
        """Tests a simple subtraction expression."""
        operators = ['-']
        operands = [5, 2]
        assert do_algebra(operators, operands) == 3

    def test_multiplication_only(self):
        """Tests a simple multiplication expression."""
        operators = ['*']
        operands = [2, 3]
        assert do_algebra(operators, operands) == 6

    def test_floor_division_only(self):
        """Tests a simple floor division expression."""
        operators = ['//']
        operands = [10, 2]
        assert do_algebra(operators, operands) == 5

    def test_exponentiation_only(self):
        """Tests a simple exponentiation expression."""
        operators = ['**']
        operands = [2, 3]
        assert do_algebra(operators, operands) == 8

    def test_addition_and_subtraction(self):
        """Tests a combination of addition and subtraction."""
        operators = ['+', '-']
        operands = [2, 3, 1]
        assert do_algebra(operators, operands) == 4

    def test_multiplication_and_addition(self):
        """Tests a combination of multiplication and addition."""
        operators = ['*', '+']
        operands = [2, 3, 4]
        assert do_algebra(operators, operands) == 10

    def test_multiplication_and_subtraction(self):
        """Tests a combination of multiplication and subtraction."""
        operators = ['*', '-']
        operands = [2, 3, 1]
        assert do_algebra(operators, operands) == 5

    def test_floor_division_and_addition(self):
        """Tests a combination of floor division and addition."""
        operators = ['//', '+']
        operands = [10, 2, 3]
        assert do_algebra(operators, operands) == 8

    def test_exponentiation_and_multiplication(self):
        """Tests a combination of exponentiation and multiplication."""
        operators = ['**', '*']
        operands = [2, 3, 2]
        assert do_algebra(operators, operands) == 32

    def test_complex_expression(self):
        """Tests a more complex expression with multiple operations."""
        operators = ['+', '*', '-', '//']
        operands = [2, 3, 4, 5, 2]
        assert do_algebra(operators, operands) == 7

    def test_large_numbers(self):
        """Tests with larger numbers to ensure no overflow issues."""
        operators = ['*']
        operands = [1000, 2000]
        assert do_algebra(operators, operands) == 2000000

    def test_zero_operand(self):
        """Tests with zero as an operand."""
        operators = ['+']
        operands = [5, 0]
        assert do_algebra(operators, operands) == 5

    def test_zero_division(self):
        """Tests floor division by zero.  Should raise ZeroDivisionError."""
        operators = ['//']
        operands = [5, 0]
        with pytest.raises(ZeroDivisionError):
            do_algebra(operators, operands)

    def test_negative_result(self):
        """Tests an expression that results in a negative number."""
        operators = ['-']
        operands = [5, 10]
        assert do_algebra(operators, operands) == -5

    def test_exponentiation_with_zero(self):
        """Tests exponentiation with zero as the base."""
        operators = ['**']
        operands = [0, 2]
        assert do_algebra(operators, operands) == 0

    def test_exponentiation_with_negative_exponent(self):
        """Tests exponentiation with a negative exponent.  Should raise ValueError."""
        operators = ['**']
        operands = [2, -2]
        with pytest.raises(ValueError):
            do_algebra(operators, operands)

    def test_empty_operator_list(self):
        """Tests with an empty operator list. Should raise ValueError."""
        operators = []
        operands = [2, 3]
        with pytest.raises(ValueError):
            do_algebra(operators, operands)

    def test_mismatched_lengths(self):
        """Tests when the lengths of operator and operand lists are mismatched. Should raise ValueError."""
        operators = ['+']
        operands = [2, 3, 4]
        with pytest.raises(ValueError):
            do_algebra(operators, operands)

    def test_non_integer_operand(self):
        """Tests with a non-integer operand. Should raise TypeError."""
        operators = ['+']
        operands = [2, 3.5]
        with pytest.raises(TypeError):
            do_algebra(operators, operands)

    def test_do_algebra_addition(self):
        """Tests addition operations."""
        operators = ['+']
        operands = [2, 3]
        assert do_algebra(operators, operands) == 5

        operators = ['+', '+', '+']
        operands = [1, 2, 3]
        assert do_algebra(operators, operands) == 6

        operators = ['+']
        operands = [0, 5]
        assert do_algebra(operators, operands) == 5

        operators = ['+']
        operands = [5, 0]
        assert do_algebra(operators, operands) == 5

    def test_do_algebra_subtraction(self):
        """Tests subtraction operations."""
        operators = ['-']
        operands = [5, 2]
        assert do_algebra(operators, operands) == 3

        operators = ['-', '-']
        operands = [10, 4, 2]
        assert do_algebra(operators, operands) == 4

        operators = ['-']
        operands = [5, 0]
        assert do_algebra(operators, operands) == 5

        operators = ['-']
        operands = [0, 5]
        assert do_algebra(operators, operands) == -5

    def test_do_algebra_multiplication(self):
        """Tests multiplication operations."""
        operators = ['*']
        operands = [2, 3]
        assert do_algebra(operators, operands) == 6

        operators = ['*', '*']
        operands = [2, 3, 4]
        assert do_algebra(operators, operands) == 24

        operators = ['*']
        operands = [0, 5]
        assert do_algebra(operators, operands) == 0

        operators = ['*']
        operands = [5, 0]
        assert do_algebra(operators, operands) == 0

    def test_do_algebra_floor_division(self):
        """Tests floor division operations."""
        operators = ['//']
        operands = [10, 2]
        assert do_algebra(operators, operands) == 5

        operators = ['//', '//']
        operands = [20, 4, 2]
        assert do_algebra(operators, operands) == 2

        operators = ['//']
        operands = [10, 3]
        assert do_algebra(operators, operands) == 3

        operators = ['//']
        operands = [3, 10]
        assert do_algebra(operators, operands) == 0

        operators = ['//']
        operands = [5, 0]
        with pytest.raises(ZeroDivisionError):
            do_algebra(operators, operands)

    def test_do_algebra_exponentiation(self):
        """Tests exponentiation operations."""
        operators = ['**']
        operands = [2, 3]
        assert do_algebra(operators, operands) == 8

        operators = ['**', '**']
        operands = [2, 3, 2]
        assert do_algebra(operators, operands) == 512

        operators = ['**']
        operands = [2, 0]
        assert do_algebra(operators, operands) == 1

        operators = ['**']
        operands = [0, 2]
        assert do_algebra(operators, operands) == 0

    def test_do_algebra_mixed_operations(self):
        """Tests mixed operations."""
        operators = ['+', '*', '-']
        operands = [2, 3, 4, 5]
        assert do_algebra(operators, operands) == 9

        operators = ['*', '+', '-']
        operands = [2, 3, 4, 5]
        assert do_algebra(operators, operands) == 11

        operators = ['-', '*', '+']
        operands = [2, 3, 4, 5]
        assert do_algebra(operators, operands) == -1

        operators = ['+', '-', '*', '//']
        operands = [10, 5, 2, 4]
        assert do_algebra(operators, operands) == 2

    def test_do_algebra_long_expression(self):
        """Tests a longer expression."""
        operators = ['+', '*', '-', '//', '**']
        operands = [2, 3, 4, 5, 2, 3]
        assert do_algebra(operators, operands) == 11

    def test_do_algebra_zero_operands(self):
        """Tests with zero operands."""
        operators = ['+']
        operands = [0, 0]
        assert do_algebra(operators, operands) == 0

    def test_do_algebra_large_numbers(self):
        """Tests with large numbers."""
        operators = ['*']
        operands = [1000, 1000]
        assert do_algebra(operators, operands) == 1000000

    def test_do_algebra_negative_result(self):
        """Tests cases that result in negative numbers."""
        operators = ['-']
        operands = [1, 2]
        assert do_algebra(operators, operands) == -1

    def test_do_algebra_invalid_input(self):
        """Tests invalid input scenarios."""
        operators = ['+']
        operands = [1]  # Not enough operands
        with pytest.raises(IndexError):
            do_algebra(operators, operands)

        operators = []  # Not enough operators
        operands = [1, 2]
        with pytest.raises(IndexError):
            do_algebra(operators, operands)
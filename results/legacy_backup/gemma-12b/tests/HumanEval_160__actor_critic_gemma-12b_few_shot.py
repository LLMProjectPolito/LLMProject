import pytest

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
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            if operand[i+1] == 0:
                return float('inf')  # Handle division by zero
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
        else:
            raise ValueError(f"Invalid operator: {operator[i]}")
    return result


class TestDoAlgebra:
    def test_basic_addition(self):
        """Test a simple addition expression."""
        operator = ['+']
        operand = [2, 3]
        assert do_algebra(operator, operand) == 5

    def test_addition_multiplication_subtraction(self):
        """Test a more complex expression with multiple operations."""
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        assert do_algebra(operator, operand) == 9

    def test_division_by_zero(self):
        """Test division by zero handling."""
        operator = ['//']
        operand = [10, 0]
        assert do_algebra(operator, operand) == float('inf')

    def test_exponentiation_with_zero(self):
        """Test exponentiation with zero exponent."""
        operator = ['**']
        operand = [5, 0]
        assert do_algebra(operator, operand) == 1

    def test_exponentiation_with_negative_exponent(self):
        """Test exponentiation with a negative exponent."""
        operator = ['**']
        operand = [2, -2]
        assert do_algebra(operator, operand) == 0.25

    def test_floor_division_with_negative_numbers(self):
        """Test floor division with negative numbers."""
        operator = ['//']
        operand = [10, -3]
        assert do_algebra(operator, operand) == -4

    def test_large_numbers(self):
        """Test with large numbers to check for potential overflow."""
        operator = ['*']
        operand = [1000000, 2000000]
        assert do_algebra(operator, operand) == 2000000000000

    def test_minimum_operand_length(self):
        """Test with the minimum allowed operand length (2)."""
        operator = ['+']
        operand = [1, 2]
        assert do_algebra(operator, operand) == 3

    def test_operator_order_of_operations(self):
        """Test that the expression is evaluated from left to right."""
        operator = ['+', '*']
        operand = [2, 3, 4]
        assert do_algebra(operator, operand) == 14  # 2 + (3 * 4)

    def test_invalid_operator(self):
        """Test with an invalid operator."""
        operator = ['&']  # Invalid operator
        operand = [2, 3]
        with pytest.raises(ValueError, match="Invalid operator: &"):
            do_algebra(operator, operand)

    def test_multiple_same_operators(self):
        """Test multiple consecutive operators of the same type."""
        operator = ['+', '+']
        operand = [1, 2, 3]
        assert do_algebra(operator, operand) == 6

    def test_mixed_positive_negative(self):
        """Test with a mix of positive and negative numbers."""
        operator = ['+', '*', '-']
        operand = [-2, 3, -4, 5]
        assert do_algebra(operator, operand) == -3  # -2 + (3 * -4) - 5

    def test_zero_as_operand(self):
        """Test with zero as an operand in different operations."""
        operator = ['+', '*', '//', '**']
        operand = [5, 0, 2, 2]
        assert do_algebra(operator, operand) == 5  # 5 + (0 * 2) // 2 ** 2

    def test_empty_operator_list(self):
        """Test with an empty operator list and at least two operands."""
        operator = []
        operand = [5, 10]
        with pytest.raises(IndexError):
            do_algebra(operator, operand)

    def test_single_operand(self):
        """Test with a single operand and an empty operator list."""
        operator = []
        operand = [5]
        with pytest.raises(IndexError):
            do_algebra(operator, operand)
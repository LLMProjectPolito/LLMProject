
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
import ast
import operator

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
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    for num in operand:
        if not isinstance(num, int) or num < 0:
            raise TypeError("Operand list must contain non-negative integers.")

    expression = operand[0]
    for i in range(len(operator)):
        expression = str(expression) + operator[i] + str(operand[i+1])
    try:
        return eval(expression)
    except (ZeroDivisionError, IndexError) as e:
        raise e


class TestDoAlgebra:
    def test_algebra_addition(self):
        operator = ['+']
        operand = [2, 3]
        assert do_algebra(operator, operand) == 5

    def test_algebra_subtraction(self):
        operator = ['-']
        operand = [5, 2]
        assert do_algebra(operator, operand) == 3

    def test_algebra_multiplication(self):
        operator = ['*']
        operand = [2, 3]
        assert do_algebra(operator, operand) == 6

    def test_algebra_floor_division(self):
        operator = ['//']
        operand = [10, 2]
        assert do_algebra(operator, operand) == 5

    def test_algebra_exponentiation(self):
        operator = ['**']
        operand = [2, 3]
        assert do_algebra(operator, operand) == 8

    def test_algebra_complex_expression(self):
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        assert do_algebra(operator, operand) == 9

    def test_algebra_multiple_operations(self):
        operator = ['+', '*', '//']
        operand = [2, 3, 4, 2]
        assert do_algebra(operator, operand) == 10

    def test_algebra_with_zero(self):
        operator = ['+']
        operand = [0, 5]
        assert do_algebra(operator, operand) == 5

    def test_algebra_with_large_numbers(self):
        operator = ['*']
        operand = [1000, 1000]
        assert do_algebra(operator, operand) == 1000000

    def test_algebra_with_exponentiation_and_zero(self):
        operator = ['**']
        operand = [0, 5]
        assert do_algebra(operator, operand) == 0

    def test_algebra_with_exponentiation_and_one(self):
        operator = ['**']
        operand = [1, 5]
        assert do_algebra(operator, operand) == 1

    def test_algebra_with_floor_division_and_zero(self):
        operator = ['//']
        operand = [5, 0]
        with pytest.raises(ZeroDivisionError):
            do_algebra(operator, operand)

    def test_algebra_negative_number(self):
        operator = ['+']
        operand = [-2, 3]
        with pytest.raises(TypeError):
            do_algebra(operator, operand)

    def test_algebra_empty_operator_list(self):
        operator = []
        operand = [2, 3]
        with pytest.raises(ValueError):
            do_algebra(operator, operand)

    def test_algebra_single_operand(self):
        operator = ['+']
        operand = [2]
        with pytest.raises(ValueError):
            do_algebra(operator, operand)

    def test_algebra_exponentiation_negative_exponent(self):
        operator = ['**']
        operand = [2, -1]
        assert do_algebra(operator, operand) == 0.5

    def test_algebra_exponentiation_floating_point_result(self):
        operator = ['**']
        operand = [2, 0.5]
        assert do_algebra(operator, operand) == 1.4142135623730951

    def test_algebra_subtraction_larger_operand(self):
        operator = ['-']
        operand = [1, 5]
        assert do_algebra(operator, operand) == -4

    def test_algebra_multiplication_with_zero(self):
        operator = ['*']
        operand = [5, 0]
        assert do_algebra(operator, operand) == 0

    def test_algebra_invalid_operand_type(self):
        operator = ['+']
        operand = [2, 'a']
        with pytest.raises(TypeError):
            do_algebra(operator, operand)

    def test_algebra_operator_length_mismatch(self):
        operator = ['+','*']
        operand = [2,3]
        with pytest.raises(ValueError):
            do_algebra(operator, operand)
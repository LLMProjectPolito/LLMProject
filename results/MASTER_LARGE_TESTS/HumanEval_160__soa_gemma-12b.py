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
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i+1])
    return eval(expression)

class TestDoAlgebra:
    def test_addition(self):
        operator = ['+']
        operand = [2, 3]
        assert do_algebra(operator, operand) == 5

    def test_subtraction(self):
        operator = ['-']
        operand = [5, 2]
        assert do_algebra(operator, operand) == 3

    def test_multiplication(self):
        operator = ['*']
        operand = [2, 3]
        assert do_algebra(operator, operand) == 6

    def test_floor_division(self):
        operator = ['//']
        operand = [10, 2]
        assert do_algebra(operator, operand) == 5

    def test_exponentiation(self):
        operator = ['**']
        operand = [2, 3]
        assert do_algebra(operator, operand) == 8

    def test_addition_multiplication(self):
        operator = ['+', '*']
        operand = [2, 3, 4]
        assert do_algebra(operator, operand) == 14

    def test_subtraction_division(self):
        operator = ['-', '//']
        operand = [10, 2, 3]
        assert do_algebra(operator, operand) == 2

    def test_complex_expression(self):
        operator = ['+', '*', '-', '//']
        operand = [2, 3, 4, 5, 2]
        assert do_algebra(operator, operand) == 7

    def test_multiple_additions(self):
        operator = ['+', '+']
        operand = [1, 2, 3]
        assert do_algebra(operator, operand) == 6

    def test_multiple_subtractions(self):
        operator = ['-', '-']
        operand = [10, 2, 3]
        assert do_algebra(operator, operand) == 5

    def test_zero_operand(self):
        operator = ['+']
        operand = [0, 5]
        assert do_algebra(operator, operand) == 5

    def test_large_numbers(self):
        operator = ['*']
        operand = [1000, 2000]
        assert do_algebra(operator, operand) == 2000000

    def test_exponentiation_with_zero(self):
        operator = ['**']
        operand = [2, 0]
        assert do_algebra(operator, operand) == 1

    def test_exponentiation_with_one(self):
        operator = ['**']
        operand = [5, 1]
        assert do_algebra(operator, operand) == 5
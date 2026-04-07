
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
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

class TestDoAlgebra:

    def test_addition_subtraction(self):
        assert do_algebra(['+', '-'], [2, 3, 4, 5]) == 9

    def test_multiplication_floor_division(self):
        assert do_algebra(['*', '//'], [2, 3, 4, 5]) == 4

    def test_exponentiation_addition(self):
        assert do_algebra(['**', '+'], [2, 3, 4, 5]) == 125

    def test_multiple_operations(self):
        assert do_algebra(['+', '*', '-', '**'], [2, 3, 4, 5, 6]) == 12

    def test_floor_division_exponentiation(self):
        assert do_algebra(['//', '**'], [2, 3, 4, 5]) == 1

    def test_single_operand(self):
        assert do_algebra(['+', '-'], [2, 3]) == 2

    def test_single_operator(self):
        assert do_algebra(['+'], [2, 3, 4, 5]) == 2

    def test_large_numbers(self):
        assert do_algebra(['*', '//'], [1000, 2000, 3000, 4000]) == 1000

    def test_zero_operand(self):
        assert do_algebra(['+', '-'], [2, 0, 3, 4, 5]) == 2

    def test_zero_operator(self):
        assert do_algebra([], [2, 3, 4, 5]) == 2

    def test_negative_numbers(self):
        assert do_algebra(['+', '-'], [-2, 3, 4, 5]) == 0

    def test_exponentiation_with_zero_exponent(self):
        assert do_algebra(['**'], [2, 0]) == 1

    def test_complex_expression(self):
        assert do_algebra(['+', '*', '//', '-'], [2, 3, 4, 5, 6]) == 1

def test_addition():
    operator = ['+', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 9

def test_subtraction():
    operator = ['-', '-', '+']
    operand = [5, 2, 3]
    assert do_algebra(operator, operand) == 0

def test_multiplication():
    operator = ['*', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 24

def test_floor_division():
    operator = ['//', '//']
    operand = [10, 2, 5]
    assert do_algebra(operator, operand) == 1

def test_exponentiation():
    operator = ['**', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 4

def test_mixed_operations():
    operator = ['+', '*', '-', '**']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 24

def test_single_operand():
    operator = ['+']
    operand = [5]
    assert do_algebra(operator, operand) == 5

def test_empty_operator():
    operator = []
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 1

def test_empty_operand():
    operator = ['+']
    operand = []
    assert do_algebra(operator, operand) == 0

def test_large_numbers():
    operator = ['*', '**']
    operand = [2, 3, 10]
    assert do_algebra(operator, operand) == 240

def test_zero_operand():
    operator = ['+', '*']
    operand = [5, 0, 2]
    assert do_algebra(operator, operand) == 10

def test_floor_division_zero():
    operator = ['//']
    operand = [10, 0]
    assert do_algebra(operator, operand) == 0

def test_exponentiation_zero():
    operator = ['**']
    operand = [2, 0]
    assert do_algebra(operator, operand) == 1

def test_complex_expression():
    operator = ['+', '*', '//', '-']
    operand = [10, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == 10
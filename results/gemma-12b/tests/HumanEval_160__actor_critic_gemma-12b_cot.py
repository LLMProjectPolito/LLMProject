
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
    expression = operand[0]
    for i in range(len(operator)):
        expression = str(expression) + operator[i] + str(operand[i+1])
    return eval(expression)

def test_do_algebra_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_do_algebra_multiplication():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_do_algebra_floor_division():
    operator = ['//']
    operand = [10, 2]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_do_algebra_complex_expression():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_multiple_operations():
    operator = ['+', '*', '//']
    operand = [2, 3, 4, 2]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_with_zero():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_with_large_numbers():
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

def test_do_algebra_with_exponentiation_and_zero():
    operator = ['**']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 0

def test_do_algebra_with_exponentiation_and_one():
    operator = ['**']
    operand = [1, 5]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_with_floor_division_and_zero():
    operator = ['//']
    operand = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_do_algebra_with_negative_number():
    operator = ['+']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_with_negative_exponent():
    operator = ['**']
    operand = [2, -2]
    assert do_algebra(operator, operand) == 0.25

def test_do_algebra_empty_operator_list():
    with pytest.raises(IndexError):
        do_algebra([], [5])

def test_do_algebra_single_operand():
    with pytest.raises(IndexError):
        do_algebra(['+'], [5])

def test_do_algebra_invalid_operator():
    operator = ['$']
    operand = [2, 3]
    with pytest.raises(NameError):
        do_algebra(operator, operand)

def test_do_algebra_with_non_integer_operand():
    operator = ['+']
    operand = [2, 3.5]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)

def test_do_algebra_order_of_operations():
    operator = ['+', '*',]
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_nested_expression():
    operator = ['+', '*', '//']
    operand = [2, 3, 4, 2]
    assert do_algebra(operator, operand) == 10
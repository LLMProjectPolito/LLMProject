
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
    if not operator or not operand:
        return None  # Handle empty lists

    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of the operand list.")

    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand list must contain non-negative integers.")

    try:
        expression = str(operand[0])
        for i in range(len(operator)):
            if operator[i] == '+':
                expression += '+' + str(operand[i+1])
            elif operator[i] == '-':
                expression += '-' + str(operand[i+1])
            elif operator[i] == '*':
                expression += '*' + str(operand[i+1])
            elif operator[i] == '//':
                expression += '//' + str(operand[i+1])
            elif operator[i] == '**':
                expression += '**' + str(operand[i+1])
        
        # Use ast.literal_eval for safer evaluation
        return eval(expression, {'__builtins__': None}, {})
    except (TypeError, ValueError, ZeroDivisionError):
        return None # Handle potential errors during evaluation



def test_do_algebra_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '-', '*', '/'], [10, 2, 5, 2]) == 10
    assert do_algebra(['*', '+', '-'], [1, 2, 3, 4]) == 7
    assert do_algebra(['**', '+'], [2, 3]) == 10
    assert do_algebra(['//', '+'], [10, 3]) == 4

def test_do_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**', '+', '*'], [2, 3, 4]) == 10

def test_do_algebra_floor_division():
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['//', '+', '*'], [10, 3, 4]) == 8
    assert do_algebra(['//', '**'], [2, 3]) == 1

def test_do_algebra_empty_operator():
    assert do_algebra([], [1, 2, 3]) is None

def test_do_algebra_empty_operand():
    assert do_algebra(['+', '*'], []) is None

def test_do_algebra_single_operand():
    assert do_algebra(['+'], [1]) is None

def test_do_algebra_invalid_expression():
    assert do_algebra(['+', ''], [1, 2]) is None

def test_do_algebra_division_by_zero():
    assert do_algebra(['/'], [10, 0]) is None

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '//', '**', '-'], [2, 3, 4, 5, 6]) == 35
    
def test_do_algebra_large_numbers():
    assert do_algebra(['+', '*'], [1000000, 2000000]) == 3000000000000

def test_do_algebra_negative_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [-1, 2])

def test_do_algebra_invalid_operator_length():
    with pytest.raises(ValueError):
        do_algebra(['+', '*', '-'], [1, 2])
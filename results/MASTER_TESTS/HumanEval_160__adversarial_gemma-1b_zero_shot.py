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
    try:
        expression = operand[:]  # Create a copy to avoid modifying the original list
        for op_str in operator:
            if op_str == '+':
                expression = expression[1:] + expression[0]
            elif op_str == '-':
                expression = expression[1:] - expression[0]
            elif op_str == '*':
                expression = expression[1:] * expression[0]
            elif op_str == '/':
                if expression[0] == 0:
                    return "Error: Division by zero"
                expression = expression[1:] // expression[0]
            elif op_str == '**':
                expression = expression[1:] ** expression[0]
        return expression
    except:
        return "Error: Invalid expression"

    
    
def test_addition():
    assert do_algebra['+', '*'] == '2 + 3 * 4 - 5'

def test_subtraction():
    assert do_algebra['-'], '2 - 3 * 4'

def test_multiplication():
    assert do_algebra['*', '/'] == '2 * 3 / 4'

def test_floor_division():
    assert do_algebra['//'], '2 // 3'

def test_exponentiation():
    assert do_algebra['**'], '2 ** 3'

def test_empty_operand():
    assert do_algebra['+', ''] == "Error: Invalid expression"

def test_empty_operator():
    assert do_algebra('', '2') == "Error: Invalid expression"

def test_invalid_expression():
    assert do_algebra['+', '3'] == "Error: Invalid expression"
    
def test_zero_division():
    assert do_algebra['/'], '2 // 3' == "Error: Division by zero"

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
    try:
        op1 = operator[0]
        op2 = operator[1]
        operand = operand[1:]

        if op1 == '+':
            return op2 + operand
        elif op1 == '-':
            return op2 - operand
        elif op1 == '*':
            return op2 * operand
        elif op1 == '/':
            if operand % op2 == 0:
                return operand // op2
            else:
                return float('inf')
        elif op1 == '**':
            return op2 ** operand
        else:
            return 0
    except:
        return 0
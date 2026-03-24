import pytest
import math

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
    if len(operator) == 1 and len(operand) == 1:
        return operator[0] + operand[0]
    elif len(operator) == 1:
        return operator[0]
    elif len(operand) == 1:
        return operand[0]
    elif len(operator) == 2:
        return operator[0] + operand[1]
    elif len(operand) == 2:
        return operand[0] * operand[1]
    else:
        return 0

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
        if len(operand) == 0:
            return 0
        if len(operand) == 1:
            return operand[0]
        
        if len(operator) == 0:
            return 0
        
        if len(operator) == 1:
            return operator[0]
        
        if len(operator) == 2:
            return operator[0] * operator[1]
        
        if operator[0] == '+':
            return operand[0] + operand[1]
        elif operator[0] == '-':
            return operand[0] - operand[1]
        elif operator[0] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '/':
            if operand[1] == 0:
                return 0
            return operand[0] // operand[1]
        elif operator[0] == '**':
            return operand[0] ** operand[1]
        else:
            return 0
    except:
        return 0

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
        if len(operator) == 1 and len(operand) == 1:
            return operator[0] + operand[0]
        elif len(operator) == 1:
            return operator[0]
        elif len(operand) == 1:
            return operand[0]
        else:
            return eval(str(operator[0]) + str(operand[0]))
    except:
        return None
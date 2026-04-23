
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
    if len(operand) == 0:
        return 0
    
    if len(operand) == 1:
        return operand[0]
    
    if len(operator) == 1:
        return operator[0]
    
    try:
        op1 = operator[0]
        op2 = operand[0]
        
        if op1 == '+':
            return op2 + op1
        elif op1 == '-':
            return op2 - op1
        elif op1 == '*':
            return op2 * op1
        elif op1 == '/':
            if op2 == 0:
                return "Division by zero"
            return op2 // op2
        elif op1 == '**':
            return op2 ** op1
        else:
            return "Invalid operator"
    except IndexError:
        return "IndexError"

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
    if len(operand) == 0:
        return 0
    
    if len(operand) == 1:
        return operand[0]
    
    if len(operator) == 1:
        return operator[0]
    
    try:
        op1 = operator[0]
        op2 = operand[0]
        
        if op1 == '+':
            return op2 + op1
        elif op1 == '-':
            return op2 - op1
        elif op1 == '*':
            return op2 * op1
        elif op1 == '/':
            if op2 == 0:
                return "Division by zero"
            return op2 // op2
        elif op1 == '**':
            return op2 ** op1
        else:
            return "Invalid operator"
    except:
        return "IndexError"

def test_do_algebra():
    assert do_algebra('+', 2) == 4
    assert do_algebra('-', 2) == 0
    assert do_algebra('*', 2) == 4
    assert do_algebra('/', 4) == 1
    assert do_algebra('/', 4) == 0
    assert do_algebra('+', 2) == 2
    assert do_algebra('-', 2) == 0
    assert do_algebra('*', 2) == 4
    assert do_algebra('/', 2) == 1
    assert do_algebra('/', 2) == 0
    assert do_algebra('+', 2) == 2
    assert do_algebra('-', 2) == 0
    assert do_algebra('*', 2) == 4
    assert do_algebra('/', 2) == 1
    assert do_algebra('/', 2) == 0
    assert do_algebra('+', 2) == 2
    assert do_algebra('-', 2) == 0
    assert do_algebra('*', 2) == 4
    assert do_algebra('/', 2) == 1
    assert do_algebra('/', 2) == 0
    assert do_algebra('+', 2) == 2
    assert do_algebra('-', 2) == 0
    assert do_algebra('*', 2) == 4
    assert do_algebra('/', 2) == 1
    assert do_algebra('/', 2) == 0
    assert do_algebra('+', 2) == 2
    assert do_algebra('-', 2) == 0
    assert do_algebra('*', 2) == 4
    assert do_algebra('/', 2) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test_do_algebra()
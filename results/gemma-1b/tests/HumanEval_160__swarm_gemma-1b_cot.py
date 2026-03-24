
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

```python
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
        op1 = operand[0]
        op2 = operator[0]
        
        if op1 == '+':
            return op2 + op1
        elif op1 == '-':
            return op2 - op1
        elif op1 == '*':
            return op2 * op1
        elif op1 == '/':
            if op2 == 0:
                return "Division by zero"
            return op2 // op1
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
        op1 = operand[0]
        op2 = operator[0]
        
        if op1 == '+':
            return op2 + op1
        elif op1 == '-':
            return op2 - op1
        elif op1 == '*':
            return op2 * op1
        elif op1 == '/':
            if op2 == 0:
                return "Division by zero"
            return op2 // op1
        elif op1 == '**':
            return op2 ** op1
        else:
            return "Invalid operator"
    except:
        return "Invalid expression"

def test_do_algebra():
    assert do_algebra('+', [2, 3, 4, 5]) == 14
    assert do_algebra('-', [2, 3, 4, 5]) == 1
    assert do_algebra('*', [2, 3, 4, 5]) == 12
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('+', [2, 3, 4, 5]) == 10
    assert do_algebra('-', [2, 3, 4, 5]) == 3
    assert do_algebra('*', [2, 3, 4, 5]) == 60
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_
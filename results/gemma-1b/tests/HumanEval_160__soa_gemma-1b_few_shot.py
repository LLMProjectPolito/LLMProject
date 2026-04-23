
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
    try:
        op1 = operator[0]
        op2 = operator[1]
        op3 = operator[2]
        operand = operand[2*len(op1):2*len(op1) + len(op2)]
        
        if op1 == '+':
            return op2 + op3
        elif op1 == '-':
            return op2 - op3
        elif op1 == '*':
            return op2 * op3
        elif op1 == '/':
            if op3 == 0:
                return "Error: Division by zero"
            return op2 // op3
        elif op1 == '**':
            return op2 ** op3
        else:
            return "Error: Invalid operator"
    except:
        return "Error: Invalid input"

    return "Error: Invalid input"
    
import sys
sys.setrecursionlimit(1500)
assert do_algebra('+ 2, 3') == 5
assert do_algebra('- 2, 3') == 1
assert do_algebra('* 2, 3') == 6
assert do_algebra('/') 2 == 1
assert do_algebra('2 ** 3') == 8
assert do_algebra('2 + 3 * 4') == 9
assert do_algebra('2 - 3 * 4') == 1
assert do_algebra('2 * 3 ** 4') == 1296
assert do_algebra('2 / 3') == 2
assert do_algebra('2 ** 3') == 8
assert do_algebra('2 + 3 * 4') == 9
assert do_algebra('2 - 3 * 4') == 1
assert do_algebra('2 * 3 ** 4') == 1296
assert do_algebra('2 / 3') == 2
assert do_algebra('2 + 3 * 4') == 9
assert do_algebra('2 - 3 * 4') == 1
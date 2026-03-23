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
        operand = operand[2:]
        
        if op1 == '+':
            return op2 + float(operand[0])
        elif op1 == '-':
            return op2 - float(operand[0])
        elif op1 == '*':
            return float(op2) * float(operand[0])
        elif op1 == '/':
            if float(operand[0]) == 0:
                return "Division by zero"
            return float(op2) // float(operand[0])
        elif op1 == '**':
            return float(op2) ** float(operand[0])
        else:
            return "Invalid operator"
    except (IndexError, TypeError):
        return "Invalid input"
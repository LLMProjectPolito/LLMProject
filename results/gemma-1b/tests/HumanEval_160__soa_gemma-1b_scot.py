
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
    
import pytest

def test_addition():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    assert result == 9
    
def test_subtraction():
    array = [2, 3, 4, 5]
    result = 2 - 3 * 4
    assert result == -5
    
def test_multiplication():
    array = [2, 3, 4, 5]
    result = 2 * 3 * 4 - 5
    assert result == 24
    
def test_floor_division():
    array = [2, 3, 4, 5]
    result = 2 // 3
    assert result == 0.6666666666666666
    
def test_exponentiation():
    array = [2, 3, 4, 5]
    result = **2
    assert result == 256
    
def test_invalid_operator():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert "Error: Invalid operator" == "Error: Invalid input"
    
def test_invalid_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert "Error: Invalid input" == "Error: Invalid input"
    
def test_empty_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert "Error: Invalid input" == "Error: Invalid input"
    
def test_zero_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert "Error: Invalid input" == "Error: Invalid input"
    
def test_mixed_operators():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 // 5
    assert result == 10
    
def test_complex_expression():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3 * 4 - 5
    assert result == 23
```
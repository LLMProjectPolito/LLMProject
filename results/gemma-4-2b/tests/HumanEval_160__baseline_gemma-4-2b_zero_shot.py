
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
    expression = ""
    for i in range(len(operand) - 1):
        expression += str(operand[i])
        if i < len(operand) - 2:
            expression += " "
    for i in range(len(operator)):
        expression += operator[i]
    expression += str(operand[-1])
    return eval(expression)

def test_addition():
    assert do_algebra(['+', 2, 3, 4], [2, 3, 4]) == 9

def test_subtraction():
    assert do_algebra(['-', 2, 3, 4], [2, 3, 4]) == 9

def test_multiplication():
    assert do_algebra(['*', 2, 3, 4], [2, 3, 4]) == 24

def test_floor_division():
    assert do_algebra(['//', 2, 3, 4], [2, 3, 4]) == 2

def test_exponentiation():
    assert do_algebra(['**', 2, 3, 4], [2, 3, 4]) == 16

def test_mixed_operations():
    assert do_algebra(['+', '-', '*', 2, 3, 4], [2, 3, 4]) == 11

def test_single_operand():
    with pytest.raises(ValueError):
        do_algebra(['+', 2], [2])

def test_no_operator():
    with pytest.raises(ValueError):
        do_algebra([], [2, 3, 4])

def test_no_operands():
    with pytest.raises(ValueError):
        do_algebra(['+', 2], [])

def test_empty_operator_list():
    assert do_algebra([], [2, 3, 4]) == 0

def test_empty_operand_list():
    with pytest.raises(ValueError):
        do_algebra(['+', 2, 3, 4], [])
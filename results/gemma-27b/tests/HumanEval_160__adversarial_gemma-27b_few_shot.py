
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
    if not operator or not operand:
        raise ValueError("Operator and operand lists cannot be empty.")
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than operand list.")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")
    for num in operand:
        if num < 0:
            raise ValueError("Operand list must contain non-negative integers.")

    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            if num == 0:
                raise ZeroDivisionError("Division by zero.")
            result //= num
        elif op == '**':
            result **= num
        else:
            raise ValueError(f"Invalid operator: {op}")
    return result

# Pytest tests
def test_algebra_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_algebra_addition():
    assert do_algebra(['+'], [1, 2]) == 3

def test_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6

def test_algebra_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_algebra_complex():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_algebra_long_chain():
    assert do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15

def test_algebra_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_algebra_empty_operator():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_algebra_empty_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_algebra_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['%'], [1, 2])

def test_algebra_operator_length_mismatch():
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [1, 2, 3])

def test_algebra_operand_length_too_short():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1])

def test_algebra_negative_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [-1, 2])

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
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
        The function raises a ValueError if an unsupported operator is encountered.
        The function is designed to work only with non-negative integers in the operand list.
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")

    for num in operand:
        if num < 0:
            raise ValueError("Operand list must contain only non-negative integers.")

    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            if operand[i+1] == 0:
                return float('inf')
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
        else:
            raise ValueError(f"Unsupported operator: {operator[i]}")
    return result

# Pytest Tests
def test_do_algebra_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_zero_operand():
    assert do_algebra(['+'], [0, 5]) == 5

def test_do_algebra_exponentiation_zero():
    assert do_algebra(['**'], [5, 0]) == 1

def test_do_algebra_floor_division_by_zero():
    assert do_algebra(['//'], [5, 0]) == float('inf')

def test_do_algebra_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '//'], [2, 3, 4, 2]) == 8.0

def test_do_algebra_single_operation():
    assert do_algebra(['+'], [1, 2]) == 3

def test_do_algebra_negative_numbers_not_supported():
    with pytest.raises(ValueError):
        do_algebra(['+'], [-1, 2])

def test_do_algebra_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['%'], [1, 2])

def test_do_algebra_empty_operator():
    with pytest.raises(ValueError):
        do_algebra([], [1])

def test_do_algebra_too_few_operands():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1])

def test_do_algebra_exponentiation_negative():
    assert do_algebra(['**'], [2, -1]) == 0.5

def test_do_algebra_floor_division_large():
    assert do_algebra(['//'], [1000000, 2]) == 500000
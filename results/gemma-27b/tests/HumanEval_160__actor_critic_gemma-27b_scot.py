
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
    if len(operand) < 2:
        raise IndexError("Operand list must have at least two elements.")

    result = operand[0]
    for i in range(len(operator)):
        try:
            if operator[i] == '+':
                result += operand[i+1]
            elif operator[i] == '-':
                result -= operand[i+1]
            elif operator[i] == '*':
                result *= operand[i+1]
            elif operator[i] == '//':
                result //= operand[i+1]
            elif operator[i] == '**':
                if operand[0] == 0 and operand[i+1] < 0:
                    raise ValueError("Cannot raise zero to a negative power")
                result **= operand[i+1]
            else:
                raise TypeError("Invalid operator")
        except ZeroDivisionError:
            raise ValueError("Division by zero")
    return result

def test_valid_expression():
    operators = ['+', '*', '-']
    operands = [2, 3, 4, 5]
    assert do_algebra(operators, operands) == 9

def test_addition_only():
    operators = ['+']
    operands = [1, 2]
    assert do_algebra(operators, operands) == 3

def test_subtraction_only():
    operators = ['-']
    operands = [5, 2]
    assert do_algebra(operators, operands) == 3

def test_multiplication_only():
    operators = ['*']
    operands = [2, 3]
    assert do_algebra(operators, operands) == 6

def test_floor_division():
    operators = ['//']
    operands = [10, 3]
    assert do_algebra(operators, operands) == 3

def test_exponentiation():
    operators = ['**']
    operands = [2, 3]
    assert do_algebra(operators, operands) == 8

def test_mixed_operators():
    operators = ['+', '*', '//', '**']
    operands = [2, 3, 4, 2]
    assert do_algebra(operators, operands) == 10

def test_zero_division():
    operators = ['//']
    operands = [5, 0]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_zero_base_negative_exponent():
    operators = ['**']
    operands = [0, -1]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_large_numbers():
    operators = ['+']
    operands = [10**9, 10**9]
    assert do_algebra(operators, operands) == 2 * 10**9

def test_invalid_operator():
    operators = ['%']
    operands = [5, 2]
    with pytest.raises(TypeError):
        do_algebra(operators, operands)

def test_insufficient_operands():
    operators = ['+']
    operands = [5]
    with pytest.raises(IndexError):
        do_algebra(operators, operands)

def test_consecutive_operators():
    operators = ['*', '*', '+']
    operands = [2, 3, 4, 5]
    assert do_algebra(operators, operands) == 29

def test_floor_division_by_zero():
    operators = ['//']
    operands = [5, 0]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_long_expression():
    operators = ['+', '*', '-', '//', '**']
    operands = [2, 3, 4, 2, 2]
    assert do_algebra(operators, operands) == 11

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
    if len(operator) != len(operand) - 1:
        raise IndexError("Operator list length is not equal to operand list length minus one.")
    if len(operator) == 0:
        raise ValueError("Operator list must have at least one operator.")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")
    for op in operand:
        if op < 0:
            raise ValueError("Operands must be non-negative integers.")

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
                raise ZeroDivisionError("Division by zero")
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
        else:
            raise ValueError("Invalid operator")
    return result

def test_valid_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_addition_only():
    assert do_algebra(['+'], [1, 2]) == 3

def test_subtraction_only():
    assert do_algebra(['-'], [5, 2]) == 3

def test_multiplication_only():
    assert do_algebra(['*'], [2, 3]) == 6

def test_floor_division():
    assert do_algebra(['//'], [10, 3]) == 3

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_mixed_operators():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_zero_operand():
    assert do_algebra(['+'], [5, 0]) == 5

def test_zero_exponent():
    assert do_algebra(['**'], [2, 0]) == 1

def test_large_numbers():
    assert do_algebra(['+'], [10**9, 10**9]) == 2e9

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['$'], [1, 2])

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_exponentiation_by_zero():
    assert do_algebra(['**'], [2, 0]) == 1

def test_negative_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [-1, 2])

def test_long_expression():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_operator_operand_length():
    with pytest.raises(IndexError):
        do_algebra(['+','*'], [1,2,3])

def test_multiplication_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['*', '//'], [4, 0])

def test_operator_list_empty():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_operand_list_too_short():
    with pytest.raises(ValueError):
        do_algebra(['+'], [1])

def test_complex_expression_1():
    assert do_algebra(['+', '*', '-', '**'], [1, 2, 3, 4]) == 1 + 2 * 3 - 4**4
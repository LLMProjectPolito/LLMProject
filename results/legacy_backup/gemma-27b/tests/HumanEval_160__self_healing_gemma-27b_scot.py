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
        raise ValueError("Operator list length must be one less than operand list length.")
    if not operator:
        raise ValueError("Operator list cannot be empty.")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")

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
                raise ZeroDivisionError("Division by zero.")
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

def test_addition():
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['+', '+'], [2, 3, 4]) == 9

def test_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3
    assert do_algebra(['-', '-'], [10, 2, 3]) == 5

def test_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*', '*'], [2, 3, 4]) == 24

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['//', '//'], [20, 2, 5]) == 2

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**', '**'], [2, 3, 2]) == 64

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_exponentiation_zero_base():
    assert do_algebra(['**'], [0, 2]) == 0

def test_exponentiation_negative_base():
    assert do_algebra(['**'], [-2, 3]) == -8

def test_invalid_operator_length():
    with pytest.raises(ValueError):
        do_algebra(['+','*'], [2, 3, 4])

def test_invalid_operand_length():
    with pytest.raises(ValueError):
        do_algebra(['+'], [2, 3, 4])

def test_empty_operator_list():
    with pytest.raises(ValueError):
        do_algebra([], [2, 3])

def test_empty_operand_list():
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_single_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [2])
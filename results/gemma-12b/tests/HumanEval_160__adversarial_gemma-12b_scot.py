
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
        raise ValueError("Length of operator list must be one less than operand list")
    if not operator:
        raise ValueError("Operator list cannot be empty")
    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands")

    expression = str(operand[0])
    for i in range(len(operator)):
        expression += " " + operator[i] + " " + str(operand[i+1])

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def test_addition():
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['+', '+'], [2, 3, 4]) == 9

def test_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3
    assert do_algebra(['-', '-'], [10, 5, 2]) == 3

def test_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*', '*',], [2, 3, 4]) == 24

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['//', '//'], [20, 4, 2]) == 2
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**', '**'], [2, 3, 2]) == 36

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8

def test_zero_values():
    assert do_algebra(['+'], [0, 5]) == 5
    assert do_algebra(['-'], [5, 0]) == 5
    assert do_algebra(['*'], [0, 5]) == 0
    assert do_algebra(['//'], [5, 0]) # Should raise ZeroDivisionError

def test_large_numbers():
    assert do_algebra(['+'], [1000000, 2000000]) == 3000000
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_single_operator():
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['-'], [2, 1]) == 1

def test_negative_operands():
    assert do_algebra(['+'], [-2, 3]) == 1
    assert do_algebra(['-'], [5, -2]) == 7
    assert do_algebra(['*'], [-2, 3]) == -6
    assert do_algebra(['//'], [10, -2]) == -5

def test_empty_operator_list():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2])

def test_empty_operand_list():
    with pytest.raises(ValueError):
        do_algebra(['+'], [])

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['%'], [1, 2])
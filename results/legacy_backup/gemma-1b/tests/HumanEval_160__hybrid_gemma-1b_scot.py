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
        if len(operator) == 1:
            return operator[0]
        elif len(operator) == 2:
            return operator[0] + operator[1]
        elif len(operator) == 3:
            return operator[0] * operator[1] * operator[2]
        elif len(operator) == 4:
            return operator[0] * operator[1] * operator[2] * operator[3]
        elif len(operator) == 5:
            return operator[0] * operator[1] * operator[2] * operator[3] * operator[4]
        else:
            return 0  # Handle cases with more than 5 operators (or raise an exception)
    except:
        return 0  # Handle cases with invalid input (e.g., empty lists)


def test_addition():
    array = [2, 3, 4, 5]
    result = do_algebra(['+', '*', '-'], array)
    assert result == 9

def test_subtraction():
    array = [2, 3, 4, 5]
    result = do_algebra(['-', '-'], array)
    assert result == 1

def test_multiplication():
    array = [2, 3, 4, 5]
    result = do_algebra(['*', ''], array)
    assert result == 24

def test_floor_division():
    array = [2, 3, 4, 5]
    result = do_algebra(['//'], array)
    assert result == 2

def test_exponentiation():
    array = [2, 3, 4, 5]
    result = do_algebra(['**'], array)
    assert result == 256

def test_empty_operand():
    array = [2, 3, 4, 5]
    result = do_algebra(['+', '*', '-'], [])
    assert result == 0

def test_empty_operator():
    array = [2, 3, 4, 5]
    result = do_algebra(['+', '*', '-'], [])
    assert result == 0

def test_invalid_operator_length():
    array = [2, 3, 4, 5]
    result = do_algebra(['+', '*', '-'], [1, 2])
    assert result == 0

def test_invalid_operator_length_2():
    array = [2, 3, 4, 5]
    result = do_algebra(['+', '*', '-'], [1, 2, 3])
    assert result == 0

def test_basic_operations():
    array = [1, 2, 3, 4]
    result = do_algebra(['+', '-', '*'], array)
    assert result == 10
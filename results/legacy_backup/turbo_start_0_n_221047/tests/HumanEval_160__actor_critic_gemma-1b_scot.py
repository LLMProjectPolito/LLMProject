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
        if len(operator) == 1 and len(operand) == 1:
            return operator[0] + operand[0]
        elif len(operator) == 1:
            return operator[0]
        elif len(operand) == 1:
            return operand[0]
        else:
            return eval(str(operator[0]) + str(operand[0]) + operator[1] + str(operand[1]))
    except (TypeError, ValueError, IndexError):
        return None  # Handle potential errors during evaluation


def test_addition():
    array = [2, 3, 4, 5]
    result = do_algebra['+', '*', '-']
    assert result == 9
    
def test_subtraction():
    array = [2, 3, 4, 5]
    result = do_algebra['-'], ['a', 'b', 'c', 'd']
    assert result == 3
    
def test_multiplication():
    array = [2, 3, 4, 5]
    result = do_algebra('*', ['a', 'b', 'c', 'd'])
    assert result == 12
    
def test_floor_division():
    array = [2, 3, 4, 5]
    result = do_algebra('/') ['a', 'b', 'c', 'd']
    assert result == 1
    
def test_exponentiation():
    array = [2, 3, 4, 5]
    result = do_algebra**(['a', 'b', 'c', 'd'])
    assert result == 24
    
def test_empty_operand():
    array = [2, 3, 4, 5]
    result = do_algebra['+', '']
    assert result is None
    
def test_empty_operator():
    array = [2, 3, 4, 5]
    result = do_algebra('', ['a', 'b', 'c', 'd'])
    assert result is None
    
def test_invalid_input():
    array = [2, 3, 4, 5]
    result = do_algebra('a', ['a', 'b', 'c', 'd'])
    assert result is None
    
def test_mixed_operators():
    array = [2, 3, 4, 5]
    result = do_algebra('+', '-'), ['a', 'b', 'c', 'd']
    assert result == 10
    
def test_large_numbers():
    array = [1000, 2000, 3000, 4000]
    result = do_algebra('*', ['a', 'b', 'c', 'd'])
    assert result == 12000
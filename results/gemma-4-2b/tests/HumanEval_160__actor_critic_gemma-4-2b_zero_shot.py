
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
        if i < len(operator):
            expression += operator[i]
        expression += str(operand[i+1])
    return eval(expression)


def test_empty_lists():
    with pytest.raises(ValueError):
        do_algebra([], [])

def test_invalid_operator_length():
    with pytest.raises(ValueError):
        do_algebra(['+', '-'], [1, 2, 3])

def test_invalid_operand_length():
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [1])

def test_addition():
    assert do_algebra(['+', '+'], [1, 2]) == 3

def test_subtraction():
    assert do_algebra(['-', '+'], [5, 2]) == 3

def test_multiplication():
    assert do_algebra(['*', '+'], [2, 3]) == 9

def test_floor_division():
    assert do_algebra(['//', '+'], [10, 3]) == 3

def test_exponentiation():
    assert do_algebra(['**', '+'], [2, 3]) == 11

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4]) == 9

def test_complex_expression():
    assert do_algebra(['**', '+', '*'], [2, 3, 4]) == 25

def test_single_operand():
    with pytest.raises(ValueError):
        do_algebra(['+', '+'], [1])

def test_zero_operand():
    assert do_algebra(['+', '+'], [0, 0]) == 0

def test_large_numbers():
    assert do_algebra(['+', '+'], [1000, 2000]) == 3000

def test_negative_numbers():
    assert do_algebra(['-', '+'], [-5, 2]) == -3

def test_all_same_numbers():
    assert do_algebra(['+', '+'], [5, 5]) == 10

def test_exponentiation_with_zero():
    assert do_algebra(['**', '+'], [0, 3]) == 27

def test_exponentiation_with_one():
    assert do_algebra(['**', '+'], [1, 3]) == 4

def test_exponentiation_with_two():
    assert do_algebra(['**', '+'], [2, 3]) == 9
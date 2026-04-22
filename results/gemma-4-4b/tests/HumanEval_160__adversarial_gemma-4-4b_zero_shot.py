
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
from your_module import do_algebra  # Replace your_module

def test_addition():
    assert do_algebra(['+', 2], [3]) == 5
    assert do_algebra(['+', 1, 2], [3]) == 4
    assert do_algebra(['+', 5, 10], [2]) == 15

def test_subtraction():
    assert do_algebra(['-', 2], [3]) == 1
    assert do_algebra(['-', 5, 10], [2]) == 5
    assert do_algebra(['-', 10, 5], [2]) == 5

def test_multiplication():
    assert do_algebra(['*', 2], [3]) == 6
    assert do_algebra(['*', 2, 3], [4]) == 24
    assert do_algebra(['*', 5, 2], [3]) == 30

def test_floor_division():
    assert do_algebra(['//', 2], [3]) == 1
    assert do_algebra(['//', 5, 2], [3]) == 1
    assert do_algebra(['//', 10, 3], [2]) == 3

def test_exponentiation():
    assert do_algebra(['**', 2], [3]) == 8
    assert do_algebra(['**', 2, 3], [4]) == 64
    assert do_algebra(['**', 5, 2], [3]) == 25

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4]) == 10
    assert do_algebra(['*', '+', '//'], [2, 3, 4]) == 10
    assert do_algebra(['+', '-', '**', '*'], [2, 3, 4, 5]) == 24

def test_edge_cases():
    assert do_algebra(['+', 1], [2]) == 3
    assert do_algebra(['-', 1], [2]) == 1
    assert do_algebra(['*', 1], [2]) == 2
    assert do_algebra(['//', 1], [2]) == 0
    assert do_algebra(['**', 1], [2]) == 1

def test_invalid_input_operator_length():
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [1, 2, 3])

def test_invalid_input_operand_length():
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [1, 2])

def test_invalid_input_empty_operator():
    with pytest.raises(ValueError):
        do_algebra([], [1, 2, 3])

def test_invalid_input_empty_operand():
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [])

def test_invalid_input_non_integer_operand():
    with pytest.raises(TypeError):
        do_algebra(['+', 2], [3.14])
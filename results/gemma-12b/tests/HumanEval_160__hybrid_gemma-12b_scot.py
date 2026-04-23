
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
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['+', '+'], [2, 3, 4]) == 9

def test_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3
    assert do_algebra(['-', '-'], [10, 3, 2]) == 5

def test_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*', '*',], [2, 3, 4]) == 24

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['//', '//'], [20, 4, 2]) == 2

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**', '**'], [2, 3, 2]) == 36

def test_mixed_operators():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['-', '*', '+'], [10, 2, 3, 4]) == 8
    assert do_algebra(['+', '*', '**'], [2, 3, 4, 2]) == 32

def test_zero_values():
    assert do_algebra(['+'], [0, 5]) == 5
    assert do_algebra(['*'], [0, 5]) == 0
    assert do_algebra(['-'], [5, 0]) == 5
    assert do_algebra(['//'], [5, 0]) == 0

def test_large_operands():
    assert do_algebra(['+'], [1000, 2000]) == 3000
    assert do_algebra(['*'], [100, 100]) == 10000

def test_floor_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_exponentiation_zero_base():
    assert do_algebra(['**'], [0, 2]) == 0
    assert do_algebra(['**'], [0, 0]) == 1

def test_exponentiation_zero_exponent():
    assert do_algebra(['**'], [2, 0]) == 1

def test_two_operands():
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['-'], [5, 2]) == 3
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['**'], [2, 3]) == 8

def test_long_expression():
    assert do_algebra(['+', '*', '//', '**'], [2, 3, 4, 2, 3]) == 20

def test_invalid_operator():
    with pytest.raises(SyntaxError):
        do_algebra(['&'], [1, 2])

def test_empty_operator():
    with pytest.raises(ZeroDivisionError):
        do_algebra([], [1, 2])

def test_empty_operand():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_operand_length_mismatch():
    with pytest.raises(IndexError):
        do_algebra(['+'], [1, 2, 3])
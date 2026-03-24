import pytest
import math

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
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

def test_empty_operand():
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [])

def test_empty_operand_alternative():
    assert do_algebra(['+', '*'], []) == 0

def test_addition():
    assert do_algebra(['+'], [5]) == 5

def test_subtraction():
    assert do_algebra(['-'], [5]) == 5

def test_multiplication():
    assert do_algebra(['*'], [5]) == 5

def test_floor_division():
    assert do_algebra(['//'], [5]) == 5

def test_exponentiation():
    assert do_algebra(['**'], [5]) == 5

def test_addition_and_multiplication():
    assert do_algebra(['+', '*'], [2, 3, 4, 5]) == 14

def test_subtraction_and_exponentiation():
    assert do_algebra(['-', '**'], [5, 2]) == 3

def test_multiplication_and_floor_division():
    assert do_algebra(['*', '//'], [6, 3, 2]) == 6

def test_exponentiation_and_addition():
    assert do_algebra(['**', '+'], [2, 3, 4]) == 16
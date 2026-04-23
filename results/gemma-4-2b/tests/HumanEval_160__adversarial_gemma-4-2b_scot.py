
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
from typing import List

def do_algebra(operator: str, operand: List[int]) -> int:
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
    if not operand:
        raise ValueError("Operand list cannot be empty.")
    if len(operand) < 2:
        raise ValueError("Operand list must contain at least two operands.")
    if not operator:
        raise ValueError("Operator list cannot be empty.")
    if len(operator) < 1:
        raise ValueError("Operator list must contain at least one operator.")

    if operator[0] == '+':
        result = operand[0]
        for i in range(1, len(operator)):
            result += operand[i]
    elif operator[0] == '-':
        result = operand[0]
        for i in range(1, len(operator)):
            result -= operand[i]
    elif operator[0] == '*':
        result = 1
        for i in range(len(operator)):
            result *= operand[i]
    elif operator[0] == '//':
        result = operand[0]
        for i in range(1, len(operator)):
            result //= operand[i]
    elif operator[0] == '**':
        result = operand[0]
        for i in range(1, len(operator)):
            result **= operand[i]
    else:
        raise ValueError("Invalid operator.")
    return result


def test_addition():
    assert do_algebra("+", [2, 3, 4, 5]) == 14

def test_subtraction():
    assert do_algebra("-", [2, 3, 4, 5]) == 9

def test_multiplication():
    assert do_algebra("*", [2, 3, 4, 5]) == 120

def test_floor_division():
    assert do_algebra("//", [2, 3, 4, 5]) == 2

def test_exponentiation():
    assert do_algebra("**", [2, 3, 4, 5]) == 16

def test_valid_input():
    assert do_algebra("+", [2, 3, 4, 5]) == 14
    assert do_algebra("*", [2, 3, 4, 5]) == 120
    assert do_algebra("-", [2, 3, 4, 5]) == 9
    assert do_algebra("//", [2, 3, 4, 5]) == 2
    assert do_algebra("**", [2, 3, 4, 5]) == 16

def test_empty_operator():
    with pytest.raises(ValueError):
        do_algebra("", [2, 3, 4, 5])

def test_empty_operand():
    with pytest.raises(ValueError):
        do_algebra("+", [])

def test_too_few_operands():
    with pytest.raises(ValueError):
        do_algebra("+", [2])

def test_too_many_operators():
    with pytest.raises(ValueError):
        do_algebra("+", [2, 3, 4])

def test_large_numbers():
    assert do_algebra("+", [1000000, 2000000, 3000000]) == 6000000

def test_zero_values():
    assert do_algebra("+", [0, 0, 0, 0]) == 0
    assert do_algebra("*", [0, 0, 0, 0]) == 0
    assert do_algebra("-", [0, 0, 0, 0]) == 0
    assert do_algebra("//", [0, 0, 0, 0]) == 0
    assert do_algebra("**", [0, 0, 0, 0]) == 0

def test_invalid_input_type():
    with pytest.raises(TypeError):
        do_algebra("+", ["2", "3", "4", "5"]) #Incorrect type for operand
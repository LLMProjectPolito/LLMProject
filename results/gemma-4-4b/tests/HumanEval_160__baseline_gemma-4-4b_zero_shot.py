
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

@pytest.fixture
def test_do_algebra():
    yield

def test_addition(test_do_algebra):
    assert do_algebra(['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [2, 3, 4, 5]) == 9

def test_subtraction(test_do_algebra):
    assert do_algebra(['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [2, 3, 4, 5]) == -1

def test_multiplication(test_do_algebra):
    assert do_algebra(['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [2, 3, 4, 5]) == 20

def test_floor_division(test_do_algebra):
    assert do_algebra(['//', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [2, 3, 4, 5]) == 0

def test_exponentiation(test_do_algebra):
    assert do_algebra(['**', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [2, 3, 4, 5]) == 16

def test_mixed_operations(test_do_algebra):
    assert do_algebra(['+', '*', '-', '//'], [2, 3, 4, 5]) == 11

def test_empty_operator_list(test_do_algebra):
    assert do_algebra([], [2, 3, 4, 5]) == 2

def test_empty_operand_list(test_do_algebra):
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [])

def test_single_operand(test_do_algebra):
    with pytest.raises(IndexError):
        do_algebra(['+'], [2])

def test_large_numbers(test_do_algebra):
    assert do_algebra(['+', '*'], [1000, 2000]) == 3000

def test_zero_operand(test_do_algebra):
    assert do_algebra(['+', '*'], [0, 5]) == 0

def test_negative_numbers(test_do_algebra):
    assert do_algebra(['+', '-'], [-2, 5]) == 3

def test_complex_expression(test_do_algebra):
    assert do_algebra(['+', '*', '**', '-'], [2, 3, 2, 4]) == 22
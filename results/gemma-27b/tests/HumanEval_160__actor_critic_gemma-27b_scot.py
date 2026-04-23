
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

@pytest.mark.parametrize(
    "operator, operands, expected",
    [
        (['+'], [2, 3], 5),
        (['-'], [5, 2], 3),
        (['*'], [2, 3], 6),
        (['//'], [10, 3], 3),
        (['**'], [2, 3], 8),
    ],
)
def test_operators_parameterized(operator, operands, expected):
    assert do_algebra(operator, operands) == expected

def test_mixed_operators_with_floor_division():
    operators = ['*', '+', '//']
    operands = [2, 3, 4, 2]
    assert do_algebra(operators, operands) == 7

def test_floor_division_negative_numbers():
    operators = ['//']
    operands = [-5, 2]
    assert do_algebra(operators, operands) == -3

def test_exponentiation_negative_exponent():
    operators = ['**']
    operands = [2, -1]
    assert do_algebra(operators, operands) == 0.5

def test_exponentiation_zero_base():
    operators = ['**']
    operands = [0, 2]
    assert do_algebra(operators, operands) == 0

def test_exponentiation_one_base():
    operators = ['**']
    operands = [1, 5]
    assert do_algebra(operators, operands) == 1

def test_floor_division_by_zero():
    operators = ['//']
    operands = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operators, operands)

def test_large_numbers():
    operators = ['+']
    operands = [10**9, 10**9]
    assert do_algebra(operators, operands) == 2 * (10**9)

def test_empty_operator_list():
    operators = []
    operands = [5, 2]
    assert do_algebra(operators, operands) == 5

def test_mismatched_list_lengths():
    operators = ['+']
    operands = [5, 2, 3]
    with pytest.raises(IndexError):
        do_algebra(operators, operands)

def test_multiple_exponentiations():
    operators = ['**', '**']
    operands = [2, 3, 2]
    assert do_algebra(operators, operands) == 512

def test_negative_numbers_multiple_operators():
    operators = ['+', '*', '-']
    operands = [-2, 3, -4, 1]
    assert do_algebra(operators, operands) == 1

def test_exponentiation_large_numbers():
    operators = ['**']
    operands = [2, 100]
    assert do_algebra(operators, operands) == 1267650600228229401496703205376
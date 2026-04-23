
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
        op = operator[i]
        val = operand[i+1]
        if op == '+':
            result += val
        elif op == '-':
            result -= val
        elif op == '*':
            result *= val
        elif op == '//':
            result //= val
        elif op == '**':
            result **= val
    return result

def test_do_algebra_basic():
    assert do_algebra(['+', 2, 3], [1, 2]) == 5
    assert do_algebra(['-', 5, 2], [1, 2]) == -3
    assert do_algebra(['*', 2, 3], [1, 2]) == 6
    assert do_algebra(['//', 2, 3], [1, 2]) == 0
    assert do_algebra(['**', 2, 3], [1, 2]) == 8

def test_do_algebra_mixed():
    assert do_algebra(['+', '-', '*', '//'], [1, 2, 3, 4]) == 5
    assert do_algebra(['+', '*', '//', '**'], [1, 2, 3, 4]) == 16
    assert do_algebra(['-', '+', '*', '//'], [1, 2, 3, 4]) == 2

def test_do_algebra_exponentiation():
    assert do_algebra(['**', 2, 3], [1, 2]) == 8
    assert do_algebra(['**', 2, 3], [1, 2, 3]) == 8

def test_do_algebra_division():
    assert do_algebra(['//', 2, 3], [1, 2]) == 0
    assert do_algebra(['//', 2, 3], [1, 2, 3]) == 0

def test_do_algebra_complex():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 16
    assert do_algebra(['+', '*', '//', '**', '-'], [1, 2, 3, 4, 5]) == 16

def test_do_algebra_edge_case_empty_operand():
    with pytest.raises(IndexError):
        do_algebra(['+', 2, 3], [])

def test_do_algebra_edge_case_invalid_operator():
    with pytest.raises(TypeError):
        do_algebra(['%', 2, 3], [1, 2])

def test_do_algebra_edge_case_invalid_operand_type():
    with pytest.raises(TypeError):
        do_algebra(['+', 2, 3], [1, 'a'])

def test_do_algebra_edge_case_negative_operand():
    with pytest.raises(TypeError):
        do_algebra(['+', 2, -3], [1, 2])

def test_do_algebra_edge_case_zero_operand():
    assert do_algebra(['+', 2, 0], [1, 2]) == 2
    assert do_algebra(['-', 2, 0], [1, 2]) == -2
    assert do_algebra(['*', 2, 0], [1, 2]) == 0
    assert do_algebra(['//', 2, 0], [1, 2]) == 0
    assert do_algebra(['**', 2, 0], [1, 2]) == 0

def test_do_algebra_operator_precedence():
    assert do_algebra(['+', '*', 2, 3], [1, 2]) == 7
    assert do_algebra(['*', '+', 2, 3], [1, 2]) == 7
    assert do_algebra(['**', 2, 3, '+', 1], [1, 2]) == 16
    assert do_algebra(['+', '**', 2, 3], [1, 2]) == 17
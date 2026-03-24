
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
import pytest

def test_do_algebra_addition():
    assert do_algebra(['+', '+'], [1, 2, 3]) == 6

def test_do_algebra_subtraction():
    assert do_algebra(['-', '-', '-'], [5, 3, 2]) == 0

def test_do_algebra_multiplication():
    assert do_algebra(['*', '*'], [2, 3, 4]) == 24

def test_do_algebra_floor_division():
    assert do_algebra(['//', '//'], [10, 2, 5]) == 1

def test_do_algebra_exponentiation():
    assert do_algebra(['**', '**'], [2, 3, 2]) == 4

def test_do_algebra_mixed():
    assert do_algebra(['+', '*', '-', '**'], [2, 3, 4, 5, 2]) == 128

def test_do_algebra_empty_operand():
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [])

def test_do_algebra_empty_operator():
    assert do_algebra([], [1, 2, 3]) == 1

def test_do_algebra_single_operand():
    assert do_algebra(['+', '*'], [1]) == 1

def test_do_algebra_single_operator():
    assert do_algebra(['+'], [1, 2, 3]) == 1

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '//', '-'], [10, 2, 5, 3, 2]) == 16
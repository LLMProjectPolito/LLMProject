
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

def test_addition():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['+', '+'], [1, 2, 3]) == 6

def test_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3
    assert do_algebra(['-', '-'], [10, 2, 1]) == 7

def test_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*', '*'], [1, 2, 3]) == 6

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5
    assert do_algebra(['//', '//'], [20, 2, 5]) == 2

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8

def test_edge_case_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])

def test_single_operation():
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-'], [5, 2]) == 3

def test_negative_numbers():
    assert do_algebra(['+'], [1, -2]) == -1
    assert do_algebra(['*'], [2, -3]) == -6

def test_large_numbers():
    assert do_algebra(['+'], [10**9, 10**9]) == 2 * 10**9
    assert do_algebra(['*'], [10**5, 10**5]) == 10**10
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
    assert do_algebra(['+'], [2, 3]) == 5

def test_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_multiplication():
    assert do_algebra(['*'], [4, 3]) == 12

def test_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_longer_expression():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_zero_operand():
    assert do_algebra(['+'], [0, 5]) == 5

def test_zero_result():
    assert do_algebra(['-', '+'], [5, -5, 0]) == 0

def test_multiple_zeros():
    assert do_algebra(['+', '*', '-'], [0, 0, 0, 0]) == 0

def test_large_numbers():
    assert do_algebra(['+'], [1000000, 2000000]) == 3000000

def test_mixed_operators():
    assert do_algebra(['*', '+', '-'], [2, 3, 4, 1]) == 7

def test_division_by_one():
    assert do_algebra(['//'], [10, 1]) == 10

def test_exponentiation_one():
    assert do_algebra(['**'], [5, 1]) == 5

def test_exponentiation_zero():
    assert do_algebra(['**'], [5, 0]) == 1

def test_negative_result():
    assert do_algebra(['-', '+'], [1, -2, 3]) == 2

def test_all_subtraction():
    assert do_algebra(['-', '-', '-'], [10, 2, 3, 1]) == 4
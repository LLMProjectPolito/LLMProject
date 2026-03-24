
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

def test_do_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6

def test_do_algebra_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_do_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_complex_expression_2():
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 7
    assert do_algebra(['*', '+', '//'], [2, 3, 4, 5]) == 10

def test_do_algebra_complex_expression_3():
    assert do_algebra(['**', '-', '+'], [2, 3, 4, 1]) == 13

def test_do_algebra_long_expression():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2]) == 1

def test_do_algebra_with_zero():
    assert do_algebra(['+', '-', '*'], [0, 1, 2, 3]) == 1

def test_do_algebra_division_by_one():
    assert do_algebra(['//'], [5, 1]) == 5

def test_do_algebra_exponentiation_with_zero():
    assert do_algebra(['**'], [0, 2]) == 0

def test_do_algebra_exponentiation_with_one():
    assert do_algebra(['**'], [2, 0]) == 1

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5, 2]) == 1

def test_do_algebra_large_numbers():
    assert do_algebra(['+', '*'], [1000, 2000, 3]) == 7000

def test_do_algebra_all_additions():
    assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

def test_do_algebra_all_multiplications():
    assert do_algebra(['*', '*', '*'], [1, 2, 3, 4]) == 24

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '-', '//'], [10, 2, 3, 6]) == 11
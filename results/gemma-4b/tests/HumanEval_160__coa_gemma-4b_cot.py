
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
import math


# Focus: Boundary Values
import pytest

def test_do_algebra_addition():
    operator = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_subtraction():
    operator = ['-', '*']
    operand = [10, 2, 3, 4]
    assert do_algebra(operator, operand) == 16

def test_do_algebra_exponentiation():
    operator = ['**', '/']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 0.25

# Focus: Type Scenarios
import pytest

def test_type_scenario_1():
    operator = ['+', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_type_scenario_2():
    operator = ['//', '**']
    operand = [10, 2, 3]
    assert do_algebra(operator, operand) == 1

def test_type_scenario_3():
    operator = ['-', '**']
    operand = [5, 2, 3]
    assert do_algebra(operator, operand) == 4

# Focus: Logic Branches
import pytest

def test_addition():
    operator = ['+', '-']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 3

def test_multiplication():
    operator = ['*', '//']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 10

def test_exponentiation():
    operator = ['**', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14
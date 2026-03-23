import pytest
import math


# Focus: Boundary Values
def test_do_algebra_addition():
    operator = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_subtraction():
    operator = ['-', '*']
    operand = [10, 2, 3, 4]
    assert do_algebra(operator, operand) == 4

def test_do_algebra_multiplication():
    operator = ['*', '//']
    operand = [10, 2, 3, 4]
    assert do_algebra(operator, operand) == 20

# Focus: Type Scenarios
def test_do_algebra_addition():
    operator = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_subtraction():
    operator = ['-', '*']
    operand = [10, 2, 3, 4]
    assert do_algebra(operator, operand) == 4

def test_do_algebra_exponentiation():
    operator = ['**', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 16

# Focus: Logic Branches
def test_do_algebra_addition():
    operator = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_subtraction():
    operator = ['-', '*']
    operand = [10, 2, 3, 4]
    assert do_algebra(operator, operand) == 4

def test_do_algebra_exponentiation():
    operator = ['**', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14
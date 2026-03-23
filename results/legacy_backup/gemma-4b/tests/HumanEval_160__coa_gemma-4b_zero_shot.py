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
    operator = ['**', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 125

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
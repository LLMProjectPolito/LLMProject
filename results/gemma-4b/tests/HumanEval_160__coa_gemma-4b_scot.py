import pytest
import math


# Focus: Boundary Values
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

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `do_algebra` performs a series of algebraic operations on a list of operands and operators.
# Boundary value testing should focus on edge cases related to the length of the operand and operator lists,
# as well as the values of the operands themselves.  Specifically, we need to test with the minimum and maximum
# operand values, and with operator lists of minimal length.

# STEP 2: PLAN - List test functions names and scenarios.
# test_do_algebra_empty_operator
# test_do_algebra_single_operand
# test_do_algebra_max_operand

### STEP 3: CODE - Write the high-quality pytest suite.
def test_do_algebra_empty_operator():
    operator = []
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_single_operand():
    operator = ['+', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 2 + 3 * 4

def test_do_algebra_max_operand():
    operator = ['+', '*', '//', '**']
    operand = [2, 3, 4, 5, 6]
    assert do_algebra(operator, operand) == 2 + 3 * 4 // 5 ** 6

# Focus: Type Scenarios
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

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The tests should focus solely on the 'Type Scenarios' dimension, meaning they should test different types of inputs for the 'operator' and 'operand' lists.
# We need to cover cases with different operators and different lengths of operand lists.

# STEP 2: PLAN - List test functions names and scenarios.
# test_operator_types: Tests different operator types.
# test_operand_lengths: Tests different operand list lengths.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_operator_types():
    assert do_algebra(['+', '-', '*'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '//', '**'], [2, 3, 4, 5]) == 8
    assert do_algebra(['-', '+'], [5, 2, 3]) == 0
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['+', '*'], [1, 2, 3, 4]) == 10

def test_operand_lengths():
    assert do_algebra(['+', '-'], [2, 3]) == 1
    assert do_algebra(['*', '//'], [2, 3, 4]) == 2
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5]) == 14
    assert do_algebra(['**'], [2, 3, 4]) == 16

# Focus: Logic Branches
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

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The tests should focus on verifying the logic branches within the `do_algebra` function, specifically how it handles different operators and operands.
### We need to cover addition, subtraction, multiplication, floor division, and exponentiation.
### STEP 2: PLAN - List test functions names and scenarios.
### test_addition: Tests addition branch.
### test_subtraction: Tests subtraction branch.
### test_multiplication: Tests multiplication branch.
### test_floor_division: Tests floor division branch.
### test_exponentiation: Tests exponentiation branch.
### STEP 3: CODE - Write the high-quality pytest suite.

def test_addition():
    operator = ['+', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 9

def test_subtraction():
    operator = ['-', '-', '+']
    operand = [5, 2, 3]
    assert do_algebra(operator, operand) == 4

def test_multiplication():
    operator = ['*', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 24

def test_floor_division():
    operator = ['//', '//']
    operand = [10, 2, 5]
    assert do_algebra(operator, operand) == 2

def test_exponentiation():
    operator = ['**', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 4
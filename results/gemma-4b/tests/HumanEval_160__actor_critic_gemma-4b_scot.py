
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

### SCoT Steps:
# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `do_algebra` takes a list of operators and a list of operands and evaluates a mathematical expression.
# It iterates through the operators and operands, applying the corresponding operation.
# The function needs to handle addition, subtraction, multiplication, floor division, and exponentiation.
# Edge cases include empty operator list, single operand, and different operator/operand lengths.
# The function should return the final result of the expression.

# STEP 2: PLAN - List test functions names and scenarios.
# test_do_algebra_addition()
# test_do_algebra_subtraction()
# test_do_algebra_multiplication()
# test_do_algebra_floor_division()
# test_do_algebra_exponentiation()
# test_do_algebra_mixed_operations()
# test_do_algebra_edge_cases()

# STEP 3: CODE - Write the high-quality pytest suite.
###
# test_do_algebra_addition()
def test_do_algebra_addition():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

# test_do_algebra_subtraction()
def test_do_algebra_subtraction():
    operator = ['-', '-', '+']
    operand = [5, 2, 3, 1]
    assert do_algebra(operator, operand) == 3

# test_do_algebra_multiplication()
def test_do_algebra_multiplication():
    operator = ['*', '*', '+']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 24

# test_do_algebra_floor_division()
def test_do_algebra_floor_division():
    operator = ['//', '//', '+']
    operand = [10, 2, 3, 1]
    assert do_algebra(operator, operand) == 3

# test_do_algebra_exponentiation()
def test_do_algebra_exponentiation():
    operator = ['**', '**', '+']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 64

# test_do_algebra_mixed_operations()
def test_do_algebra_mixed_operations():
    operator = ['+', '*', '-', '**', '//']
    operand = [1, 2, 3, 4, 5, 6]
    assert do_algebra(operator, operand) == 21

# test_do_algebra_edge_cases()
def test_do_algebra_edge_cases():
    operator = ['+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 1

    operator = ['-']
    operand = [5, 2, 3]
    assert do_algebra(operator, operand) == 5

    operator = ['*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 24

    operator = ['//']
    operand = [10, 2, 3]
    assert do_algebra(operator, operand) == 3

    operator = ['**']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 16
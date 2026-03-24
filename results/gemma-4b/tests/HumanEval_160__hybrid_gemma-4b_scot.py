
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

# STEP 1: REASONING
# The function `do_algebra` takes a list of operators and a list of operands and evaluates a mathematical expression.
# The expression is built by applying the operators to the operands in sequence.
# The function needs to handle addition, subtraction, multiplication, floor division, and exponentiation.
# The tests should cover various combinations of operators and operands, including edge cases like empty lists or zero operands.
# We need to test the order of operations (PEMDAS/BODMAS) implicitly through the order of operations in the function.

# STEP 2: PLAN
# Test functions:
# - test_addition: Tests addition operations.
# - test_subtraction: Tests subtraction operations.
# - test_multiplication: Tests multiplication operations.
# - test_floor_division: Tests floor division operations.
# - test_exponentiation: Tests exponentiation operations.
# - test_mixed_operations: Tests a combination of all operations.
# - test_empty_operator: Tests with an empty operator list (should return the first operand).
# - test_empty_operand: Tests with an empty operand list (should return 0).
# - test_single_operand: Tests with a single operand (should return the operand).
# - test_zero_operand: Tests with a zero operand.

# STEP 3: CODE
# pytest suite
def test_addition():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

def test_subtraction():
    operator = ['-', '-', '-']
    operand = [5, 3, 2, 1]
    assert do_algebra(operator, operand) == 3

def test_multiplication():
    operator = ['*', '*', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 120

def test_floor_division():
    operator = ['//', '//', '//']
    operand = [10, 5, 2, 1]
    assert do_algebra(operator, operand) == 2

def test_exponentiation():
    operator = ['**', '**', '**']
    operand = [2, 3, 2, 1]
    assert do_algebra(operator, operand) == 8

def test_mixed_operations():
    operator = ['+', '*', '-', '**', '//']
    operand = [2, 3, 4, 5, 6, 7]
    assert do_algebra(operator, operand) == 24

def test_empty_operator():
    operator = []
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 1

def test_empty_operand():
    operator = ['+', '*']
    operand = []
    assert do_algebra(operator, operand) == 0

def test_single_operand():
    operator = ['+']
    operand = [5]
    assert do_algebra(operator, operand) == 5

def test_zero_operand():
    operator = ['*', '+']
    operand = [2, 0, 3]
    assert do_algebra(operator, operand) == 0
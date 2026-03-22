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
# test_do_algebra_basic: Test with a simple expression.
# test_do_algebra_multiple_operations: Test with multiple operations.
# test_do_algebra_exponentiation: Test with exponentiation.
# test_do_algebra_floor_division: Test with floor division.
# test_do_algebra_subtraction: Test with subtraction.
# test_do_algebra_addition: Test with addition.
# test_do_algebra_multiplication: Test with multiplication.
# test_do_algebra_empty_operator: Test with an empty operator list.
# test_do_algebra_single_operand: Test with a single operand.
# test_do_algebra_different_lengths: Test with different lengths of operator and operand lists.
# test_do_algebra_large_numbers: Test with large numbers to check for potential overflow issues.

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_do_algebra_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_multiple_operations():
    operator = ['+', '*', '-', '//', '**']
    operand = [2, 3, 4, 5, 6, 7]
    assert do_algebra(operator, operand) == 21

def test_do_algebra_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_do_algebra_floor_division():
    operator = ['//']
    operand = [10, 3]
    assert do_algebra(operator, operand) == 3

def test_do_algebra_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_do_algebra_addition():
    operator = ['+']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 7

def test_do_algebra_multiplication():
    operator = ['*']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_empty_operator():
    operator = []
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_single_operand():
    operator = ['+']
    operand = [5]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_different_lengths():
    operator = ['+', '*']
    operand = [1, 2, 3]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_do_algebra_large_numbers():
    operator = ['*', '**']
    operand = [2**30, 2]
    assert do_algebra(operator, operand) == 2**33
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
# We need to test various scenarios including different operators, operand values, and operator combinations.
# Edge cases should be considered, such as empty operator list, single operand, and different operand lengths.
# The function should handle both positive and negative operands correctly.

# STEP 2: PLAN
# Test functions:
# - test_addition: Tests addition operations.
# - test_subtraction: Tests subtraction operations.
# - test_multiplication: Tests multiplication operations.
# - test_floor_division: Tests floor division operations.
# - test_exponentiation: Tests exponentiation operations.
# - test_mixed_operations: Tests a combination of different operations.
# - test_empty_operator: Tests the case where the operator list is empty.
# - test_single_operand: Tests the case where the operand list has only one element.
# - test_large_numbers: Tests with large numbers to check for potential overflow issues.
# - test_zero_division: Tests division by zero (should handle gracefully).

# STEP 3: CODE
# pytest suite
def test_addition():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

def test_subtraction():
    operator = ['-', '-', '+']
    operand = [5, 2, 1]
    assert do_algebra(operator, operand) == 2

def test_multiplication():
    operator = ['*', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 24

def test_floor_division():
    operator = ['//', '//']
    operand = [10, 2, 5]
    assert do_algebra(operator, operand) == 1

def test_exponentiation():
    operator = ['**', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 4

def test_mixed_operations():
    operator = ['+', '*', '-', '**']
    operand = [1, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == 125

def test_empty_operator():
    operator = []
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 1

def test_single_operand():
    operator = ['+', '*']
    operand = [1, 2]
    assert do_algebra(operator, operand) == 1

def test_large_numbers():
    operator = ['*', '**']
    operand = [2**30, 2]
    assert do_algebra(operator, operand) == 2**32

def test_zero_division():
    operator = ['//']
    operand = [10, 0]
    assert do_algebra(operator, operand) == 0
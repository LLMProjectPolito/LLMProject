
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
### STEP 1: REASONING
# The function `do_algebra` takes a list of operators and a list of operands as input.
# It evaluates a mathematical expression using these operators and operands.
# The expression is built sequentially, applying each operator to the result of the previous operation.
# The tests should cover various scenarios, including different operators, operand values, and combinations of operations.
# We need to test edge cases like empty operator list, single operand, and different operator precedences.

### STEP 2: PLAN
# Test cases:
# 1. Basic addition, subtraction, multiplication, floor division, exponentiation.
# 2. Mixed operations.
# 3. Edge cases: empty operator list, single operand.
# 4. Larger numbers and exponentiation.
# 5. Floor division with zero.

# Test functions:
# - test_basic_operations: Tests basic arithmetic operations.
# - test_mixed_operations: Tests a combination of operations.
# - test_edge_cases: Tests edge cases like empty operator list and single operand.
# - test_large_numbers: Tests with larger numbers and exponentiation.
# - test_floor_division_zero: Tests floor division by zero.

### STEP 3: CODE
def test_basic_operations():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_mixed_operations():
    operator = ['+', '*', '//', '**']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 128

def test_edge_cases():
    operator = []
    operand = [2, 3]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

    operator = ['+']
    operand = [2]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_large_numbers():
    operator = ['*', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 256

def test_floor_division_zero():
    operator = ['//']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 0

def test_exponentiation_zero():
    operator = ['**']
    operand = [2, 0]
    assert do_algebra(operator, operand) == 1

def test_complex_expression():
    operator = ['+', '*', '-', '**', '//']
    operand = [10, 2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 100

def test_negative_numbers():
    operator = ['-', '*']
    operand = [-2, 3, 4]
    assert do_algebra(operator, operand) == -12

def test_multiple_operations_with_same_operand():
    operator = ['+', '*', '+', '//']
    operand = [1, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == 15
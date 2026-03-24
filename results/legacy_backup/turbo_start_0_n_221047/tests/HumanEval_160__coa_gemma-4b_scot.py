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
# The function `do_algebra` calculates the result of an algebraic expression given a list of operators and a list of operands.
# Boundary value testing should focus on edge cases like empty operand lists, single operand, or operators at the beginning/end of the lists.
# We need to test with the minimum and maximum possible operand values to ensure correct handling of edge cases.

# STEP 2: PLAN - List test functions names and scenarios.
# test_do_algebra_empty_operand
# test_do_algebra_single_operand
# test_do_algebra_operator_at_start
# test_do_algebra_operator_at_end

# STEP 3: CODE - Write the high-quality pytest suite.
def test_do_algebra_empty_operand():
    assert do_algebra(['+', '*'], []) == 0

def test_do_algebra_single_operand():
    assert do_algebra(['+', '*'], [5]) == 5

def test_do_algebra_operator_at_start():
    assert do_algebra(['+', '*'], [2, 3, 4, 5]) == 2 + 3 * 4 - 5

def test_do_algebra_operator_at_end():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 2 + 3 * 4 - 5

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
    assert do_algebra(['*', '//', '**'], [2, 3, 4, 5]) == 4
    assert do_algebra(['-', '+'], [5, 2, 3]) == 0
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['//'], [10, 2]) == 5

def test_operand_lengths():
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14
    assert do_algebra(['-', '//'], [5, 2, 3]) == 1
    assert do_algebra(['*', '**'], [2, 3, 4]) == 48
    assert do_algebra(['+', '-'], [1, 2, 3, 4]) == 0

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
# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `do_algebra` evaluates an algebraic expression given a list of operators and a list of operands.
# The tests should focus on verifying the correct application of each operator based on the input.
# We need to test different operator combinations and operand values to ensure the logic branches are handled correctly.

# STEP 2: PLAN - List test functions names and scenarios.
# test_addition: Tests addition operator.
# test_subtraction: Tests subtraction operator.
# test_multiplication: Tests multiplication operator.
# test_floor_division: Tests floor division operator.
# test_exponentiation: Tests exponentiation operator.
# test_mixed_operators: Tests a combination of different operators.

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_addition():
    operator = ['+', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 9

def test_subtraction():
    operator = ['-', '-', '+']
    operand = [5, 2, 3]
    assert do_algebra(operator, operand) == 0

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

def test_mixed_operators():
    operator = ['+', '*', '-', '**']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 24

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
# - test_empty_operator: Tests with an empty operator list.
# - test_single_operand: Tests with a single operand.
# - test_large_numbers: Tests with large numbers to check for potential overflow issues.
# - test_zero_division: Tests division by zero (should handle gracefully).

# STEP 3: CODE
#

### Test Suite
def test_addition():
    assert do_algebra(['+', '+'], [1, 2, 3]) == 6
    assert do_algebra(['+', '*'], [1, 2, 3, 4]) == 10

def test_subtraction():
    assert do_algebra(['-', '-'], [1, 2, 3, 4]) == -2
    assert do_algebra(['-', '*'], [1, 2, 3, 4]) == -2

def test_multiplication():
    assert do_algebra(['*', '*'], [1, 2, 3, 4]) == 24
    assert do_algebra(['*', '+'], [1, 2, 3, 4]) == 14

def test_floor_division():
    assert do_algebra(['//', '//'], [1, 2, 3, 4]) == 1
    assert do_algebra(['//', '*'], [1, 2, 3, 4]) == 0

def test_exponentiation():
    assert do_algebra(['**', '**'], [1, 2, 3, 4]) == 1
    assert do_algebra(['**', '*'], [1, 2, 3, 4]) == 6

def test_mixed_operations():
    assert do_algebra(['+', '*', '-'], [1, 2, 3, 4, 5]) == 14
    assert do_algebra(['*', '+', '-'], [1, 2, 3, 4, 5]) == 14

def test_empty_operator():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2, 3])

def test_single_operand():
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [1])

def test_large_numbers():
    assert do_algebra(['*', '*'], [1000, 1000, 1000, 1000]) == 1000000000

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//', '//'], [1, 0, 3, 4])
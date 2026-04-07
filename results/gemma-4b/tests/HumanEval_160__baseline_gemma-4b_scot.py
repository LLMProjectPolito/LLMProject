
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
# The tests should cover various scenarios, including different operators, operand values, and combinations of operators.
# We need to test edge cases like empty operator list, single operand, and different operator precedences.

### STEP 2: PLAN
# Test cases:
# 1. Basic addition, subtraction, multiplication, floor division, exponentiation.
# 2. Mixed operations.
# 3. Edge cases: empty operator list, single operand.
# 4. Larger numbers and exponentiation.
# 5. Floor division with zero (should not raise an error, but result in 0).

### STEP 3: CODE
def test_addition():
    assert do_algebra(['+', '+'], [2, 3]) == 5

def test_subtraction():
    assert do_algebra(['-', '-', ], [5, 2, 1]) == 2

def test_multiplication():
    assert do_algebra(['*', '*'], [2, 3, 4]) == 24

def test_floor_division():
    assert do_algebra(['//', '//'], [10, 2, 5]) == 1

def test_exponentiation():
    assert do_algebra(['**', '**'], [2, 3, 2]) == 4

def test_mixed_operations():
    assert do_algebra(['+', '*', '-', '**'], [2, 3, 4, 5, 2]) == 14

def test_large_numbers_exponentiation():
    assert do_algebra(['**'], [2, 10]) == 1024

def test_floor_division_zero():
    assert do_algebra(['//'], [10, 0]) == 0

def test_complex_expression():
    assert do_algebra(['+', '*', '-', '**'], [1, 2, 3, 4, 2]) == 14

def test_empty_operator_list():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2, 3])

def test_single_operand():
    with pytest.raises(IndexError):
        do_algebra(['+', '+'], [1])

def test_multiple_operators():
    assert do_algebra(['+', '*', '-', '**'], [1, 2, 3, 4, 2]) == 14

def test_different_operands():
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == 10
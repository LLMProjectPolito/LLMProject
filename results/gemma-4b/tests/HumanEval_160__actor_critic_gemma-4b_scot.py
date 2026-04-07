
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
# It iterates through the operators, applying each operation to the current result and the next operand.
# The function needs to handle addition, subtraction, multiplication, floor division, and exponentiation.
# The function should return the final result of the expression.

# STEP 2: PLAN - List test functions names and scenarios.
# test_basic_addition()
# test_basic_subtraction()
# test_basic_multiplication()
# test_basic_floor_division()
# test_basic_exponentiation()
# test_multiple_operations()
# test_edge_case_single_operand()
# test_edge_case_empty_operator()
# test_edge_case_large_numbers()
# test_edge_case_zero_operand()


# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_basic_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_basic_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_basic_multiplication():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_basic_floor_division():
    operator = ['//']
    operand = [10, 3]
    assert do_algebra(operator, operand) == 3

def test_basic_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_multiple_operations():
    operator = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 14

def test_edge_case_single_operand():
    operator = ['+']
    operand = [5]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_edge_case_empty_operator():
    operator = []
    operand = [2, 3]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_edge_case_large_numbers():
    operator = ['*']
    operand = [1000, 2000]
    assert do_algebra(operator, operand) == 2000000

def test_edge_case_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_complex_expression():
    operator = ['*', '+', '//']
    operand = [4, 2, 3, 1]
    assert do_algebra(operator, operand) == 11

def test_exponentiation_with_multiple_operations():
    operator = ['+', '**']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 83

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
import math


# Focus: Operator Precedence
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

def test_operator_precedence_multiplication_addition():
    assert do_algebra(['+', '*'], [2, 3, 4]) == 2 + 3 * 4

def test_operator_precedence_subtraction_multiplication():
    assert do_algebra(['*', '-'], [2, 3, 4]) == 2 * 3 - 4

def test_operator_precedence_exponentiation_addition():
    assert do_algebra(['+', '**'], [2, 3, 2]) == 2 + 3**2

# Focus: Empty/Invalid Input Lists
import pytest

def test_empty_operator_list():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2])

def test_empty_operand_list():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_operator_list_too_short():
    with pytest.raises(IndexError):
        do_algebra(['+'], [1, 2, 3])

# Focus: Large Numbers/Overflow
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

def test_large_numbers_addition():
    operators = ['+']
    operands = [10**10, 10**10]
    assert do_algebra(operators, operands) == 2 * (10**10)

def test_large_numbers_multiplication():
    operators = ['*']
    operands = [10**5, 10**5]
    assert do_algebra(operators, operands) == 10**10

def test_large_numbers_mixed_operations():
    operators = ['+', '*', '-', '**']
    operands = [2, 3, 4, 5]
    assert do_algebra(operators, operands) == (2 + 3 * 4) - 5**2
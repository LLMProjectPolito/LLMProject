
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

def test_operator_precedence_exponentiation_subtraction():
    assert do_algebra(['-', '**'], [2, 3, 2]) == 2 - 3 ** 2

def test_operator_precedence_multiple_operators():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 2 + 3 * 4 - 5

# Focus: Empty/Invalid Input Lists
import pytest

def test_empty_operator_list():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2])

def test_empty_operand_list():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_operand_list_with_one_element():
    with pytest.raises(IndexError):
        do_algebra(['+'], [1])

# Focus: Large Numbers/Overflow
import pytest

def test_large_number_addition():
    operators = ['+']
    operands = [10**18, 10**18]
    expected = 2 * (10**18)
    assert do_algebra(operators, operands) == expected

def test_large_number_multiplication():
    operators = ['*']
    operands = [10**9, 10**9]
    expected = 10**18
    assert do_algebra(operators, operands) == expected

def test_large_number_mixed_operations():
    operators = ['+', '*', '-', '//']
    operands = [10**9, 2, 10**9, 2]
    expected = (10**9 + 2 * 10**9) - (10**9 // 2)
    assert do_algebra(operators, operands) == expected
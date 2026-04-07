
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
from your_module import do_algebra  # Replace your_module

# Fixtures for common data
@pytest.fixture
def sample_operators():
    return ['+', '*', '-', '//', '**']

@pytest.fixture
def sample_operands():
    return [2, 3, 4, 5]

# Test cases for do_algebra
def test_do_algebra_addition(sample_operators, sample_operands):
    operators = ['+']
    operands = [2, 3]
    assert do_algebra(operators, operands) == 5

def test_do_algebra_subtraction(sample_operators, sample_operands):
    operators = ['-']
    operands = [5, 2]
    assert do_algebra(operators, operands) == 3

def test_do_algebra_multiplication(sample_operators, sample_operands):
    operators = ['*']
    operands = [2, 3]
    assert do_algebra(operators, operands) == 6

def test_do_algebra_floor_division(sample_operators, sample_operands):
    operators = ['//']
    operands = [10, 2]
    assert do_algebra(operators, operands) == 5

def test_do_algebra_exponentiation(sample_operators, sample_operands):
    operators = ['**']
    operands = [2, 3]
    assert do_algebra(operators, operands) == 8

def test_do_algebra_complex_expression(sample_operators, sample_operands):
    operators = ['+', '*', '-', '//']
    operands = [2, 3, 4, 5]
    assert do_algebra(operators, operands) == 9

def test_do_algebra_exponentiation_with_others(sample_operators, sample_operands):
    operators = ['+', '**']
    operands = [2, 3]
    assert do_algebra(operators, operands) == 11

def test_do_algebra_multiple_operators(sample_operators, sample_operands):
    operators = ['*', '+', '//']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 10

def test_do_algebra_long_expression(sample_operators, sample_operands):
    operators = ['+', '*', '-', '//', '**']
    operands = [2, 3, 4, 5, 6]
    assert do_algebra(operators, operands) == 27

def test_do_algebra_zero_operand(sample_operators, sample_operands):
    operators = ['+']
    operands = [0, 5]
    assert do_algebra(operators, operands) == 5

def test_do_algebra_negative_result(sample_operators, sample_operands):
    operators = ['-']
    operands = [2, 5]
    assert do_algebra(operators, operands) == -3

def test_do_algebra_large_numbers(sample_operators, sample_operands):
    operators = ['*']
    operands = [1000, 1000]
    assert do_algebra(operators, operands) == 1000000

def test_do_algebra_division_by_zero(sample_operators, sample_operands):
    operators = ['//']
    operands = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operators, operands)

def test_do_algebra_exponentiation_zero_base(sample_operators, sample_operands):
    operators = ['**']
    operands = [0, 5]
    assert do_algebra(operators, operands) == 0

def test_do_algebra_exponentiation_zero_exponent(sample_operators, sample_operands):
    operators = ['**']
    operands = [5, 0]
    assert do_algebra(operators, operands) == 1

# Test cases for is_palindrome
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Test cases for get_max
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
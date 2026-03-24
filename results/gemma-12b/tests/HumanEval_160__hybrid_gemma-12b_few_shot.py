
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
from your_module import do_algebra, is_palindrome, get_max  # Replace your_module

@pytest.fixture
def sample_operators():
    return ['+', '*', '-', '//', '**']

@pytest.fixture
def sample_operands():
    return [2, 3, 4, 5]

# do_algebra tests
def test_do_algebra_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_do_algebra_multiplication():
    operator = ['*']
    operand = [2, 4]
    assert do_algebra(operator, operand) == 8

def test_do_algebra_floor_division():
    operator = ['//']
    operand = [10, 2]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_do_algebra_complex_expression():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_multiple_operations():
    operator = ['+', '*', '//']
    operand = [2, 3, 4, 2]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_long_expression():
    operator = ['+', '*', '-', '//', '**']
    operand = [1, 2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 27

def test_do_algebra_zero_values():
    operator = ['+', '*']
    operand = [0, 5, 0]
    assert do_algebra(operator, operand) == 0

def test_do_algebra_large_numbers():
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

def test_do_algebra_mixed_operations():
    operator = ['*', '+', '//']
    operand = [2, 3, 6, 2]
    assert do_algebra(operator, operand) == 12

def test_do_algebra_negative_result():
    operator = ['-']
    operand = [5, 10]
    assert do_algebra(operator, operand) == -5

def test_do_algebra_division_by_one():
    operator = ['//']
    operand = [10, 1]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_exponentiation_zero():
    operator = ['**']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_exponentiation_one():
    operator = ['**']
    operand = [5, 1]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_addition_with_fixture():
    operators = ['+'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 14

def test_do_algebra_subtraction_with_fixture():
    operators = ['-'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == -1

def test_do_algebra_multiplication_with_fixture():
    operators = ['*'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 120

def test_do_algebra_floor_division_with_fixture():
    operators = ['//'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 0

def test_do_algebra_exponentiation_with_fixture():
    operators = ['**'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 1024

def test_do_algebra_mixed_operations_with_fixture():
    operators = ['+', '*', '-']
    assert do_algebra(operators, [2, 3, 4, 5]) == 9

def test_do_algebra_complex_expression_with_fixture():
    operators = ['+', '*', '//', '**']
    operands = [2, 3, 4, 5, 6]
    assert do_algebra(operators, operands) == 2 + 3 * 4 // 5 ** 6

def test_do_algebra_single_operand_list():
    operators = ['+'] * (len(sample_operands) - 1)
    operands = [10]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_do_algebra_empty_operator_list():
    operators = []
    operands = [5]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_do_algebra_zero_operands():
    operators = ['+']
    operands = []
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_do_algebra_large_numbers_with_fixture():
    operators = ['*'] * (len(sample_operands) - 1)
    operands = [1000, 2000, 3000]
    assert do_algebra(operators, operands) == 6000000

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Get Max tests
def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None
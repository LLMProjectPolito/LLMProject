
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
from your_module import is_palindrome
from your_module import get_max

# Fixtures
@pytest.fixture
def sample_operators():
    return ['+', '*', '-', '//', '**']

@pytest.fixture
def sample_operands():
    return [2, 3, 4, 5]

# do_algebra tests
def test_do_algebra_addition():
    """Tests with only addition operations."""
    operator = ['+'] * 3
    operand = [1, 2, 3, 4]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_subtraction():
    """Tests with only subtraction operations."""
    operator = ['-'] * 3
    operand = [10, 5, 2, 1]
    assert do_algebra(operator, operand) == 2

def test_do_algebra_multiplication():
    """Tests with only multiplication operations."""
    operator = ['*'] * 3
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 120

def test_do_algebra_floor_division():
    """Tests with only floor division operations."""
    operator = ['//'] * 3
    operand = [20, 5, 2, 1]
    assert do_algebra(operator, operand) == 2

def test_do_algebra_exponentiation():
    """Tests with only exponentiation operations."""
    operator = ['**'] * 3
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 1024

def test_do_algebra_mixed_operations():
    """Tests with a mix of addition, subtraction, multiplication, and floor division."""
    operator = ['+', '*', '-', '//']
    operand = [2, 3, 4, 5, 1]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_complex_expression():
    """Tests a more complex expression with multiple operations."""
    operator = ['+', '*', '-', '//', '**']
    operand = [2, 3, 4, 5, 2, 3]
    assert do_algebra(operator, operand) == 27

def test_do_algebra_zero_operands():
    """Tests with zero as an operand."""
    operator = ['+']
    operand = [0, 0]
    assert do_algebra(operator, operand) == 0

def test_do_algebra_large_numbers():
    """Tests with large numbers to ensure no overflow issues."""
    operator = ['*'] * 3
    operand = [1000, 1000, 1000]
    assert do_algebra(operator, operand) == 1000000000

def test_do_algebra_single_operation():
    """Tests with only one operation."""
    operator = ['+']
    operand = [5, 3]
    assert do_algebra(operator, operand) == 8

def test_do_algebra_negative_result():
    """Tests a case where the result is negative."""
    operator = ['-']
    operand = [5, 10]
    assert do_algebra(operator, operand) == -5

def test_do_algebra_long_expression():
    """Tests a longer expression with more operands and operators."""
    operator = ['+', '*', '-', '//', '**', '+', '*']
    operand = [1, 2, 3, 4, 5, 6, 7, 8]
    assert do_algebra(operator, operand) == 1024

def test_do_algebra_with_sample_operators_and_operands():
    """Tests using the sample fixtures."""
    operators = ['+'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 14

    operators = ['-'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == -1

    operators = ['*'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 120

    operators = ['//'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 0

    operators = ['**'] * (len(sample_operands) - 1)
    assert do_algebra(operators, sample_operands) == 1024

    operators = ['+', '*', '-']
    assert do_algebra([operators[0], operators[1], operators[2]], [2, 3, 4, 5]) == 9

def test_do_algebra_error_handling():
    """Tests for error conditions."""
    with pytest.raises(ValueError):
        do_algebra([], [5])  # Empty operator list
    with pytest.raises(ValueError):
        do_algebra(['+'], [])  # Empty operand list
    with pytest.raises(ValueError):
        do_algebra(['+'], [0]) # Single operand list

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False # Case sensitive

# Get Max tests
def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_duplicates():
    assert get_max([5, 5, 5]) == 5
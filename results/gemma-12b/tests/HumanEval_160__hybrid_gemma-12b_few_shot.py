import pytest
from your_module import do_algebra  # Replace your_module
from your_module import is_palindrome, get_max  # Assuming these are in your_module

@pytest.fixture
def sample_operators():
    return ['+', '*', '-', '//', '**']

@pytest.fixture
def sample_operands():
    return [2, 3, 4, 5]

@pytest.fixture
def large_operands():
    return [1000, 1000]

@pytest.fixture
def zero_operands():
    return [0, 5, 0]

@pytest.fixture
def long_operands():
    return [1, 2, 3, 4, 5, 6]

# do_algebra tests
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
    operators = ['+', '**', '-']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 35

def test_do_algebra_multiple_operators(sample_operators, sample_operands):
    operators = ['*', '+', '//']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 10

def test_do_algebra_long_expression(sample_operators, sample_operands):
    operators = ['+', '*', '-', '//', '**', '+']
    operands = [1, 2, 3, 4, 5, 6]
    assert do_algebra(operators, operands) == 721

def test_do_algebra_zero_values(zero_operands):
    operators = ['+', '*']
    operands = zero_operands
    assert do_algebra(operators, operands) == 0

def test_do_algebra_large_numbers(large_operands):
    operators = ['*']
    operands = large_operands
    assert do_algebra(operators, operands) == 1000000

def test_do_algebra_mixed_operations(sample_operators, sample_operands):
    operators = ['*', '+', '//']
    operands = [2, 3, 4, 2]
    assert do_algebra(operators, operands) == 10

def test_do_algebra_negative_result(sample_operators):
    operators = ['-']
    operands = [5, 10]
    assert do_algebra(operators, operands) == -5

def test_do_algebra_division_by_one(sample_operators):
    operators = ['//']
    operands = [10, 1]
    assert do_algebra(operators, operands) == 10

def test_do_algebra_exponentiation_zero(sample_operators):
    operators = ['**']
    operands = [5, 0]
    assert do_algebra(operators, operands) == 1

def test_do_algebra_exponentiation_one(sample_operators):
    operators = ['**']
    operands = [5, 1]
    assert do_algebra(operators, operands) == 5

def test_do_algebra_with_same_operators(sample_operators):
    operators = ['+', '+', '+']
    operands = [1, 2, 3]
    assert do_algebra(operators, operands) == 6

def test_do_algebra_with_floor_division_and_zero(sample_operators):
    operators = ['//']
    operands = [5, 0]
    assert do_algebra(operators, operands) == 0

def test_do_algebra_with_exponentiation_and_zero(sample_operators):
    operators = ['**']
    operands = [2, 0]
    assert do_algebra(operators, operands) == 1

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False  # Case sensitive

def test_palindrome_with_spaces():
    assert is_palindrome("A man, a plan, a canal: Panama") == False # Spaces are not ignored

# Max tests
def test_get_max_positive(sample_operands):
    assert get_max(sample_operands) == 5

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_duplicates():
    assert get_max([5, 5, 5]) == 5
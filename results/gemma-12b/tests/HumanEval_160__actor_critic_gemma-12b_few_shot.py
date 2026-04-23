
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
            if operand[i+1] == 0:
                return float('inf')  # Handle division by zero
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

@pytest.mark.parametrize("operator, operand, expected", [
    (['+'], [2, 3], 5),
    (['*'], [2, 3], 6),
    (['-'], [5, 2], 3),
    (['//'], [10, 2], 5),
    (['**'], [2, 3], 8),
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['+', '*', '//'], [2, 3, 4, 5], 11),
    (['-', '*', '//'], [5, 2, 3, 4], -1),
])
def test_do_algebra_basic(operator, operand, expected):
    """Tests basic algebraic operations."""
    assert do_algebra(operator, operand) == expected

def test_do_algebra_division_by_zero():
    """Tests division by zero handling."""
    assert do_algebra(['//'], [10, 0]) == float('inf')

def test_do_algebra_exponentiation_with_zero():
    """Tests exponentiation with zero."""
    assert do_algebra(['**'], [5, 0]) == 1
    assert do_algebra(['**'], [0, 5]) == 0

def test_do_algebra_exponentiation_with_negative_numbers():
    """Tests exponentiation with negative numbers."""
    assert do_algebra(['**'], [2, -2]) == 0.25
    assert do_algebra(['**'], [-2, 2]) == 4

def test_do_algebra_floor_division_with_negative_numbers():
    """Tests floor division with negative numbers."""
    assert do_algebra(['//'], [10, -3]) == -4
    assert do_algebra(['//'], [-10, 3]) == -4
    assert do_algebra(['//'], [-10, -3]) == 3

def test_do_algebra_large_numbers():
    """Tests with large numbers to check for potential overflow."""
    assert do_algebra(['*'], [1000000, 1000000]) == 1000000000000

def test_do_algebra_invalid_operator():
    """Tests handling of invalid operators.  This test expects any exception."""
    with pytest.raises(Exception):
        do_algebra(['$'], [2, 3])

def test_do_algebra_empty_operator_list():
    """Tests with an empty operator list (should raise an error)."""
    with pytest.raises(IndexError):
        do_algebra([], [2, 3])

def test_do_algebra_single_operand():
    """Tests with a single operand (should raise an error)."""
    with pytest.raises(IndexError):
        do_algebra(['+'], [2])

def test_do_algebra_exponentiation_with_negative_base_and_non_integer_exponent():
    """Tests exponentiation with a negative base and a non-integer exponent."""
    assert do_algebra(['**'], [-2, 0.5]) == 0.7071067811865476

def test_do_algebra_floor_division_with_non_integer_operands():
    """Tests floor division with non-integer operands."""
    assert do_algebra(['//'], [10.5, 3.2]) == 3
    assert do_algebra(['//'], [10, 3.2]) == 3

def test_do_algebra_long_chain():
    """Tests a longer chain of operations."""
    assert do_algebra(['+', '*', '-', '//', '**'], [2, 3, 4, 5, 2]) == 10
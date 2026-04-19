
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

def test_do_algebra_example():
    """Test the example provided in the docstring."""
    # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_basic_ops():
    """Test each basic operator individually."""
    assert do_algebra(['+'], [10, 5]) == 15
    assert do_algebra(['-'], [10, 5]) == 5
    assert do_algebra(['-'], [5, 10]) == -5
    assert do_algebra(['*'], [10, 5]) == 50
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_precedence():
    """Test mathematical order of operations (PEMDAS)."""
    # Power before Multiplication: 2 * (3**2) = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    # Power before Addition: 2 + (3**2) = 11
    assert do_algebra(['+', '**'], [2, 3, 2]) == 11
    # Multiplication before Addition: 1 + (2 * 3) = 7
    assert do_algebra(['+', '*'], [1, 2, 3]) == 7
    # Floor division before Addition: 5 + (10 // 2) = 10
    assert do_algebra(['+', '//'], [5, 10, 2]) == 10
    # Power before Floor Division: (2**3) // 2 = 4
    assert do_algebra(['**', '//'], [2, 3, 2]) == 4
    # Multiplication and Floor Division (left-to-right): (10 * 20) // 3 = 66
    assert do_algebra(['*', '//'], [10, 20, 3]) == 66

def test_do_algebra_complex_expressions():
    """Test longer sequences of mixed operators."""
    # 2**3 * 2 + 10 // 4 => 8 * 2 + 2 => 16 + 2 = 18
    assert do_algebra(['**', '*', '+', '//'], [2, 3, 2, 10, 4]) == 18
    # 10 - 2 * 3 + 4**2 // 2 => 10 - 6 + 16 // 2 => 10 - 6 + 8 = 12
    assert do_algebra(['-', '*', '+', '**', '//'], [10, 2, 3, 4, 2, 2]) == 12
    # 1 + 2 * 3 ** 2 // 4 - 5 => 1 + 2 * 9 // 4 - 5 => 1 + 18 // 4 - 5 => 1 + 4 - 5 = 0
    assert do_algebra(['+', '*', '**', '//', '-'], [1, 2, 3, 2, 4, 5]) == 0
    # 2 ** 3 * 2 // 10 + 5 => 8 * 2 // 10 + 5 => 16 // 10 + 5 => 1 + 5 = 6
    assert do_algebra(['**', '*', '//', '+'], [2, 3, 2, 10, 5]) == 6

def test_do_algebra_zeros():
    """Test behavior with zeros."""
    assert do_algebra(['*'], [0, 100]) == 0
    assert do_algebra(['+'], [0, 0]) == 0
    assert do_algebra(['**'], [0, 5]) == 0
    assert do_algebra(['**'], [5, 0]) == 1
    assert do_algebra(['**'], [0, 0]) == 1  # 0**0 is 1 in Python
    assert do_algebra(['*', '+'], [0, 10, 5]) == 5
    assert do_algebra(['+', '*'], [10, 0, 5]) == 10

def test_do_algebra_large_numbers():
    """Test with larger integers."""
    assert do_algebra(['+'], [10**12, 10**12]) == 2 * 10**12
    assert do_algebra(['*'], [10**6, 10**6]) == 10**12
    assert do_algebra(['**', '+'], [10, 5, 100]) == 100100

def test_do_algebra_constraints():
    """Test minimum requirements: 1 operator, 2 operands."""
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['-'], [1, 1]) == 0
    assert do_algebra(['*'], [1, 1]) == 1
    assert do_algebra(['//'], [1, 1]) == 1
    assert do_algebra(['**'], [1, 1]) == 1

@pytest.mark.parametrize("operators, operands, expected", [
    (['+'], [1, 1], 2),
    (['-'], [1, 1], 0),
    (['*'], [1, 1], 1),
    (['//'], [1, 1], 1),
    (['**'], [1, 1], 1),
    (['+', '+', '+'], [1, 1, 1, 1], 4),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    (['+', '-', '*', '//', '**'], [1, 1, 1, 1, 1, 1], 1), # 1+1-1*1//1**1 = 1
])
def test_do_algebra_parametrized(operators, operands, expected):
    """Parametrized tests for various simple combinations."""
    assert do_algebra(operators, operands) == expected
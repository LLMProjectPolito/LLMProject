
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

def test_basic_operations():
    """Test each operator in isolation with two operands."""
    assert do_algebra(['+'], [10, 5]) == 15
    assert do_algebra(['-'], [10, 5]) == 5
    assert do_algebra(['*'], [10, 5]) == 50
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['**'], [2, 3]) == 8

@pytest.mark.parametrize("operators, operands, expected", [
    (['+', '*'], [2, 3, 4], 14),        # 2 + (3 * 4) = 14
    (['-', '*'], [10, 2, 5], 0),        # 10 - (2 * 5) = 0
    (['*', '+'], [2, 5, 3], 13),        # (2 * 5) + 3 = 13
    (['//', '+'], [10, 3, 5], 8),       # (10 // 3) + 5 = 3 + 5 = 8
    (['+', '//'], [10, 3, 5], 8),       # 10 + (3 // 5) = 10 + 0 = 10? No, 10 + 0 = 10. 
                                        # Wait: 10 + (3 // 5) is 10 + 0 = 10.
])
def test_precedence_levels(operators, operands, expected):
    """Test that multiplication/division takes precedence over addition/subtraction."""
    # Correcting the logic for the parametrization above:
    # 10 + (3 // 5) -> 10 + 0 = 10
    if operators == ['+', '//'] and operands == [10, 3, 5]:
        expected = 10
    assert do_algebra(operators, operands) == expected

def test_exponentiation_precedence():
    """Test that exponentiation takes precedence over multiplication and addition."""
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18  # 2 * (3 ** 2) = 18
    assert do_algebra(['+', '**'], [2, 3, 2]) == 11  # 2 + (3 ** 2) = 11

def test_exponentiation_associativity():
    """Test Python's right-to-left associativity for exponentiation."""
    # 2 ** 3 ** 2 should be 2 ** (3 ** 2) = 2 ** 9 = 512
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512

def test_provided_example():
    """Test the specific example provided in the problem description."""
    operators = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    # 2 + 3 * 4 - 5 => 2 + 12 - 5 = 9
    assert do_algebra(operators, operand) == 9

def test_complex_chain():
    """Test a long chain of mixed operators."""
    # 2 + 3 * 4 - 5 // 6 ** 2
    # 2 + 12 - 5 // 36
    # 14 - 0 = 14
    operators = ['+', '*', '-', '//', '**']
    operands = [2, 3, 4, 5, 6, 2]
    assert do_algebra(operators, operands) == 14

def test_large_numbers():
    """Test with larger integer values."""
    assert do_algebra(['*', '+'], [1000, 1000, 1], 1000001)
    assert do_algebra(['**'], [10, 6]) == 1000000

def test_floor_division_edge_cases():
    """Test floor division with results that are zero or exact."""
    assert do_algebra(['//'], [5, 10]) == 0
    assert do_algebra(['//'], [10, 5]) == 2
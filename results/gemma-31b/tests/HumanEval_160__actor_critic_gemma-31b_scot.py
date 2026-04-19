
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

# The function do_algebra is assumed to be defined in the environment.

@pytest.mark.parametrize("operators, operands, expected", [
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
])
def test_basic_operations(operators, operands, expected):
    """Test each supported operator in isolation."""
    assert do_algebra(operators, operands) == expected

def test_operator_precedence():
    """Test that Python's operator precedence (PEMDAS) is respected."""
    # 2 + 3 * 4 = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14
    # 2 * 3 ** 2 = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    # 10 - 2 * 3 = 4
    assert do_algebra(['-', '*'], [10, 2, 3]) == 4

def test_exponentiation_associativity():
    """Test that exponentiation is right-associative (2**3**2 == 2**(3**2) == 512)."""
    # 2 ** 3 ** 2 should be 512, not (2**3)**2 = 64
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512

def test_example_case():
    """Test the specific example provided in the problem description."""
    operators = ['+', '*', '-']
    operands = [2, 3, 4, 5]
    # Expression: 2 + 3 * 4 - 5 = 9
    assert do_algebra(operators, operands) == 9

def test_minimum_input():
    """Test the smallest valid input size (1 operator, 2 operands)."""
    assert do_algebra(['+'], [0, 0]) == 0
    assert do_algebra(['-'], [0, 1]) == -1

def test_division_by_zero():
    """Test that floor division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])
    with pytest.raises(ZeroDivisionError):
        do_algebra(['+', '//'], [5, 2, 0])

def test_large_numbers():
    """Test the function with large integers."""
    assert do_algebra(['*'], [10**6, 10**6]) == 10**12
    assert do_algebra(['**'], [2, 10]) == 1024

def test_complex_expression():
    """Test a longer chain of mixed operators."""
    # 10 + 2 ** 3 // 2 * 3 - 1
    # 10 + 8 // 2 * 3 - 1 -> 10 + 4 * 3 - 1 -> 10 + 12 - 1 = 21
    operators = ['+', '**', '//', '*', '-']
    operands = [10, 2, 3, 2, 3, 1]
    assert do_algebra(operators, operands) == 21

def test_negative_operands_floor_division():
    """Test that floor division behaves correctly with negative numbers (rounds down)."""
    # -10 // 3 in Python is -4, not -3
    assert do_algebra(['//'], [-10, 3]) == -4
    assert do_algebra(['//'], [10, -3]) == -4

def test_floating_point_operands():
    """Test if the function supports floating point numbers using pytest.approx for precision."""
    # 1.5 + 2.5 = 4.0
    assert do_algebra(['+'], [1.5, 2.5]) == pytest.approx(4.0)
    # 2.0 ** 3.0 = 8.0
    assert do_algebra(['**'], [2.0, 3.0]) == pytest.approx(8.0)
    # 1.1 + 2.2 = 3.3 (classic float precision test)
    assert do_algebra(['+'], [1.1, 2.2]) == pytest.approx(3.3)

def test_exponentiation_edge_cases():
    """Test negative exponents and zero-based exponentiation."""
    # Negative exponent: 2 ** -1 = 0.5
    assert do_algebra(['**'], [2, -1]) == pytest.approx(0.5)
    # Zero exponent: 0 ** 0 = 1 in Python
    assert do_algebra(['**'], [0, 0]) == 1
    # Zero base with negative exponent: 0 ** -1 should raise ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        do_algebra(['**'], [0, -1])

def test_mismatched_input_lengths():
    """Test that mismatched lengths of operators and operands raise ValueError."""
    # Too many operators
    with pytest.raises(ValueError):
        do_algebra(['+', '-'], [1, 2])
    # Too many operands
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])

def test_unsupported_operators():
    """Test that unsupported operators raise a ValueError or TypeError."""
    # '/' is not in the supported list (only '//')
    with pytest.raises((ValueError, TypeError)):
        do_algebra(['/'], [10, 2])
    # '^' is not a valid Python exponentiation operator
    with pytest.raises((ValueError, TypeError)):
        do_algebra(['^'], [2, 3])

def test_empty_and_single_inputs():
    """
    Test behavior with empty lists or single operands.
    Per spec: Operator list has at least one operator, operand list has at least two.
    """
    with pytest.raises(ValueError):
        do_algebra([], [])
    with pytest.raises(ValueError):
        do_algebra([], [1])

def test_invalid_operand_types():
    """Test that non-numeric operands raise a TypeError."""
    with pytest.raises(TypeError):
        do_algebra(['+'], ["1", 2])
    with pytest.raises(TypeError):
        do_algebra(['*'], [None, 5])

def test_negative_result():
    """Test expressions that result in negative numbers."""
    assert do_algebra(['-'], [5, 10]) == -5
    assert do_algebra(['-', '*'], [2, 3, 4]) == -10 # 2 - 12
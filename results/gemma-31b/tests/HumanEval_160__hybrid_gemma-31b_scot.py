
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

# The function do_algebra is already defined in the environment.
# We are testing the implementation of:
# def do_algebra(operators, operands): ...

class TestDoAlgebra:
    """
    Superior merged test suite for the do_algebra function.
    Covers basic operations, Python operator precedence, associativity, 
    edge cases, and error handling.
    """

    @pytest.mark.parametrize("operators, operands, expected", [
        (['+'], [10, 5], 15),            # Simple Addition
        (['-'], [10, 5], 5),             # Simple Subtraction
        (['*'], [10, 5], 50),            # Simple Multiplication
        (['//'], [10, 3], 3),            # Simple Floor Division
        (['**'], [2, 3], 8),             # Simple Exponentiation
    ])
    def test_basic_operations(self, operators, operands, expected):
        """Test each basic operator in isolation."""
        assert do_algebra(operators, operands) == expected

    def test_docstring_example(self):
        """Test the specific example provided in the function docstring."""
        # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    @pytest.mark.parametrize("operators, operands, expected", [
        (['+', '*'], [2, 3, 4], 14),     # 2 + (3 * 4) = 14
        (['*', '+'], [2, 3, 4], 10),     # (2 * 3) + 4 = 10
        (['*', '**'], [2, 3, 2], 18),    # 2 * (3 ** 2) = 18
        (['**', '*'], [2, 3, 2], 16),    # (2 ** 3) * 2 = 16
        (['+', '//'], [10, 5, 2], 12),   # 10 + (5 // 2) = 12
        (['//', '+'], [10, 5, 2], 4),    # (10 // 5) + 2 = 4
        (['-', '**'], [10, 2, 3], 2),    # 10 - (2 ** 3) = 2
        (['**', '-'], [2, 3, 1], 7),     # (2 ** 3) - 1 = 7
    ])
    def test_operator_precedence(self, operators, operands, expected):
        """Test that Python's mathematical order of operations is respected."""
        assert do_algebra(operators, operands) == expected

    def test_associativity(self):
        """Test that operators follow correct associativity rules."""
        # Exponentiation is right-associative: 2**2**3 == 2**(2**3) == 2**8 == 256
        assert do_algebra(['**', '**'], [2, 2, 3]) == 256
        
        # Subtraction is left-associative: 10-5-2 == (10-5)-2 == 3
        assert do_algebra(['-', '-'], [10, 5, 2]) == 3
        
        # Floor division is left-associative: 12//3//2 == (12//3)//2 == 2
        assert do_algebra(['//', '//'], [12, 3, 2]) == 2

    @pytest.mark.parametrize("operators, operands, expected", [
        (['+', '*', '**', '//', '-'], [10, 2, 3, 2, 4, 1], 13), 
        # 10 + 2 * (3**2) // 4 - 1 => 10 + 18 // 4 - 1 => 10 + 4 - 1 = 13
        (['**', '+', '//', '*', '-'], [2, 3, 10, 3, 2, 1], 13),
        # (2**3) + (10 // 3) * 2 - 1 => 8 + 3 * 2 - 1 => 8 + 6 - 1 = 13
    ])
    def test_complex_expressions(self, operators, operands, expected):
        """Test complex chains of mixed operators."""
        assert do_algebra(operators, operands) == expected

    @pytest.mark.parametrize("operators, operands, expected", [
        (['+'], [0, 0], 0),              # Zeroes
        (['*'], [0, 10], 0),             # Multiplication by zero
        (['//'], [1, 2], 0),             # Floor division resulting in 0
        (['**'], [5, 0], 1),             # Exponentiation to power of 0
        (['**'], [0, 5], 0),             # Zero to power of positive
        (['*', '+'], [0, 5, 10], 10),    # (0 * 5) + 10 = 10
    ])
    def test_zero_edge_cases(self, operators, operands, expected):
        """Test behavior with zeros as operands and exponents."""
        assert do_algebra(operators, operands) == expected

    def test_division_by_zero(self):
        """Test that floor division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [10, 0])
        
        with pytest.raises(ZeroDivisionError):
            do_algebra(['+', '//'], [5, 2, 0])

    def test_large_numbers(self):
        """Test with larger integers to ensure stability."""
        # 2**10 + 100 = 1024 + 100 = 1124
        assert do_algebra(['**', '+'], [2, 10, 100]) == 1124

    def test_minimum_input(self):
        """Test the minimum allowed input size (1 operator, 2 operands)."""
        assert do_algebra(['+'], [1, 1]) == 2

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
    Implementation provided for the sake of the test suite.
    Constructs a string expression and evaluates it using Python's eval.
    """
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += f" {operator[i]} {operand[i+1]}"
    return eval(expression)

class TestDoAlgebra:
    """
    Blue Team QA Suite for do_algebra.
    Focuses on operator precedence, edge cases, and mathematical constraints.
    """

    @pytest.mark.parametrize("operators, operands, expected", [
        # Basic Example from prompt
        (['+', '*', '-'], [2, 3, 4, 5], 9), 
        # Simple addition/subtraction
        (['+', '+'], [1, 2, 3], 6),
        (['-', '-'], [10, 5, 2], 3),
        # Operator Precedence: Multiplication before Addition
        (['+', '*'], [1, 2, 3], 7), 
        # Operator Precedence: Exponentiation before Multiplication
        (['*', '**'], [2, 3, 2], 18), # 2 * (3**2) = 18
        # Operator Precedence: Exponentiation before Floor Division
        (['//', '**'], [100, 2, 3], 11), # 100 // (2**3) = 100 // 8 = 12? No, 100//8 = 12. 
        # Wait, 100 // 8 is 12. Let's use a clearer one:
        (['//', '**'], [64, 2, 3], 8), # 64 // 8 = 8
        # Floor Division behavior
        (['//'], [10, 3], 3),
        (['//'], [5, 2], 2),
        # Exponentiation
        (['**'], [2, 10], 1024),
        (['**'], [5, 0], 1),
        # Complex chain
        (['**', '*', '//', '+'], [2, 3, 4, 2, 1], 17), # (2**3 * 4 // 2) + 1 = (8 * 4 // 2) + 1 = 17
        # Minimum constraints (1 operator, 2 operands)
        (['+'], [1, 1], 2),
        (['-'], [1, 1], 0),
        # Zeroes
        (['+', '*'], [0, 0, 0], 0),
        (['*'], [0, 100], 0),
    ])
    def test_functional_correctness(self, operators, operands, expected):
        """Test various combinations of operators and operands for mathematical correctness."""
        assert do_algebra(operators, operands) == expected

    def test_division_by_zero(self):
        """Ensure that floor division by zero raises the appropriate Python exception."""
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [10, 0])

    def test_large_numbers(self):
        """Test the function with larger integers to check for overflow or performance issues."""
        # 10**5 is large but manageable
        assert do_algebra(['**'], [10, 5], 100000)

    def test_operator_precedence_deep(self):
        """
        Verify strict adherence to PEMDAS.
        Expression: 2 + 3 * 4 ** 2 // 8 - 1
        Calculation: 
        1. 4**2 = 16
        2. 3 * 16 = 48
        3. 48 // 8 = 6
        4. 2 + 6 - 1 = 7
        """
        operators = ['+', '*', '**', '//', '-']
        operands = [2, 3, 4, 2, 8, 1]
        assert do_algebra(operators, operands) == 7

    def test_type_consistency(self):
        """Ensure the result is an integer given the constraints (non-negative ints and //)."""
        result = do_algebra(['//', '+'], [10, 3, 1])
        assert isinstance(result, int)

    @pytest.mark.parametrize("bad_ops, bad_operands", [
        # Testing if the function handles mismatched lengths (though prompt says they are equal)
        (['+'], [1]), 
        (['+', '*'], [1, 2]),
    ])
    def test_mismatched_lengths(self, bad_ops, bad_operands):
        """
        Test how the function handles inputs that violate the length constraint.
        Depending on implementation, this might raise IndexError.
        """
        with pytest.raises((IndexError, SyntaxError)):
            do_algebra(bad_ops, bad_operands)
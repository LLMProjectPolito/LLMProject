
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
    """
    # Construct the expression string by interleaving operands and operators
    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i]) + " " + operator[i] + " "
    expression += str(operand[-1])
    
    # eval() follows standard Python operator precedence:
    # ** (Exponentiation) -> * / // % (Multiplication/Division) -> + - (Addition/Subtraction)
    return eval(expression)

class TestDoAlgebra:
    """
    Superior test suite for do_algebra function.
    Combines functional scenarios, operator precedence, edge cases, and error handling.
    """

    @pytest.mark.parametrize("operators, operands, expected", [
        # --- Basic Operations (Single Operator) ---
        (['+'], [10, 20], 30),
        (['-'], [10, 20], -10),
        (['*'], [10, 20], 200),
        (['//'], [20, 3], 6),
        (['**'], [2, 3], 8),
        
        # --- Problem Description Example ---
        (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + (3 * 4) - 5 = 2 + 12 - 5 = 9
        
        # --- Operator Precedence: Multiplication/Division before Addition/Subtraction ---
        (['+', '*'], [2, 3, 4], 14),       # 2 + (3 * 4) = 14
        (['*', '+'], [2, 3, 4], 10),       # (2 * 3) + 4 = 10
        (['-', '//'], [10, 10, 2], 5),     # 10 - (10 // 2) = 10 - 5 = 5
        (['//', '-'], [10, 2, 3], 2),      # (10 // 2) - 3 = 5 - 3 = 2
        (['//', '+'], [10, 2, 5], 10),     # (10 // 2) + 5 = 10
        (['+', '//'], [5, 10, 2], 10),     # 5 + (10 // 2) = 10
        
        # --- Operator Precedence: Exponentiation before Multiplication/Division ---
        (['*', '**'], [2, 3, 2], 18),      # 2 * (3 ** 2) = 2 * 9 = 18
        (['**', '*'], [2, 3, 2], 16),      # (2 ** 3) * 2 = 8 * 2 = 16
        (['**', '//'], [2, 3, 4], 2),      # (2 ** 3) // 4 = 8 // 4 = 2
        (['+', '**'], [2, 3, 2], 11),      # 2 + (3 ** 2) = 2 + 9 = 11
        
        # --- Right-Associativity of Exponentiation ---
        (['**', '**'], [2, 3, 2], 512),    # 2 ** (3 ** 2) = 2 ** 9 = 512
        
        # --- Complex Mixed Expressions ---
        (['**', '*', '+', '//'], [2, 3, 2, 10, 4], 18), # (2**3 * 2) + (10 // 4) = 16 + 2 = 18
        (['-', '*', '**'], [10, 2, 3, 2], -8),           # 10 - (2 * 3**2) = 10 - 18 = -8
        
        # --- Edge Cases: Zeros ---
        (['+', '*'], [0, 0, 0], 0),
        (['**'], [0, 5], 0),
        (['**'], [5, 0], 1),               # Any non-zero to power 0 is 1
        (['//'], [0, 5], 0),
        
        # --- Edge Cases: Large Numbers ---
        (['*'], [1000000, 1000000], 1000000000000),
        (['**'], [2, 10], 1024),
    ])
    def test_do_algebra_success(self, operators, operands, expected):
        """Tests various valid combinations of operators and operands."""
        assert do_algebra(operators, operands) == expected

    def test_do_algebra_long_chain(self):
        """Test a long chain of the same operator to ensure stability and linear processing."""
        operators = ['+'] * 9
        operands = [1] * 10
        assert do_algebra(operators, operands) == 10

    def test_do_algebra_subtraction_chain(self):
        """Test sequential subtraction to ensure left-to-right evaluation for same-precedence ops."""
        operators = ['-', '-', '-']
        operands = [100, 10, 10, 10]
        # 100 - 10 - 10 - 10 = 70
        assert do_algebra(operators, operands) == 70

    def test_do_algebra_floor_division_precision(self):
        """Ensure floor division is strictly used and returns an integer."""
        operators = ['//']
        operands = [7, 2]
        result = do_algebra(operators, operands)
        assert result == 3
        assert isinstance(result, int)

    def test_division_by_zero(self):
        """Tests that floor division by zero raises a ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [10, 0])

    def test_invalid_operator(self):
        """Tests that an invalid operator string causes a SyntaxError via eval()."""
        with pytest.raises(SyntaxError):
            do_algebra(['@'], [10, 5])

    def test_mismatched_lengths_behavior(self):
        """Tests that mismatched operator/operand lengths cause a SyntaxError."""
        # One operator, three operands -> "1 + 2 3" -> SyntaxError
        with pytest.raises(SyntaxError):
            do_algebra(['+'], [1, 2, 3])

    def test_minimum_input_size(self):
        """Tests the minimum constraints: 1 operator, 2 operands."""
        assert do_algebra(['+'], [1, 1]) == 2
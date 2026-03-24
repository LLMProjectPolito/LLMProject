# STEP 1: REASONING
# The function `do_algebra` constructs and evaluates an algebraic expression from two lists: `operator` and `operand`.
# The `operator` list contains strings representing basic algebraic operations (+, -, *, //, **).
# The `operand` list contains non-negative integers.
# The length of `operator` is one less than the length of `operand`.
# The goal is to create a comprehensive pytest suite to test various scenarios, including:
# - Valid input combinations with different operators and operands.
# - Edge cases with small operands.
# - Cases involving exponentiation.
# - Cases involving floor division.
# - Invalid input scenarios (although the problem statement specifies valid input, it's good practice to consider them).
# - Cases with zero operands.

# STEP 2: PLAN
# Test functions:
# - test_addition: Tests addition operations.
# - test_subtraction: Tests subtraction operations.
# - test_multiplication: Tests multiplication operations.
# - test_floor_division: Tests floor division operations.
# - test_exponentiation: Tests exponentiation operations.
# - test_mixed_operations: Tests a combination of different operations.
# - test_small_operands: Tests with small integer operands.
# - test_zero_operands: Tests with zero as operands.
# - test_long_expression: Tests a longer expression with multiple operations.

# STEP 3: CODE
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
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += " " + operator[i] + " " + str(operand[i+1])
    return eval(expression)

class TestDoAlgebra:
    def test_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5
        assert do_algebra(['+', '+'], [2, 3, 4]) == 9
        assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3
        assert do_algebra(['-', '-'], [10, 3, 2]) == 5
        assert do_algebra(['-', '-', '-'], [10, 5, 2, 1]) == 2

    def test_multiplication(self):
        assert do_algebra(['*'], [2, 3]) == 6
        assert do_algebra(['*', '*'], [2, 3, 4]) == 24
        assert do_algebra(['*', '*', '*', '*'], [1, 2, 3, 4, 5]) == 120

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5
        assert do_algebra(['//', '//'], [15, 3, 2]) == 2
        assert do_algebra(['//', '//', '//'], [20, 4, 2, 1]) == 2

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['**', '**'], [2, 3, 2]) == 36
        assert do_algebra(['**', '**', '**'], [2, 3, 2, 3]) == 216

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8
        assert do_algebra(['-', '*', '+', '//'], [10, 2, 3, 4, 2]) == 4

    def test_small_operands(self):
        assert do_algebra(['+'], [1, 1]) == 2
        assert do_algebra(['-'], [2, 1]) == 1
        assert do_algebra(['*'], [1, 1]) == 1
        assert do_algebra(['//'], [2, 1]) == 2
        assert do_algebra(['**'], [1, 2]) == 1

    def test_zero_operands(self):
        assert do_algebra(['+'], [0, 5]) == 5
        assert do_algebra(['-'], [5, 0]) == 5
        assert do_algebra(['*'], [0, 5]) == 0
        assert do_algebra(['//'], [5, 0]) == float('inf') # or raise ZeroDivisionError
        assert do_algebra(['**'], [0, 2]) == 0
        assert do_algebra(['**'], [2, 0]) == 1

    def test_long_expression(self):
        assert do_algebra(['+', '*', '//', '-'], [1, 2, 3, 4, 5]) == 4
        assert do_algebra(['*', '+', '**', '//'], [2, 3, 4, 2, 3]) == 20

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

# STEP 1: REASONING
# The function `do_algebra` constructs and evaluates an algebraic expression from two lists: `operator` and `operand`.
# The `operator` list contains strings representing basic algebraic operations (+, -, *, //, **).
# The `operand` list contains non-negative integers.
# The length of `operator` is one less than the length of `operand`.
# The goal is to create a pytest suite to thoroughly test this function, covering various scenarios, including:
# - Basic arithmetic operations with positive integers.
# - Operations with zero.
# - Floor division behavior.
# - Exponentiation.
# - Edge cases: small and large operands, long operator/operand lists.
# - Error handling (although the prompt doesn't explicitly require it, it's good practice to consider).

# STEP 2: PLAN
# Test functions:
# - test_addition: Tests basic addition.
# - test_subtraction: Tests basic subtraction.
# - test_multiplication: Tests basic multiplication.
# - test_floor_division: Tests floor division.
# - test_exponentiation: Tests exponentiation.
# - test_mixed_operations: Tests a combination of operations.
# - test_zero_operands: Tests scenarios involving zero operands.
# - test_large_operands: Tests with larger integer operands.
# - test_long_lists: Tests with longer operator and operand lists.
# - test_floor_division_by_zero: Tests floor division by zero (expecting ZeroDivisionError).
# - test_exponentiation_negative_operand: Tests exponentiation with a negative operand (expecting TypeError).

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
        assert do_algebra(['+'], [10, 5]) == 15

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3
        assert do_algebra(['-'], [10, 3]) == 7

    def test_multiplication(self):
        assert do_algebra(['*'], [2, 3]) == 6
        assert do_algebra(['*'], [5, 4]) == 20

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 3]) == 3
        assert do_algebra(['//'], [15, 5]) == 3

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['**'], [3, 2]) == 9

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert do_algebra(['*', '+', '//'], [2, 3, 4, 5]) == 11

    def test_zero_operands(self):
        assert do_algebra(['+'], [0, 5]) == 5
        assert do_algebra(['-'], [5, 0]) == 5
        assert do_algebra(['*'], [0, 5]) == 0
        assert do_algebra(['//'], [5, 0]) == 5 # floor division with 0 operand

    def test_large_operands(self):
        assert do_algebra(['+'], [1000, 2000]) == 3000
        assert do_algebra(['*'], [100, 100]) == 10000

    def test_long_lists(self):
        operators = ['+', '*', '-', '//', '**']
        operands = [1, 2, 3, 4, 5, 6]
        assert do_algebra(operators, operands) == 719

    def test_floor_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [5, 0])

    def test_exponentiation_negative_operand(self):
        with pytest.raises(TypeError):
            do_algebra(['**'], [-2, 3])
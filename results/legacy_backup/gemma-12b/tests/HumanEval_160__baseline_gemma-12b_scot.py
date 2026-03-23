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
# - Invalid input (although the prompt specifies valid input, testing invalid input can reveal potential vulnerabilities).

# STEP 2: PLAN
# Test functions:
# - test_addition: Tests basic addition.
# - test_subtraction: Tests basic subtraction.
# - test_multiplication: Tests basic multiplication.
# - test_floor_division: Tests floor division.
# - test_exponentiation: Tests exponentiation.
# - test_mixed_operations: Tests a combination of operations.
# - test_zero_operands: Tests operations involving zero.
# - test_large_operands: Tests operations with larger numbers.
# - test_long_lists: Tests with longer operator and operand lists.
# - test_single_operator: Tests with a single operator.
# - test_negative_result: Tests cases that result in negative numbers (although operands are non-negative, the result might be negative).

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
        assert do_algebra(['+'], [0, 5]) == 5

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3
        assert do_algebra(['-', '-'], [5, 2, 1]) == 2
        assert do_algebra(['-'], [5, 0]) == 5

    def test_multiplication(self):
        assert do_algebra(['*'], [2, 3]) == 6
        assert do_algebra(['*', '*',], [2, 3, 4]) == 24
        assert do_algebra(['*'], [5, 0]) == 0

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5
        assert do_algebra(['//'], [10, 3]) == 3
        assert do_algebra(['//'], [5, 2]) == 2
        assert do_algebra(['//'], [5, 5]) == 1

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['**'], [2, 2]) == 4
        assert do_algebra(['**'], [3, 2]) == 9

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8
        assert do_algebra(['-', '*', '+'], [10, 2, 3, 1]) == 9

    def test_zero_operands(self):
        assert do_algebra(['+'], [0, 0]) == 0
        assert do_algebra(['-'], [0, 0]) == 0
        assert do_algebra(['*'], [0, 0]) == 0
        assert do_algebra(['//'], [0, 1]) == 0
        assert do_algebra(['**'], [0, 2]) == 0

    def test_large_operands(self):
        assert do_algebra(['+'], [1000, 2000]) == 3000
        assert do_algebra(['*'], [100, 100]) == 10000

    def test_long_lists(self):
        operators = ['+', '*', '-', '//', '**'] * 2
        operands = [1, 2, 3, 4, 5] * 2
        assert do_algebra(operators, operands) == 1 + 2 * 3 - 4 // 5 ** 1 + 2 * 3 - 4 // 5 ** 1

    def test_single_operator(self):
        assert do_algebra(['+'], [1, 2]) == 3
        assert do_algebra(['-'], [5, 2]) == 3
        assert do_algebra(['*'], [3, 4]) == 12
        assert do_algebra(['//'], [8, 2]) == 4
        assert do_algebra(['**'], [2, 3]) == 8

    def test_negative_result(self):
        assert do_algebra(['-'], [2, 5]) == -3
        assert do_algebra(['-'], [10, 20]) == -10
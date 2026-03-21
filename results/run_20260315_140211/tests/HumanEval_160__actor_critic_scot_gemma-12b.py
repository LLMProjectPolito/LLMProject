import pytest
import ast

def do_algebra(operator, values):
    """
    Given two lists operator, and values. The first list has basic algebra operations, and 
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
        The length of operator list is equal to the length of values list minus one.
        Values is a list of of non-negative integers.
        Operator list has at least one operator, and values list has at least two values.

    """
    expression = str(values[0])
    for i in range(len(operator)):
        expression = f"{expression} {operator[i]} {values[i+1]}"
    try:
        return ast.literal_eval(expression)
    except (ValueError, SyntaxError) as e:
        print(f"Error evaluating expression: {expression}. Error: {e}")
        return None


class TestDoAlgebra:
    def test_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3

    def test_multiplication(self):
        assert do_algebra(['*'], [2, 4]) == 8

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8

    def test_combined_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    def test_order_of_operations(self):
        assert do_algebra(['*', '+'], [2, 3, 4]) == 14  # 2 * (3 + 4)

    def test_longer_expression(self):
        assert do_algebra(['+', '*', '//', '-'], [1, 2, 3, 4, 5]) == 2  # (1 + 2) * (3 // 4) - 5

    def test_large_numbers(self):
        assert do_algebra(['+'], [1000000, 2000000]) == 3000000

    def test_floor_division_by_zero(self):
        assert do_algebra(['//'], [10, 0]) is None

    def test_zero_exponent(self):
        assert do_algebra(['**'], [5, 0]) == 1

    def test_negative_numbers(self):
        assert do_algebra(['+'], [-2, 3]) == 1

    def test_zero_values_addition(self):
        assert do_algebra(['+', '0', '+'], [2, 0, 5]) == 7

    def test_zero_values_multiplication(self):
        assert do_algebra(['*', '0', '+'], [2, 0, 5]) == 0

    def test_invalid_syntax(self):
        assert do_algebra(['+'], [2, 'a']) is None

    def test_invalid_operator(self):
        assert do_algebra(['$'], [2, 3]) is None
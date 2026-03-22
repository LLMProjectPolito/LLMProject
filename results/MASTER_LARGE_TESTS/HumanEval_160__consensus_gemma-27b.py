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
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

class TestDoAlgebra:

    def test_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3

    def test_multiplication(self):
        assert do_algebra(['*'], [4, 3]) == 12

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8

    def test_complex_expression(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    def test_multiple_operations(self):
        assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

    def test_zero_operand(self):
        assert do_algebra(['+'], [0, 5]) == 5
        assert do_algebra(['*'], [0, 5]) == 0

    def test_large_numbers(self):
        assert do_algebra(['+'], [1000000, 2000000]) == 3000000

    def test_mixed_operations(self):
        assert do_algebra(['*', '+', '-'], [2, 3, 4, 1]) == 7

    def test_division_by_one(self):
        assert do_algebra(['//'], [10, 1]) == 10

    def test_exponentiation_with_zero(self):
        assert do_algebra(['**'], [2, 0]) == 1

    def test_long_expression(self):
        operators = ['+', '-', '*', '//', '+', '**']
        operands = [1, 2, 3, 4, 5, 2]
        assert do_algebra(operators, operands) == 1

    def test_all_additions(self):
        operators = ['+', '+', '+']
        operands = [1, 2, 3, 4]
        assert do_algebra(operators, operands) == 10

    def test_do_algebra_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5

    def test_do_algebra_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3

    def test_do_algebra_multiplication(self):
        assert do_algebra(['*'], [2, 3]) == 6

    def test_do_algebra_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5

    def test_do_algebra_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8

    def test_do_algebra_complex_expression_2(self):
        assert do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8

    def test_do_algebra_complex_expression_3(self):
        assert do_algebra(['**', '-', '+'], [2, 3, 4, 1]) == 13

    def test_do_algebra_with_zero(self):
        assert do_algebra(['+', '-', '*'], [0, 1, 2, 3]) == 1

    def test_do_algebra_with_large_numbers(self):
        assert do_algebra(['+', '*', '-'], [100, 200, 3, 50]) == 650

    def test_do_algebra_multiple_operations(self):
        assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

    def test_do_algebra_multiple_subtractions(self):
        assert do_algebra(['-', '-', '-'], [5, 1, 2, 1]) == 1

    def test_do_algebra_mixed_operations(self):
        assert do_algebra(['+', '*', '-', '//'], [1, 2, 3, 6]) == 2

    def test_do_algebra_exponentiation_and_addition(self):
        assert do_algebra(['**', '+'], [2, 3, 1]) == 9

    def test_do_algebra_exponentiation_and_subtraction(self):
        assert do_algebra(['**', '-'], [2, 3, 1]) == 7
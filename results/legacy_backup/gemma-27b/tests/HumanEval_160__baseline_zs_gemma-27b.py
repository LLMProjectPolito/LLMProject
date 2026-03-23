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

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    def test_longer_expression(self):
        assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

    def test_zero_operand(self):
        assert do_algebra(['+'], [0, 5]) == 5
        assert do_algebra(['*'], [0, 5]) == 0

    def test_multiple_additions(self):
        assert do_algebra(['+', '+'], [1, 2, 3]) == 6

    def test_multiple_subtractions(self):
        assert do_algebra(['-', '-'], [5, 2, 1]) == 2

    def test_multiple_multiplications(self):
        assert do_algebra(['*', '*'], [2, 3, 4]) == 24

    def test_division_by_one(self):
        assert do_algebra(['//'], [10, 1]) == 10

    def test_exponentiation_with_one(self):
        assert do_algebra(['**'], [5, 1]) == 5

    def test_exponentiation_with_zero(self):
        assert do_algebra(['**'], [5, 0]) == 1

    def test_large_numbers(self):
        assert do_algebra(['+'], [1000000, 2000000]) == 3000000

    def test_mixed_large_numbers(self):
        assert do_algebra(['*', '+'], [1000, 2, 3000]) == 6002000
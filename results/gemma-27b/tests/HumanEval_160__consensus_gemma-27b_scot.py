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
    def test_basic_addition_subtraction(self):
        assert do_algebra(['+', '-'], [2, 3, 1]) == 4

    def test_multiplication_division(self):
        assert do_algebra(['*', '//'], [2, 3, 2]) == 3

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    def test_longer_expression(self):
        assert do_algebra(['+', '-', '*', '//', '**'], [2, 3, 4, 2, 2]) == 7

    def test_zero_operand(self):
        assert do_algebra(['+'], [5, 0]) == 5

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            do_algebra(['//'], [5, 0])

    def test_empty_operator_list(self):
        with pytest.raises(IndexError):
            do_algebra([], [5, 0])

    def test_invalid_operator(self):
        with pytest.raises(KeyError):
            do_algebra(['$'], [2, 3])

    def test_all_addition(self):
        assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

    def test_all_multiplication(self):
        assert do_algebra(['*', '*', '*'], [1, 2, 3, 4]) == 24

    def test_negative_numbers(self):
        assert do_algebra(['+', '-'], [-2, 3, 1]) == 2

    def test_large_numbers(self):
        assert do_algebra(['+', '*'], [1000, 2, 3]) == 6000

    def test_combination_of_all_operations(self):
        assert do_algebra(['+', '*', '-', '//', '**'], [2, 3, 4, 5, 2]) == 2

    def test_operator_list_with_one_element(self):
        assert do_algebra(['+'], [2, 3]) == 5

    def test_operand_list_with_two_elements(self):
        assert do_algebra(['+'], [2, 3]) == 5

    def test_exponentiation_with_zero(self):
        assert do_algebra(['**'], [2, 0]) == 1
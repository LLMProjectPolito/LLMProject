
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
from your_module import do_algebra  # Replace your_module

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
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    if not operator:
        raise ValueError("Operator list cannot be empty.")
    if not operand:
        raise ValueError("Operand list cannot be empty.")
    if any(op < 0 for op in operand):
        raise ValueError("Operands must be non-negative integers.")

    expression = str(operand[0])
    for i in range(len(operator)):
        if operator[i] not in ['+', '-', '*', '//', '**']:
            raise TypeError("Invalid operator: {}".format(operator[i]))
        expression += " " + operator[i] + " " + str(operand[i+1])

    return eval(expression)


class TestDoAlgebra:
    def test_addition(self):
        assert do_algebra(['+'], [2, 3]) == 5
        assert do_algebra(['+', '+'], [1, 2, 3]) == 6

    def test_subtraction(self):
        assert do_algebra(['-'], [5, 2]) == 3
        assert do_algebra(['-', '-'], [10, 5, 2]) == 3

    def test_multiplication(self):
        assert do_algebra(['*'], [2, 3]) == 6
        assert do_algebra(['*', '*'], [1, 2, 3]) == 6

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 2]) == 5
        assert do_algebra(['//', '//'], [15, 3, 2]) == 2

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['**', '**'], [2, 3, 2]) == 36

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
        assert do_algebra(['*', '+', '//'], [2, 3, 4, 5]) == 11

    def test_zero_operand(self):
        assert do_algebra(['+'], [0, 5]) == 5
        assert do_algebra(['*'], [2, 0]) == 0
        assert do_algebra(['-'], [5, 0]) == 5
        assert do_algebra(['//'], [5, 0]) == float('inf') # or raise ZeroDivisionError

    def test_large_numbers(self):
        assert do_algebra(['+'], [1000000, 2000000]) == 3000000
        assert do_algebra(['*'], [100, 1000]) == 100000

    def test_single_operator(self):
        assert do_algebra(['+'], [1, 1]) == 2
        assert do_algebra(['-'], [5, 2]) == 3

    def test_invalid_operator(self):
        with pytest.raises(TypeError):
            do_algebra(['&'], [1, 2])

    def test_empty_operator(self):
        with pytest.raises(ValueError):
            do_algebra([], [1, 2])

    def test_empty_operand(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [])

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [1, 2, 3])

    def test_negative_operand(self):
        with pytest.raises(ValueError):
            do_algebra(['+'], [-1, 2])
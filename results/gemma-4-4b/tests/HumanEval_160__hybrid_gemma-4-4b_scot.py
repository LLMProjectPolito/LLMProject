
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
        raise ValueError("The length of operator list must be equal to the length of operand list minus one.")

    if not operator:
        raise ValueError("Operator list must have at least one operator.")

    if len(operand) < 2:
        raise ValueError("Operand list must have at least two operands.")

    expression = str(operand[0])
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i + 1])

    return eval(expression)


class TestDoAlgebra:

    def test_addition(self):
        assert do_algebra(['+', 'x'], [2, 3]) == 5
        assert do_algebra(['+', '1', '2'], [1, 2]) == 3

    def test_subtraction(self):
        assert do_algebra(['-', 'x'], [5, 2]) == 3
        assert do_algebra(['-', '10', '5'], [10, 5]) == 5

    def test_multiplication(self):
        assert do_algebra(['*', '+'], [2, 3]) == 6
        assert do_algebra(['*', '4', '5'], [4, 5]) == 20

    def test_floor_division(self):
        assert do_algebra(['//'], [10, 3]) == 3
        assert do_algebra(['//', '15', '4'], [15, 4]) == 3

    def test_exponentiation(self):
        assert do_algebra(['**'], [2, 3]) == 8
        assert do_algebra(['**', '2', '3'], [2, 3]) == 8

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2, 3, 4]) == 9
        assert do_algebra(['*', '+', '//'], [5, 2, 4]) == 10
        assert do_algebra(['+', '1', '*', '2', '3'], [1, 2, 3]) == 7

    def test_large_numbers(self):
        assert do_algebra(['+', '1000', '2000'], [1000, 2000]) == 3000

    def test_negative_numbers(self):
        assert do_algebra(['+', '-'], [5, -2]) == 3
        assert do_algebra(['*', '-', '2', '3'], [2, 3]) == -6

    def test_zero(self):
        assert do_algebra(['+', '0', '5'], [0, 5]) == 5
        assert do_algebra(['*', '0', '5'], [0, 5]) == 0

    def test_edge_cases_length(self):
        with pytest.raises(ValueError) as excinfo:
            do_algebra(['+', 'x'], [2])
        assert "The length of operator list must be equal to the length of operand list minus one." in str(excinfo.value)

        with pytest.raises(ValueError) as excinfo:
            do_algebra([], [1, 2])
        assert "Operator list must have at least one operator." in str(excinfo.value)

        with pytest.raises(ValueError) as excinfo:
            do_algebra(['+', 'x'], [2, 3])
        assert "Operand list must have at least two operands." in str(excinfo.value)
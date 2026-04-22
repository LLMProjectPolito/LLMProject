
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
import pytest

class TestDoAlgebra:

    def test_addition(self):
        assert do_algebra(['+', 2, 3], [2]) == 5
        assert do_algebra(['+', 1, 1, 1], [1]) == 3

    def test_subtraction(self):
        assert do_algebra(['-', 2, 3], [2]) == -1
        assert do_algebra(['-', 5, 2], [5]) == 3

    def test_multiplication(self):
        assert do_algebra(['*', 2, 3], [2]) == 6
        assert do_algebra(['*', 4, 5], [4]) == 20

    def test_floor_division(self):
        assert do_algebra(['//', 10, 3], [10]) == 3
        assert do_algebra(['//', 15, 4], [15]) == 3

    def test_exponentiation(self):
        assert do_algebra(['**', 2, 3], [2]) == 8
        assert do_algebra(['**', 3, 2], [3]) == 9

    def test_mixed_operations(self):
        assert do_algebra(['+', '*', '-'], [2]) == 9
        assert do_algebra(['+', 2, '*', 3, '-', 1], [2]) == 14
        assert do_algebra(['*', 2, '+', 3, '//', 2], [2]) == 9

    def test_single_operand(self):
        with pytest.raises(IndexError):
            do_algebra(['+', 2], [2])

    def test_empty_operator_list(self):
        with pytest.raises(IndexError):
            do_algebra([], [2])

    def test_empty_operand_list(self):
        with pytest.raises(IndexError):
            do_algebra(['+', 2], [])

    def test_invalid_operator(self):
        with pytest.raises(IndexError):
            do_algebra(['%', 2, 3], [2])
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

def test_do_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [4, 3]) == 12

def test_do_algebra_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_do_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5]) == 1

def test_do_algebra_with_zero():
    assert do_algebra(['+'], [0, 5]) == 5
    assert do_algebra(['*'], [0, 10]) == 0
    assert do_algebra(['//'], [10, 0]) == pytest.raises(ZeroDivisionError)

def test_do_algebra_long_expression():
    assert do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '-', '//'], [1, 2, 3, 4, 5]) == 1

def test_do_algebra_exponentiation_and_addition():
    assert do_algebra(['**', '+'], [2, 3, 1]) == 9

def test_do_algebra_edge_case_1():
    assert do_algebra(['-'], [100, 1]) == 99

def test_do_algebra_edge_case_2():
    assert do_algebra(['*'], [1, 100]) == 100

def test_do_algebra_edge_case_3():
    assert do_algebra(['//'], [100, 10]) == 10

def test_do_algebra_edge_case_4():
    assert do_algebra(['**'], [2, 10]) == 1024

def test_do_algebra_with_zero_2():
    assert do_algebra(['+', '*'], [0, 5, 2]) == 10

def test_do_algebra_large_numbers():
    assert do_algebra(['+', '*'], [1000, 2, 3]) == 6000

def test_do_algebra_floor_division_with_remainder():
    assert do_algebra(['//'], [7, 3]) == 2

def test_do_algebra_exponentiation_with_zero_exponent():
    assert do_algebra(['**'], [5, 0]) == 1

def test_do_algebra_exponentiation_with_one_exponent():
    assert do_algebra(['**'], [5, 1]) == 5

def test_do_algebra_long_expression_2():
    operators = ['+', '-', '*', '//', '**', '+', '-']
    operands = [1, 2, 3, 4, 5, 6, 7]
    assert do_algebra(operators, operands) == -11

def test_do_algebra_all_additions():
    operators = ['+', '+', '+', '+']
    operands = [1, 2, 3, 4, 5]
    assert do_algebra(operators, operands) == 15

def test_do_algebra_all_multiplications():
    operators = ['*', '*', '*', '*']
    operands = [1, 2, 3, 4, 5]
    assert do_algebra(operators, operands) == 120
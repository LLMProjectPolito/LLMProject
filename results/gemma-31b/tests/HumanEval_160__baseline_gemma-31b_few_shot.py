
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

def test_do_algebra_basic_addition():
    assert do_algebra(['+'], [1, 2]) == 3

def test_do_algebra_basic_subtraction():
    assert do_algebra(['-'], [10, 5]) == 5

def test_do_algebra_basic_multiplication():
    assert do_algebra(['*'], [3, 4]) == 12

def test_do_algebra_basic_floor_division():
    assert do_algebra(['//'], [10, 3]) == 3

def test_do_algebra_basic_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_example_case():
    # Example from docstring: 2 + 3 * 4 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_precedence_mul_add():
    # Multiplication should happen before addition: 2 + 3 * 4 = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

def test_do_algebra_precedence_exp_mul():
    # Exponentiation should happen before multiplication: 2 * 3 ** 2 = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18

def test_do_algebra_precedence_div_sub():
    # Floor division should happen before subtraction: 10 - 6 // 2 = 7
    assert do_algebra(['-', '//'], [10, 6, 2]) == 7

def test_do_algebra_complex_mixed():
    # 2 ** 3 + 10 // 3 * 2 = 8 + 3 * 2 = 8 + 6 = 14
    assert do_algebra(['**', '+', '//', '*'], [2, 3, 10, 3, 2]) == 14

def test_do_algebra_with_zeros():
    # 0 * 5 + 0 ** 2 = 0 + 0 = 0
    assert do_algebra(['*', '+', '**'], [0, 5, 0, 2]) == 0
    # 10 + 0 * 5 = 10
    assert do_algebra(['+', '*'], [10, 0, 5]) == 10

def test_do_algebra_large_numbers():
    # 100 ** 2 // 10 = 10000 // 10 = 1000
    assert do_algebra(['**', '//'], [100, 2, 10]) == 1000
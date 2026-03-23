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
        raise ValueError("Length of operator list must be one less than the length of operand list.")
    for num in operand:
        if not isinstance(num, int) or num < 0:
            raise ValueError("Operand list must contain non-negative integers.")

    expression = operand[0]
    for i in range(len(operator)):
        expression = str(expression) + operator[i] + str(operand[i+1])
    try:
        return eval(expression)
    except ZeroDivisionError:
        return None

def test_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6

def test_algebra_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_algebra_complex_expression():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_algebra_multiple_operations():
    assert do_algebra(['+', '*', '//'], [2, 3, 4, 2]) == 10

def test_algebra_with_zero():
    assert do_algebra(['+'], [0, 5]) == 5

def test_algebra_with_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_algebra_with_exponentiation_and_zero():
    assert do_algebra(['**'], [0, 5]) == 0

def test_algebra_with_exponentiation_and_one():
    assert do_algebra(['**'], [1, 5]) == 1

def test_algebra_with_floor_division_and_one():
    assert do_algebra(['//'], [5, 1]) == 5

def test_algebra_with_floor_division_and_zero():
    assert do_algebra(['//'], [5, 0]) is None

def test_algebra_exponentiation_with_negative_base():
    assert do_algebra(['**'], [-2, 3]) == -8

def test_algebra_floor_division_with_negative_numbers():
    assert do_algebra(['//'], [-10, 3]) == -4

def test_algebra_large_exponent():
    assert do_algebra(['**'], [2, 10]) == 1024

def test_algebra_invalid_operand_type():
    with pytest.raises(ValueError):
        do_algebra(['+'], [2.5, 3])

def test_algebra_negative_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [-2, 3])

def test_algebra_mismatched_lengths():
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [2, 3])

def test_algebra_empty_operator_list():
    with pytest.raises(ValueError):
        do_algebra([], [5])

def test_algebra_single_operand():
    with pytest.raises(ValueError):
        do_algebra(['+'], [5])
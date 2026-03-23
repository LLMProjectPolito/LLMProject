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

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `do_algebra` takes a list of operators and a list of operands and evaluates a mathematical expression.
### The expression is built by applying the operators to the operands in sequence.
### The function should handle addition, subtraction, multiplication, floor division, and exponentiation.
### The function should handle edge cases such as empty operator list or operand list.
### The function should handle cases where the operands are non-negative integers.
### STEP 2: PLAN - List test functions names and scenarios.
### test_do_algebra_addition()
### test_do_algebra_subtraction()
### test_do_algebra_multiplication()
### test_do_algebra_floor_division()
### test_do_algebra_exponentiation()
### test_do_algebra_mixed_operations()
### test_do_algebra_single_operand()
### test_do_algebra_empty_operator()
### test_do_algebra_empty_operand()
### STEP 3: CODE - Write the high-quality pytest suite.

def test_do_algebra_addition():
    assert do_algebra(['+', '+'], [2, 3, 4]) == 9

def test_do_algebra_subtraction():
    assert do_algebra(['-', '-', 5], [2, 3, 4]) == 9

def test_do_algebra_multiplication():
    assert do_algebra(['*', '*'], [2, 3, 4]) == 24

def test_do_algebra_floor_division():
    assert do_algebra(['//', '//'], [2, 3, 4]) == 1

def test_do_algebra_exponentiation():
    assert do_algebra(['**', '**'], [2, 3]) == 8

def test_do_algebra_mixed_operations():
    assert do_algebra(['+', '*', '-', '**'], [2, 3, 4, 5, 2]) == 242

def test_do_algebra_single_operand():
    assert do_algebra(['+', '+'], [2]) == 2

def test_do_algebra_empty_operator():
    assert do_algebra([], [2, 3, 4]) == 2

def test_do_algebra_empty_operand():
    assert do_algebra(['+', '*'], []) == 0

def test_do_algebra_complex():
    assert do_algebra(['*', '+', '//', '**'], [10, 2, 3, 4, 5]) == 100

def test_do_algebra_large_numbers():
    assert do_algebra(['*', '+'], [100, 200, 300]) == 600

def test_do_algebra_floor_division_edge():
    assert do_algebra(['//'], [10, 3]) == 3

def test_do_algebra_exponentiation_edge():
    assert do_algebra(['**'], [2, 0]) == 1
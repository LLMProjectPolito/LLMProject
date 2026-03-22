import pytest
import math


# Focus: Operator Precedence
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `do_algebra` evaluates an expression based on operators and operands.
# Operator precedence (PEMDAS/BODMAS) is crucial. We need to test scenarios that specifically
# verify the correct order of operations.  We'll focus on combinations of +, *, -, //, and **.

# STEP 2: PLAN - List test functions names and scenarios.
# 1. test_operator_precedence_add_mul: Tests addition and multiplication precedence.
# 2. test_operator_precedence_mul_add: Tests multiplication and addition precedence.
# 3. test_operator_precedence_exp_add: Tests exponentiation and addition precedence.

# STEP 3: CODE - Write the high-quality pytest suite.

def test_operator_precedence_add_mul():
    operators = ['+', '*']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 14  # 2 + (3 * 4) = 2 + 12 = 14

def test_operator_precedence_mul_add():
    operators = ['*', '+']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 10  # (2 * 3) + 4 = 6 + 4 = 10

def test_operator_precedence_exp_add():
    operators = ['**', '+']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 12  # 2 ** 3 + 4 = 8 + 4 = 12

# Focus: Empty/Invalid Input Lists
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `do_algebra` takes two lists: `operator` and `operand`.
# We need to test the function's behavior when either of these lists is empty or invalid.
# Invalid input includes empty lists, lists with incorrect lengths, or lists containing invalid data types.

# STEP 2: PLAN - List test functions names and scenarios.
# 1. test_empty_operator_list: Test with an empty operator list.
# 2. test_empty_operand_list: Test with an empty operand list.
# 3. test_operator_operand_length_mismatch: Test when the operator list length is not equal to the operand list length minus one.

# STEP 3: CODE - Write the high-quality pytest suite.

def test_empty_operator_list():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2, 3])

def test_empty_operand_list():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_operator_operand_length_mismatch():
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [1, 2])

# Focus: Large Numbers/Overflow
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

@pytest.mark.parametrize("operators, operands, expected", [
    (['+', '+', '+'], [10**9, 10**9, 10**9], 3 * 10**9),
    (['*', '*', '*'], [2, 10**5, 10**5], 2 * 10**10),
    (['**', '**'], [2, 3, 2], 2**(2**3)),
    (['+', '*', '-', '**'], [1, 10**6, 1, 2], 1 + (10**6 * 1) - (1**2)),
    (['//', '//'], [10**9, 2, 2], 250000000),
])
def test_large_numbers(operators, operands, expected):
    assert do_algebra(operators, operands) == expected
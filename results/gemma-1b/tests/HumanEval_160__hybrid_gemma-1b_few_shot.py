
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

```python
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
    if len(operand) == 0:
        return None

    if len(operand) == 1:
        return operand[0]

    if len(operator) == 0:
        return None

    if len(operator) == 1:
        return operator[0]

    if len(operator) == 2:
        return operator[0] * operator[1]

    if operator[0] == '+':
        return operand[0] + operand[1]
    elif operator[0] == '-':
        return operand[0] - operand[1]
    elif operator[0] == '*':
        return operand[0] * operand[1]
    elif operator[0] == '/':
        if operand[1] == 0:
            return None
        return operand[0] // operand[1]
    elif operator[0] == '**':
        return operand[0] ** operand[1]
    else:
        return None

# Test cases
def test_do_algebra():
    assert do_algebra('+ 2 3') == 5
    assert do_algebra('- 2 3') == 1
    assert do_algebra('* 2 3') == 6
    assert do_algebra('/') 2 3 == 1
    assert do_algebra('2 3') == 5
    assert do_algebra('2') == 2
    assert do_algebra('3') == 3
    assert do_algebra('2 3 4') == 24
    assert do_algebra('2 3 + 4') == 10
    assert do_algebra('2 3 * 4') == 24
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 / 4') == 0.5
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert do_algebra('2 3 ** 4') == 16
    assert
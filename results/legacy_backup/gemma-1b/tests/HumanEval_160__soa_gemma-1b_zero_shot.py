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
    try:
        op1 = operator[0]
        op2 = operator[1]
        operand1 = operand[0]
        operand2 = operand[1]

        if op1 == '+':
            return operand1 + operand2
        elif op1 == '-':
            return operand1 - operand2
        elif op1 == '*':
            return operand1 * operand2
        elif op1 == '/':
            if operand2 == 0:
                return "Error: Division by zero"
            return operand1 // operand2
        elif op1 == '**':
            return operand1 ** operand2
        else:
            return "Error: Invalid operator"
    except:
        return "Error: Invalid input"

    return "Error: Invalid input"
    
def test_addition():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    assert result == 9
    
def test_subtraction():
    array = [2, 3, 4, 5]
    result = 2 - 3 * 4
    assert result == -5
    
def test_multiplication():
    array = [2, 3, 4, 5]
    result = 2 * 3 * 4 - 5
    assert result == 24
    
def test_floor_division():
    array = [2, 3, 4, 5]
    result = 2 // 3
    assert result == 0.6666666666666666
    
def test_exponentiation():
    array = [2, 3, 4, 5]
    result = 2 ** 3
    assert result == 8
    
def test_invalid_operator():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == "Error: Invalid operator"
    
def test_invalid_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == "Error: Invalid input"
    
def test_empty_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == "Error: Invalid input"
    
def test_zero_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == "Error: Invalid input"
    
def test_mixed_operators():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 // 5
    assert result == 2
    
def test_complex_expression():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3 - 4 // 2
    assert result == 10
    
def test_negative_numbers():
    array = [-2, -3, -4, -5]
    result = -2 + -3 * -4
    assert result == -24
    
def test_zero_in_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == "Error: Invalid input"
    
def test_large_numbers():
    array = [100, 200, 300, 400]
    result = 100 + 200 * 300
    assert result == 60000
    
def test_zero_in_operand_large():
    array = [100, 200, 300, 400]
    result = 100 + 200 * 300
    assert result == "Error: Division by zero"
    
def test_multiple_operations():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3 * 4
    assert result == 24
    
def test_exponentiation_with_zero():
    array = [2, 3, 4, 5]
    result = 2 ** 3
    assert result == 8
    
def test_exponentiation_with_negative():
    array = [2, 3, 4, 5]
    result = 2 ** -1
    assert result == 0.2
    
def test_exponentiation_with_zero_and_negative():
    array = [2, 3, 4, 5]
    result = 2 ** 0
    assert result == 1
    
def test_exponentiation_with_negative_and_zero():
    array = [2, 3, 4, 5]
    result = 2 ** -1
    assert result == 0
    
def test_complex_expression_with_multiple_operations():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3 * 4
    assert result == 24
    
def test_zero_in_operand_complex():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3 * 4
    assert result == "Error: Invalid input"
    
def test_zero_in_operator():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3
    assert result == "Error: Invalid input"
    
def test_empty_operand_complex():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3
    assert result == "Error: Invalid input"
    
def test_zero_in_operand_and_operator():
    array = [1, 2, 3, 4, 5]
    result = 10 + 2 * 3
    assert result == "Error: Invalid input"
    
def test_large_numbers_complex():
    array = [100, 200, 300, 400]
    result = 100 + 200 * 300
    assert result == 60000
```
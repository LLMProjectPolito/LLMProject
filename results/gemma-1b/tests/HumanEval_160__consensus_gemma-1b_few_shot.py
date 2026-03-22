def test_do_algebra(arr: list[int], operator: list[str], operand: list[int]) -> int:
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
    if len(arr) != len(operand):
        raise ValueError("Length of operator list must equal the length of operand list.")

    result = operand[0]
    for i in range(1, len(operand)):
        if operator[0] == '+':
            result += operand[i]
        elif operator[0] == '-':
            result -= operand[i]
        elif operator[0] == '*':
            result *= operand[i]
        elif operator[0] == '/':
            if operand[i] == 0:
                raise ZeroDivisionError("Division by zero")
            result //= operand[i]
        elif operator[0] == '**':
            result **= operand[i]
    return result
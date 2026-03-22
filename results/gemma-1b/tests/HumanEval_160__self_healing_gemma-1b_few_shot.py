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
    if len(operand) != 2:
        raise ValueError("Invalid input: Operand list must have length 2.")

    op1, op2 = operator

    if op1 == '+':
        result = operand[0] + operand[1]
    elif op1 == '-':
        result = operand[0] - operand[1]
    elif op1 == '*':
        result = operand[0] * operand[1]
    elif op1 == '/':
        if operand[1] == 0:
            return 0  # Handle division by zero
        result = operand[0] // operand[1]
    elif op1 == '**':
        result = operand[0] ** operand[1]
    else:
        return 0  # Handle invalid operator

    return result
import pytest

def do_algebra(operator, operand):
    try:
        if len(operator) == 1 and len(operand) == 1:
            return operator[0] + operand[0]
        elif len(operator) == 1:
            return operator[0]
        elif len(operand) == 1:
            return operand[0]
        elif len(operator) == 2:
            return operator[0] + operand[1]
        elif len(operand) == 2:
            return operand[0] * operator[1]
        elif len(operator) == 3:
            return operator[0] + operand[1] * operator[2]
        elif len(operand) == 3:
            return operand[0] * operand[1] * operand[2]
        else:
            return 0
    except:
        return 0
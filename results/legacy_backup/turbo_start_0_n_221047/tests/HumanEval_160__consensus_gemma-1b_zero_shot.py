import pytest

def do_algebra(operator, operand):
    try:
        return eval(str(operator[0]) + str(operand[0]) + operator[1] + str(operand[1]))
    except:
        return 0
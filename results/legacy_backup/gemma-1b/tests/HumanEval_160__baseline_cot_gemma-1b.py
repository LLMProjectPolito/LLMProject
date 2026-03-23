def do_algebra(operator, operand):
    try:
        if len(operator) == 1:
            if len(operand) == 1:
                return operator[0] * operand[0]
            else:
                return operator[0] + operand[0]
        elif len(operator) == 2:
            if len(operand) == 2:
                return operator[0] + operand[1]
            else:
                return operator[0] * operand[1]
        elif len(operator) == 3:
            if len(operand) == 3:
                return operator[0] * operand[1] + operand[2]
            else:
                return operator[0] * operand[1] + operator[1] * operand[2]
        elif len(operator) == 4:
            if len(operand) == 4:
                return operator[0] * operand[1] + operator[1] * operand[2] + operand[3]
            else:
                return operator[0] * operand[1] + operator[1] * operand[2] + operator[2] * operand[3]
        else:
            return 0
    except:
        return 0
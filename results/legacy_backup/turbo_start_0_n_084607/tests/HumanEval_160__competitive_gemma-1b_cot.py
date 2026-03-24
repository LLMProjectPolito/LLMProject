def do_algebra(operator, operand):
    try:
        if operator == '+':
            return operand[0] + operand[1]
        elif operator == '-':
            return operand[0] - operand[1]
        elif operator == '*':
            return operand[0] * operand[1]
        elif operator == '//':
            if operand[0] == 0:
                return "Error: Division by zero"
            return operand[0] // operand[1]
        elif operator == '**':
            if operand[0] == 0:
                return "Error: Exponentiation by zero"
            return operand[0] ** operand[1]
        else:
            return "Error: Invalid operator"
    except IndexError:
        return "Error: Invalid input"
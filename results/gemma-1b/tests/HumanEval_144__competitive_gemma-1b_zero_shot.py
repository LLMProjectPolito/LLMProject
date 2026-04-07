
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

def simplify(x, n):
    try:
        x_int = int(x)
        n_int = int(n)
        if x_int == 0 or n_int == 0:
            return False
        numerator = x_int
        denominator = n_int
        common_divisor = gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        if denominator == 1:
            return True
        else:
            return numerator == denominator
    except:
        return False

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
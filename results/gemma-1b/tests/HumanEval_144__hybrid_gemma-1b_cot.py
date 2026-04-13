
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
        x_val = str(x)
        n_val = str(n)
        
        num_val = int(x_val)
        den_val = int(n_val)
        
        if den_val == 0:
            return False
        
        numerator = num_val
        denominator = den_val
        
        if numerator % denominator == 0:
            return True
        else:
            return False
    except:
        return False

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
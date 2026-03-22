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
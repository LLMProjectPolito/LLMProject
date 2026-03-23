def simplify(x, n):
    try:
        numerator, denominator = x.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
            return False
        if numerator % denominator == 0:
            return True
        else:
            return False
    except:
        return False
def simplify(x, n):
    try:
        numerator, denominator = x.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
            return False
        return numerator * denominator == int(numerator * denominator)
    except:
        return False
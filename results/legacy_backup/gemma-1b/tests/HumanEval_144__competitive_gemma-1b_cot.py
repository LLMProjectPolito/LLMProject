def simplify(x, n):
    try:
        numerator, denominator = map(int, x.split('/'))
        if denominator == 0:
            return False
        if numerator == 0:
            return False
        return str(numerator / denominator) == str(int(numerator / denominator))
    except:
        return False
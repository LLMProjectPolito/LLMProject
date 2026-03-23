import pytest

def simplify(x, n):
    """
    Simplifies the expression x * n.
    Returns True if x * n evaluates to a whole number and False otherwise.
    Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.
    """
    try:
        numerator, denominator = x.split('/')
        numerator_int = int(numerator)
        denominator_int = int(denominator)

        if denominator_int == 0:
            return False

        return numerator_int * denominator_int == int(numerator_int * denominator_int)
    except ValueError:
        return False
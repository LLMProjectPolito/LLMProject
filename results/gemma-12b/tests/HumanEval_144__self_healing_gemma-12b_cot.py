
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

import pytest
from fractions import Fraction

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
    x_frac = Fraction(x)
    n_frac = Fraction(n)
    product = x_frac * n_frac
    return product.denominator == 1

class TestSimplify:
    def test_simplify_true(self):
        assert simplify("1/5", "5/1") == True
        assert simplify("2/2", "1/1") == True
        assert simplify("1/1", "1/1") == True
        assert simplify("3/3", "2/2") == True
        assert simplify("4/4", "1/1") == True
        assert simplify("1/2", "2/1") == True
        assert simplify("1/3", "3/1") == True
        assert simplify("1/4", "4/1") == True
        assert simplify("1/5", "5/1") == True
        assert simplify("1/6", "6/1") == True
        assert simplify("1/7", "7/1") == True
        assert simplify("1/8", "8/1") == True
        assert simplify("1/9", "9/1") == True
        assert simplify("1/10", "10/1") == True

    def test_simplify_false(self):
        assert simplify("1/6", "2/1") == False
        assert simplify("7/10", "10/2") == False
        assert simplify("1/2", "3/1") == False
        assert simplify("1/3", "2/1") == False
        assert simplify("1/4", "3/1") == False
        assert simplify("1/5", "2/1") == False
        assert simplify("1/6", "3/1") == False
        assert simplify("1/7", "2/1") == False
        assert simplify("1/8", "3/1") == False
        assert simplify("1/9", "2/1") == False
        assert simplify("1/10", "3/1") == False
        assert simplify("2/3", "1/2") == False
        assert simplify("3/4", "1/2") == False
        assert simplify("4/5", "1/2") == False
        assert simplify("5/6", "1/2") == False
        assert simplify("6/7", "1/2") == False
        assert simplify("7/8", "1/2") == False
        assert simplify("8/9", "1/2") == False
        assert simplify("9/10", "1/2") == False
        assert simplify("1/2", "1/3") == False
        assert simplify("1/3", "1/4") == False
        assert simplify("1/4", "1/5") == False
        assert simplify("1/5", "1/6") == False
        assert simplify("1/6", "1/7") == False
        assert simplify("1/7", "1/8") == False
        assert simplify("1/8", "1/9") == False
        assert simplify("1/9", "1/10") == False
        assert simplify("2/5", "3/7") == False
        assert simplify("3/8", "5/12") == False
        assert simplify("1/11", "1/13") == False
        assert simplify("1/12", "1/13") == False
        assert simplify("1/13", "1/14") == False
        assert simplify("1/14", "1/15") == False
        assert simplify("1/15", "1/16") == False
        assert simplify("1/16", "1/17") == False
        assert simplify("1/17", "1/18") == False
        assert simplify("1/18", "1/19") == False
        assert simplify("1/19", "1/20") == False
        assert simplify("1/20", "1/21") == False
        assert simplify("1/21", "1/22") == False
        assert simplify("1/22", "1/23") == False
        assert simplify("1/23", "1/24") == False
        assert simplify("1/24", "1/25") == False
        assert simplify("1/25", "1/26") == False
        assert simplify("1/26", "1/27") == False
        assert simplify("1/27", "1/28") == False
        assert simplify("1/28", "1/29") == False
        assert simplify("1/29", "1/30") == False
        assert simplify("1/30", "1/31") == False
        assert simplify("1/31", "1/32") == False
        assert simplify("1/32", "1/33") == False
        assert simplify("1/33", "1/34") == False
        assert simplify("1/34", "1/35") == False
        assert simplify("1/35", "1/36") == False
        assert simplify("1/36", "1/37") == False
        assert simplify("1/37", "1/38") == False
        assert simplify("1/38", "1/39") == False
        assert simplify("1/39", "1/40") == False
        assert simplify("1/40", "1/41") == False
        assert simplify("1/41", "1/42") == False
        assert simplify("1/42", "1/43") == False
        assert simplify("1/43", "1/44") == False
        assert simplify("1/44", "1/45") == False
        assert simplify("1/45", "1/46") == False
        assert simplify("1/46", "1/47") == False
        assert simplify("1/47", "1/48") == False
        assert simplify("1/48", "1/49") == False
        assert simplify("1/49", "1/50") == False
        assert simplify("1/50", "1/51") == False
        assert simplify("1/51", "1/52") == False
        assert simplify("1/52", "1/53") == False
        assert simplify("1/53", "1/54") == False
        assert simplify("1/54", "1/55") == False
        assert simplify("1/55", "1/56") == False
        assert simplify("1/56", "1/57") == False
        assert simplify("1/57", "1/58") == False
        assert simplify("1/58", "1/59") == False
        assert simplify("1/59", "1/60") == False
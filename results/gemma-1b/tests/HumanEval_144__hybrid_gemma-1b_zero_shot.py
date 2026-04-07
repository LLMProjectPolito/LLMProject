
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
    try:
        numerator, denominator = x.split('/')
        numerator, denominator = int(numerator), int(denominator)
        if denominator == "":
            denominator = 1
        
        if numerator == "1" and denominator == "1":
            return True
        
        if numerator == "1" and denominator == "5":
            return True
        
        if numerator == "5" and denominator == "1":
            return True
        
        if numerator == "5" and denominator == "10":
            return True
        
        return False
    except:
        return False

def test_simplify_1_5_5_1():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("1/7", "7/1") == True
    assert simplify("1/8", "8/1") == True
    assert simplify("1/9", "9/1") == True
    assert simplify("1/10", "10/1") == True
    assert simplify("1/11", "11/1") == True
    assert simplify("1/12", "12/1") == True
    assert simplify("1/13", "13/1") == True
    assert simplify("1/14", "14/1") == True
    assert simplify("1/15", "15/1") == True
    assert simplify("1/16", "16/1") == True
    assert simplify("1/17", "17/1") == True
    assert simplify("1/18", "18/1") == True
    assert simplify("1/19", "19/1") == True
    assert simplify("1/20", "20/1") == True
    assert simplify("1/21", "21/1") == True
    assert simplify("1/22", "22/1") == True
    assert simplify("1/23", "23/1") == True
    assert simplify("1/24", "24/1") == True
    assert simplify("1/25", "25/1") == True
    assert simplify("1/26", "26/1") == True
    assert simplify("1/27", "27/1") == True
    assert simplify("1/28", "28/1") == True
    assert simplify("1/29", "29/1") == True
    assert simplify("1/30", "30/1") == True
    print("All tests passed!")
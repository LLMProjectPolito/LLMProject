import pytest

def simplify(x, n):
    try:
        numerator, denominator = x.split('/')
        if denominator == "":
            denominator = 1
        
        numerator = int(numerator)
        denominator = int(denominator)
        
        return numerator * denominator == int(numerator * denominator)
    except ValueError:
        return False

def test_simplify_valid_fractions():
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

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

```python
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
        if denominator == "":
            denominator = 1
        
        if numerator == "0":
            return False
        
        if denominator == "0":
            return False

        if numerator == "0" and denominator != "0":
            return False

        return float(numerator) / float(denominator) == int(float(numerator) / float(denominator))
    except:
        return False

def test_simplify_simple_cases():
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
    assert simplify("1/6", "6/1") == False
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
    assert simplify("1/31", "31/1") == True
    assert simplify("1/32", "32/1") == True
    assert simplify("1/33", "33/1") == True
    assert simplify("1/34", "34/1") == True
    assert simplify("1/35", "35/1") == True
    assert simplify("1/36", "36/1") == True
    assert simplify("1/37", "37/1") == True
    assert simplify("1/38", "38/1") == True
    assert simplify("1/39", "39/1") == True
    assert simplify("1/40", "40/1") == True
    assert simplify("1/41", "41/1") == True
    assert simplify("1/42", "42/1") == True
    assert simplify("1/43", "43/1") == True
    assert simplify("1/44", "44/1") == True
    assert simplify("1/45", "45/1") == True
    assert simplify("1/46", "46/1") == True
    assert simplify("1/47", "47/1") == True
    assert simplify("1/48", "48/1") == True
    assert simplify("1/49", "49/1") == True
    assert simplify("1/50", "50/1") == True
    assert simplify("1/51", "51/1") == True
    assert simplify("1/52", "52/1") == True
    assert simplify("1/53", "53/1") == True
    assert simplify("1/54", "54/1") == True
    assert simplify("1/55", "55/1") == True
    assert simplify("1/56", "56/1") == True
    assert simplify("1/57", "57/1") == True
    assert simplify("1/58", "58/1") == True
    assert simplify("1/59", "59/1") == True
    assert simplify("1/60", "60/1") == True
    assert simplify("1/61", "61/1") == True
    assert simplify("1/62", "62/1") == True
    assert simplify("1/63", "63/1") == True
    assert simplify("1/64", "64/1") == True
    assert simplify("1/65", "65/1") == True
    assert simplify("1/66", "66/1") == True
    assert simplify("1/67", "67/1") == True
    assert simplify("1/68", "68/1") == True
    assert simplify("1/69", "69/1") == True
    assert simplify("1/70", "70/1") == True
    assert simplify("1/71", "71/1") == True
    assert simplify("1/72", "72/1") == True
    assert simplify("1/73", "73/1") == True
    assert simplify("1/74", "74/1") == True
    assert simplify("1/75", "75/1") == True
    assert simplify("1/76", "76/1") == True
    assert simplify("1/77", "77/1") == True
    assert simplify("1/78", "78/1") == True
    assert simplify("1/79", "79/1") == True
    assert simplify("1/80", "80/1") == True
    assert simplify("1/81", "81/1") == True
    assert simplify("1/82", "82/1") == True
    assert simplify("1/83", "83/1") == True
    assert simplify("1/84", "84/1") == True
    assert simplify("1/85", "85/1") == True
    assert simplify("1/86", "86/1") == True
    assert simplify("1/87", "87/1") == True
    assert simplify("1/88", "88/1") == True
    assert simplify("1/89", "89/1") == True
    assert simplify("1/90", "90/1") == True
    assert simplify("1/91", "91/1") == True
    assert simplify("1/92", "92/1") == True
    assert simplify("1/93", "93/1") == True
    assert
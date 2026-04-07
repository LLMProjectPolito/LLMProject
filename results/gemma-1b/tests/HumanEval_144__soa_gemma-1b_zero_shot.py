
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

        return float(numerator) / float(denominator) == int(float(numerator) / float(denominator))
    except:
        return False

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/10", "10/2") == False
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("1/7", "7/1") == True
    assert simplify("1/8", "8/1") == True
    assert simplify("1/9", "9/1") == True
    assert simplify("1/10", "10/2") == False
    assert simplify("1/11", "11/1") == True
    assert simplify("1/12", "12/1") == True
    assert simplify("1/13", "13/1") == True
    assert simplify("1/14", "14/1") == True
    assert simplify("1/15", "15/1") == True
    assert simplify("1/16", "16/1") == True
    assert simplify("1/17", "17/1") == True
    assert simplify("1/18", "18/1") == True
    assert simplify("1/19", "19/1") == True
    assert simplify("1/20", "20/2") == False
    assert simplify("1/21", "21/2") == False
    assert simplify("1/22", "22/2") == False
    assert simplify("1/23", "23/2") == False
    assert simplify("1/24", "24/2") == False
    assert simplify("1/25", "25/2") == False
    assert simplify("1/26", "26/2") == False
    assert simplify("1/27", "27/2") == False
    assert simplify("1/28", "28/2") == False
    assert simplify("1/29", "29/2") == False
    assert simplify("1/30", "30/2") == False
    assert simplify("1/31", "31/2") == False
    assert simplify("1/32", "32/2") == False
    assert simplify("1/33", "33/2") == False
    assert simplify("1/34", "34/2") == False
    assert simplify("1/35", "35/2") == False
    assert simplify("1/36", "36/2") == False
    assert simplify("1/37", "37/2") == False
    assert simplify("1/38", "38/2") == False
    assert simplify("1/39", "39/2") == False
    assert simplify("1/40", "40/2") == False
    assert simplify("1/41", "41/2") == False
    assert simplify("1/42", "42/2") == False
    assert simplify("1/43", "43/2") == False
    assert simplify("1/44", "44/2") == False
    assert simplify("1/45", "45/2") == False
    assert simplify("1/46", "46/2") == False
    assert simplify("1/47", "47/2") == False
    assert simplify("1/48", "48/2") == False
    assert simplify("1/49", "49/2") == False
    assert simplify("1/50", "50/2") == False
    assert simplify("1/51", "51/2") == False
    assert simplify("1/52", "52/2") == False
    assert simplify("1/53", "53/2") == False
    assert simplify("1/54", "54/2") == False
    assert simplify("1/55", "55/2") == False
    assert simplify("1/56", "56/2") == False
    assert simplify("1/57", "57/2") == False
    assert simplify("1/58", "58/2") == False
    assert simplify("1/59", "59/2") == False
    assert simplify("1/60", "60/2") == False
    assert simplify("1/61", "61/2") == False
    assert simplify("1/62", "62/2") == False
    assert simplify("1/63", "63/2") == False
    assert simplify("1/64", "64/2") == False
    assert simplify("1/65", "65/2") == False
    assert simplify("1/66", "66/2") == False
    assert simplify("1/67", "67/2") == False
    assert simplify("1/68", "68/2") == False
    assert simplify("1/69", "69/2") == False
    assert simplify("1/70", "70/2") == False
    assert simplify("1/71", "71/2") == False
    assert simplify("1/72", "72/2") == False
    assert simplify("1/73", "73/2") == False
    assert simplify("1/74", "74/2") == False
    assert simplify("1/75", "75/2") == False
    assert simplify("1/76", "76/2") == False
    assert simplify("1/77", "77/2") == False
    assert simplify("1/78", "78/2") == False
    assert simplify("1/79", "79/2") == False
    assert simplify("1/80", "80/2") == False
    assert simplify("1/81", "81/2") == False
    assert simplify("1/82", "82/2") == False
    assert simplify("1/83", "83/2") == False
    assert simplify("1/84", "84/2") == False
    assert simplify("1/85", "85/2") == False
    assert simplify("1/86", "86/2") == False
    assert simplify("1/87", "87/2") == False
    assert simplify("1/88", "88/2") == False
    assert simplify("1/89", "89/2") == False
    assert simplify("1/90", "90

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

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("4/6", "3/2") == True
    assert simplify("10/4", "2/1") == True

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False
    assert simplify("2/5", "5/4") == False
    assert simplify("3/7", "7/5") == False

def test_simplify_mixed():
    assert simplify("1/2", "2/4") == True
    assert simplify("2/4", "1/2") == True
    assert simplify("3/5", "5/3") == False
    assert simplify("4/7", "7/4") == False
    assert simplify("5/8", "8/5") == True

def test_simplify_whole_numbers():
    assert simplify("1/1", "2/2") == True
    assert simplify("3/3", "4/4") == True
    assert simplify("5/5", "6/6") == True
    assert simplify("7/7", "8/8") == True
    assert simplify("9/9", "10/10") == True

def test_simplify_large_numbers():
    assert simplify("100/25", "4/1") == True
    assert simplify("25/100", "1/4") == True
    assert simplify("1000/200", "5/1") == True
    assert simplify("200/1000", "1/5") == True
    assert simplify("123/456", "456/123") == True
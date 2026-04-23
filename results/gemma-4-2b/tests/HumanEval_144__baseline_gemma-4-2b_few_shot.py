
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
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    
    if den1 == 0 or den2 == 0:
        return False

    result_num = num1 * num2
    result_den = den1 * den2
    
    return result_num % result_den == 0

def test_simplify_positive():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True

def test_simplify_different_numbers():
    assert simplify("1/3", "2/1") == False
    assert simplify("2/5", "1/2") == False
    assert simplify("3/4", "4/3") == True

def test_simplify_same_numbers():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/2", "2/2") == True
    assert simplify("5/5", "5/5") == True

def test_simplify_large_numbers():
    assert simplify("100/200", "200/100") == True
    assert simplify("1000/2000", "2000/1000") == True
    assert simplify("1000/2000", "1000/2000") == False
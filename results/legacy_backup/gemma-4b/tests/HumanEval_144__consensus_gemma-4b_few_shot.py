def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("3/4", "4/1") == True
    assert simplify("4/3", "3/1") == True
    assert simplify("5/7", "7/5") == True
    assert simplify("10/11", "11/10") == True

def test_simplify_zero_denominator():
    assert simplify("1/0", "5/1") == False

def test_simplify_negative_numbers():
    assert simplify("-1/2", "2/1") == True
    assert simplify("1/-2", "-2/1") == True
    assert simplify("-1/2", "2/-1") == True

def test_simplify_large_numbers():
    assert simplify("123/456", "456/123") == True
    assert simplify("123/456", "456/123") == True
    assert simplify("1000/1001", "1001/1000") == True

def test_simplify_equal_numbers():
    assert simplify("1/1", "1/1") == True
    assert simplify("10/10", "10/10") == True
    assert simplify("100/100", "100/100") == True
def test_simplify_basic():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False
    assert simplify("1/1", "1/2") == False
    assert simplify("10/1", "1/1") == True
    assert simplify("10/2", "1/1") == True
    assert simplify("10/3", "1/1") == False
    assert simplify("1/10", "10/1") == True
    assert simplify("1/10", "1/2") == False

def test_simplify_large_numbers():
    assert simplify("123/456", "456/123") == True
    assert simplify("123/456", "457/123") == False
    assert simplify("1000/1000", "1000/1000") == True
    assert simplify("1000/1001", "1001/1000") == False
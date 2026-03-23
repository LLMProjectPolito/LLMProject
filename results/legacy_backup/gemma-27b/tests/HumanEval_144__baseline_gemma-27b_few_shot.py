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
    assert simplify("123/456", "456/123") == True
    assert simplify("789/1011", "1011/789") == False
def test_simplify_basic_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True

def test_simplify_basic_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/2") == False

def test_simplify_zero_denominator():
    assert simplify("1/0", "5/1") == False

def test_simplify_large_numbers():
    assert simplify("123/456", "456/123") == True

def test_simplify_equal_numbers():
    assert simplify("5/5", "5/1") == True
    assert simplify("10/10", "10/1") == True

def test_simplify_one_over_one():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "2/1") == False

def test_simplify_complex_fraction():
    assert simplify("12/18", "18/3") == True
    assert simplify("12/18", "3/12") == False
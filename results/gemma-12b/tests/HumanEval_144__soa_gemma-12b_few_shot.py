def test_simplify_basic_true():
    assert simplify("1/5", "5/1") == True

def test_simplify_basic_false():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_false():
    assert simplify("7/10", "10/2") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True

def test_simplify_one_is_one():
    assert simplify("1/1", "2/3") == False
    assert simplify("2/3", "1/1") == False

def test_simplify_large_numbers_true():
    assert simplify("100/200", "200/100") == True

def test_simplify_large_numbers_false():
    assert simplify("100/201", "201/100") == False

def test_simplify_zero_numerator_true():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == True

def test_simplify_zero_numerator_false():
    assert simplify("0/1", "1/2") == False
    assert simplify("1/2", "0/1") == False

def test_simplify_decimal_result_false():
    assert simplify("1/3", "1/3") == False

def test_simplify_complex_true():
    assert simplify("2/4", "4/2") == True

def test_simplify_complex_false():
    assert simplify("2/5", "3/4") == False
def test_simplify_true_case1():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_case1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case2():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_case2():
    assert simplify("2/3", "3/2") == True

def test_simplify_true_case3():
    assert simplify("1/1", "1/1") == True

def test_simplify_false_case3():
    assert simplify("1/2", "1/3") == False

def test_simplify_with_larger_numbers_true():
    assert simplify("12/4", "3/1") == True

def test_simplify_with_larger_numbers_false():
    assert simplify("15/4", "2/1") == False

def test_simplify_different_denominators_true():
    assert simplify("2/5", "5/2") == True

def test_simplify_different_denominators_false():
    assert simplify("3/7", "7/3") == False

def test_simplify_one_is_whole_number_true():
    assert simplify("1/1", "2/2") == True

def test_simplify_one_is_whole_number_false():
    assert simplify("1/1", "2/3") == False
import pytest

def test_simplify_true_case_1():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_case_1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_case_2():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_case_2():
    assert simplify("2/3", "3/2") == True

def test_simplify_true_case_3():
    assert simplify("1/1", "1/1") == True

def test_simplify_false_case_3():
    assert simplify("1/2", "1/3") == False

def test_simplify_true_case_4():
    assert simplify("4/6", "3/2") == True

def test_simplify_false_case_4():
    assert simplify("5/7", "7/5") == False

def test_simplify_true_case_5():
    assert simplify("10/4", "2/1") == True

def test_simplify_false_case_5():
    assert simplify("1/4", "1/2") == False

def test_simplify_with_larger_numbers_true():
    assert simplify("100/25", "5/1") == True

def test_simplify_with_larger_numbers_false():
    assert simplify("100/25", "6/1") == False

def test_simplify_with_same_fraction():
    assert simplify("2/3", "2/3") == True

def test_simplify_with_one_as_denominator():
    assert simplify("1/1", "2/1") == True

def test_simplify_with_one_as_numerator():
    assert simplify("1/2", "2/1") == False

def test_simplify_complex_fractions_true():
    assert simplify("15/8", "4/3") == True

def test_simplify_complex_fractions_false():
    assert simplify("15/8", "5/3") == False
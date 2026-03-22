import pytest

def test_simplify_valid_fractions_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("4/7", "7/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("5/2", "2/1") == True
    assert simplify("10/4", "2/1") == True

def test_simplify_valid_fractions_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("2/5", "3/1") == False
    assert simplify("3/4", "5/1") == False
    assert simplify("1/2", "1/3") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("100/1", "1/100") == True
    assert simplify("1/100", "100/1") == True

def test_simplify_large_numbers():
    assert simplify("1000/5", "5/1") == True
    assert simplify("1000/7", "7/1") == True
    assert simplify("1000/3", "3/1") == True
    assert simplify("1000/11", "11/1") == True
    assert simplify("1000/13", "13/1") == True

def test_simplify_different_denominators():
    assert simplify("2/3", "6/9") == True
    assert simplify("4/5", "8/10") == True
    assert simplify("1/2", "50/100") == True
    assert simplify("3/4", "15/20") == True

def test_simplify_complex_fractions():
    assert simplify("12/15", "25/5") == False
    assert simplify("21/28", "4/3") == True
    assert simplify("15/20", "3/4") == True
    assert simplify("16/24", "2/3") == True

def test_simplify_fractions_with_common_factors():
    assert simplify("6/8", "4/3") == False
    assert simplify("9/12", "3/4") == True
    assert simplify("10/15", "2/3") == True
    assert simplify("14/21", "2/3") == True

def test_simplify_fractions_with_large_common_factors():
    assert simplify("100/200", "1/2") == True
    assert simplify("50/150", "1/3") == True
    assert simplify("25/75", "1/3") == True
    assert simplify("120/180", "2/3") == True

def test_simplify_numerator_and_denominator_same():
    assert simplify("5/5", "1/1") == True
    assert simplify("10/10", "1/1") == True
    assert simplify("100/100", "1/1") == True
    assert simplify("7/7", "1/1") == True
import pytest

def test_simplify_valid_fractions_whole_number():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("4/7", "7/1") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("5/2", "2/1") == True

def test_simplify_valid_fractions_not_whole_number():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("2/5", "3/1") == False
    assert simplify("3/4", "5/1") == False

def test_simplify_valid_fractions_negative_result():
    assert simplify("1/2", "-1/1") == False
    assert simplify("-1/2", "1/1") == False
    assert simplify("-1/2", "-1/1") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/2", "1/2") == False
    assert simplify("2/1", "1/2") == False
    assert simplify("1/100", "100/1") == True
    assert simplify("100/1", "1/100") == True

def test_simplify_large_numbers():
    assert simplify("1000/500", "2/1") == True
    assert simplify("1000/3", "1/1") == False
    assert simplify("12345/6789", "6789/12345") == True

def test_simplify_different_denominators():
    assert simplify("2/3", "6/9") == True
    assert simplify("4/5", "8/10") == True
    assert simplify("1/2", "3/6") == True
    assert simplify("1/2", "4/7") == False

def test_simplify_complex_fractions():
    assert simplify("11/13", "13/11") == True
    assert simplify("17/19", "19/17") == True
    assert simplify("23/29", "29/23") == True
    assert simplify("31/37", "37/31") == True

def test_simplify_zero_numerator():
    assert simplify("0/1", "1/1") == True
    assert simplify("0/5", "5/1") == True
    assert simplify("0/1", "1/2") == True

def test_simplify_fraction_with_same_numerator_denominator():
    assert simplify("5/5", "1/1") == True
    assert simplify("10/10", "2/2") == True
    assert simplify("15/15", "3/3") == True
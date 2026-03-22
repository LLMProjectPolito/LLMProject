import pytest

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_not_whole_number_2():
    assert simplify("7/10", "10/2") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "2/1") == True

def test_simplify_zero_numerator():
    assert simplify("0/1", "1/1") == True

def test_simplify_large_numbers():
    assert simplify("123/456", "456/123") == True

def test_simplify_large_numbers_2():
    assert simplify("1234/5678", "5678/1234") == True

def test_simplify_reduced_fraction():
    assert simplify("1/2", "2/1") == True

def test_simplify_unreduced_fraction():
    assert simplify("2/4", "4/2") == True

def test_simplify_large_denominator():
    assert simplify("1/1000", "1000/1") == True

def test_simplify_large_numerator():
    assert simplify("1000/1", "1/1000") == True
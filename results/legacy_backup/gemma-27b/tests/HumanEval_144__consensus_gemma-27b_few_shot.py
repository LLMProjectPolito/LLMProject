import pytest

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("4/6", "3/2") == True
    assert simplify("10/4", "2/1") == True
    assert simplify("10/2", "1/5") == True

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False
    assert simplify("2/5", "5/4") == False
    assert simplify("3/7", "7/5") == False
    assert simplify("2/5", "3/7") == False
    assert simplify("1/7", "2/3") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "2/2") == True
    assert simplify("1/2", "2/4") == True
    assert simplify("10/10", "1/1") == True
    assert simplify("1/100", "100/1") == True
    assert simplify("100/1", "1/100") == True

def test_simplify_larger_numbers():
    assert simplify("123/456", "456/123") == True
    assert simplify("1000/2000", "2000/1000") == True
    assert simplify("1234/5678", "5678/1234") == True
    assert simplify("123/456", "789/1011") == False

def test_simplify_different_values():
    assert simplify("2/3", "4/6") == True
    assert simplify("3/4", "6/8") == True
    assert simplify("5/6", "10/12") == True
    assert simplify("7/8", "14/16") == True
    assert simplify("9/10", "18/20") == True

def test_simplify_large_numbers_true():
    assert simplify("100/20", "5/1") == True

def test_simplify_large_numbers_false():
    assert simplify("101/20", "5/1") == False

def test_simplify_same_fraction():
    assert simplify("5/2", "5/2") == True

def test_simplify_one_whole_number():
    assert simplify("1/1", "2/1") == True

def test_simplify_another_whole_number():
    assert simplify("2/1", "1/1") == True
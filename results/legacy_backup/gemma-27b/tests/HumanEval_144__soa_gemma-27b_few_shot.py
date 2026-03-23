import pytest

def test_simplify_true():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("4/6", "3/2") == True
    assert simplify("10/4", "2/1") == True
    assert simplify("1/2", "2/4") == True

def test_simplify_false():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "2/1") == False
    assert simplify("2/5", "5/2") == False
    assert simplify("3/4", "4/5") == False
    assert simplify("1/7", "2/1") == False

def test_simplify_edge_cases():
    assert simplify("1/1", "2/2") == True
    assert simplify("10/10", "1/1") == True
    assert simplify("1/100", "100/1") == True
    assert simplify("1/2", "3/1") == False
    assert simplify("1/1", "1/2") == False

def test_simplify_larger_numbers():
    assert simplify("12/5", "5/12") == True
    assert simplify("100/10", "10/100") == True
    assert simplify("1000/100", "100/1000") == True
    assert simplify("123/456", "456/123") == True
    assert simplify("123/456", "123/456") == True
    assert simplify("123/456", "457/123") == False
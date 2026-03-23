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
    assert simplify("1/2", "1/3") == False
    assert simplify("2/5", "1/2") == False
    assert simplify("3/4", "1/5") == False

def test_simplify_fractions_with_common_factors():
    assert simplify("2/4", "4/1") == True
    assert simplify("3/6", "2/1") == True
    assert simplify("4/8", "2/1") == True
    assert simplify("6/9", "3/1") == True

def test_simplify_large_numbers():
    assert simplify("100/20", "2/1") == True
    assert simplify("1000/50", "5/1") == True
    assert simplify("100/3", "1/1") == False

def test_simplify_fractions_with_same_values():
    assert simplify("5/5", "5/5") == True
    assert simplify("10/10", "10/10") == True

def test_simplify_edge_cases():
    assert simplify("1/1", "2/2") == True
    assert simplify("2/2", "1/1") == True
    assert simplify("1/2", "2/1") == False
    assert simplify("2/1", "1/2") == False

def test_simplify_different_denominators():
    assert simplify("1/2", "3/4") == False
    assert simplify("2/3", "4/5") == False
    assert simplify("3/5", "1/2") == False
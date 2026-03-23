import pytest

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_not_whole_number():
    assert simplify("7/10", "10/2") == False

def test_simplify_one_whole():
    assert simplify("1/1", "2/3") == True

def test_simplify_other_whole():
    assert simplify("3/1", "1/1") == True

def test_simplify_both_whole():
    assert simplify("1/1", "1/1") == True

def test_simplify_large_numbers():
    assert simplify("12345/67890", "67890/12345") == False

def test_simplify_same_number():
    assert simplify("1/2", "1/2") == False

def test_simplify_complex_fraction():
    assert simplify("2/3", "3/4") == False

def test_simplify_fraction_with_one():
    assert simplify("1/4", "4/1") == True

def test_simplify_fraction_with_one_and_other():
    assert simplify("1/3", "2/1") == False

def test_simplify_fraction_with_other_and_one():
    assert simplify("2/1", "1/3") == False
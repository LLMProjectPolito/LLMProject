import pytest

def test_simplify_basic_true():
    assert simplify("1/2", "2/1") == True

def test_simplify_basic_false():
    assert simplify("1/3", "1/2") == False

def test_simplify_numerator_one():
    assert simplify("1/5", "5/1") == True

def test_simplify_denominator_one():
    assert simplify("2/1", "3/1") == True

def test_simplify_both_one():
    assert simplify("1/1", "1/1") == True

def test_simplify_large_numbers_true():
    assert simplify("100/2", "2/1") == True

def test_simplify_large_numbers_false():
    assert simplify("100/3", "1/2") == False

def test_simplify_simplifies_to_one():
    assert simplify("2/2", "1/1") == True

def test_simplify_boundary_case():
    assert simplify("2/3", "3/2") == False

def test_simplify_equivalent_fractions_true():
    assert simplify("2/4", "2/1") == True

def test_simplify_equivalent_fractions_false():
    assert simplify("1/2", "1/3") == False

def test_simplify_complex_true():
    assert simplify("4/6", "3/2") == True

def test_simplify_complex_false():
    assert simplify("5/7", "2/3") == False

def test_simplify_fraction_times_whole_number():
    assert simplify("1/2", "4/1") == True

def test_simplify_whole_number_times_fraction():
    assert simplify("4/1", "1/2") == True

def test_simplify_zero_numerator():
    assert simplify("0/5", "5/1") == True

def test_simplify_zero_numerator_and_denominator():
    assert simplify("0/5", "0/1") == True
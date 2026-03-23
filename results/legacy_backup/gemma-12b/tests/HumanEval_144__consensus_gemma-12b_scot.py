import pytest

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number_1():
    assert simplify("1/6", "2/1") == False

def test_simplify_not_whole_number_2():
    assert simplify("7/10", "10/2") == False

def test_simplify_same_fraction():
    assert simplify("1/1", "1/1") == True

def test_simplify_one_is_one():
    assert simplify("1/2", "1/1") == False
    assert simplify("2/1", "1/1") == True

def test_simplify_large_numbers():
    assert simplify("100/200", "200/100") == True
    assert simplify("100/201", "201/100") == False

def test_simplify_fraction_with_one_as_denominator():
    assert simplify("1/1", "5/1") == False
    assert simplify("5/1", "1/1") == False

def test_simplify_fraction_with_one_as_numerator():
    assert simplify("1/2", "1/3") == False
    assert simplify("1/3", "1/2") == False

def test_simplify_fraction_with_same_numerator():
    assert simplify("2/3", "3/2") == False

def test_simplify_fraction_with_same_denominator():
    assert simplify("3/4", "4/3") == False

def test_simplify_one_whole():
    assert simplify("1/1", "2/3") == True

def test_simplify_other_whole():
    assert simplify("3/1", "1/1") == True

def test_simplify_both_whole():
    assert simplify("1/1", "1/1") == True

def test_simplify_large_numbers_2():
    assert simplify("12345/67890", "67890/12345") == False

def test_simplify_same_number():
    assert simplify("1/2", "1/2") == False

def test_simplify_fraction_with_one_as_denominator_2():
    assert simplify("1/1", "5/1") == True

def test_simplify_fraction_with_one_as_numerator_2():
    assert simplify("5/1", "1/1") == True

def test_simplify_fraction_with_one_as_both_2():
    assert simplify("1/1", "1/1") == True

def test_simplify_complex_fractions():
    assert simplify("2/3", "3/4") == False

def test_simplify_another_complex_fractions():
    assert simplify("3/5", "10/6") == False

def test_simplify_one_over_one():
    assert simplify("1/1", "1/1") == True

def test_simplify_one_over_two():
    assert simplify("1/2", "1/1") == False

def test_simplify_two_over_one():
    assert simplify("2/1", "1/2") == False

def test_simplify_numerator_one():
    assert simplify("1/7", "14/1") == True

def test_simplify_denominator_one():
    assert simplify("14/1", "1/7") == True

def test_simplify_fraction_with_larger_numerator():
    assert simplify("5/2", "2/1") == False

def test_simplify_fraction_with_larger_denominator():
    assert simplify("1/100", "100/1") == True

def test_simplify_fraction_with_same_numerator_and_denominator():
    assert simplify("2/2", "3/3") == True

def test_simplify_same_numerator_different_denominator():
    assert simplify("1/2", "1/3") == False

def test_simplify_different_numerator_same_denominator():
    assert simplify("1/5", "2/5") == False
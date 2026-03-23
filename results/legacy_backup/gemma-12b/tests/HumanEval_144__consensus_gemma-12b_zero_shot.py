import pytest
from your_module import simplify  # Replace your_module

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_another_not_whole_number():
    assert simplify("7/10", "10/2") == False

def test_simplify_one_over_one():
    assert simplify("1/1", "1/1") == True

def test_simplify_one_over_two_and_two_over_one():
    assert simplify("1/2", "2/1") == False

def test_simplify_two_over_one_and_one_over_two():
    assert simplify("2/1", "1/2") == False

def test_simplify_large_numbers_whole():
    assert simplify("100/2", "2/1") == True

def test_simplify_large_numbers_not_whole():
    assert simplify("100/3", "2/1") == False

def test_simplify_same_fraction():
    assert simplify("1/2", "1/2") == True

def test_simplify_fraction_with_one_as_numerator():
    assert simplify("1/3", "6/1") == True

def test_simplify_fraction_with_one_as_denominator():
    assert simplify("5/1", "2/1") == False

def test_simplify_fraction_with_large_numerator_and_denominator():
    assert simplify("12345/6789", "6789/12345") == False

def test_simplify_fraction_with_small_numerator_and_denominator():
    assert simplify("2/3", "3/2") == False

def test_simplify_fraction_with_same_numerator_and_denominator():
    assert simplify("5/5", "1/1") == True

def test_simplify_fraction_with_different_numerator_and_denominator():
    assert simplify("3/4", "5/6") == False

def test_simplify_fraction_with_one_numerator_and_denominator():
    assert simplify("1/1", "2/2") == True

def test_simplify_fraction_with_one_numerator_and_denominator_2():
    assert simplify("2/2", "1/1") == True
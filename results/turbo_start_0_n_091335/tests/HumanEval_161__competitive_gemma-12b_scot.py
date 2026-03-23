import pytest

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "^%$#@!"
    assert solve("") == ""

def test_solve_all_letters_lower():
    assert solve("abc") == "ABC"
    assert solve("xyz") == "XYZ"
    assert solve("a") == "A"

def test_solve_all_letters_upper():
    assert solve("ABC") == "abc"
    assert solve("XYZ") == "xyz"
    assert solve("A") == "a"

def test_solve_mixed_letters_and_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("1a2B3c") == "1A2b3C"
    assert solve("!Ab@c") == "!aB@C"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_string_with_spaces():
    assert solve("a b c") == "A B C"
    assert solve(" A b C ") == " a B c "

def test_solve_string_with_numbers_and_symbols():
    assert solve("123abc456") == "123ABC456"
    assert solve("!@#abcXYZ") == "!@#ABCxyz"

def test_solve_long_string():
    long_string = "This is a long string with some letters and numbers 1234567890!@#$"
    expected_result = "tHIS IS A LONG STRING WITH SOME LETTERS AND NUMBERS 1234567890!@#$"
    assert solve(long_string) == expected_result
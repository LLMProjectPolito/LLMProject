import pytest

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "!@#$%^"
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
    assert solve("123a456b789") == "123A456B789"
    assert solve("!@#a$%^b") == "!@#A$%^B"

def test_solve_long_string():
    long_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    expected_result = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    assert solve(long_string) == expected_result
import pytest

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$") == "!@#$"

def test_solve_all_letters_lower():
    assert solve("ab") == "AB"
    assert solve("abc") == "ABC"

def test_solve_all_letters_upper():
    assert solve("AB") == "ab"
    assert solve("ABC") == "abc"

def test_solve_mixed_letters_and_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("a#B@c") == "A#b@C"
    assert solve("a1b2c") == "A1B2C"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_letter():
    assert solve("a") == "A"
    assert solve("A") == "a"

def test_solve_complex_string():
    assert solve("Hello, World!") == "hELLO, wORLD!"
    assert solve("This is a test.") == "tHIS IS A TEST."

def test_solve_string_with_numbers_and_symbols():
    assert solve("1a2B3c") == "1A2b3C"
    assert solve("!@#aB$c%") == "!@#A$b%"
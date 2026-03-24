import pytest

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "^%$#@!"
    assert solve("") == ""

def test_solve_all_letters_lower():
    assert solve("abc") == "ABC"
    assert solve("xyz") == "XYZ"
    assert solve("aBc") == "AbC"

def test_solve_all_letters_upper():
    assert solve("ABC") == "abc"
    assert solve("XYZ") == "xyz"
    assert solve("aBc") == "AbC"

def test_solve_mixed_letters_and_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("1a2B3c") == "1A2b3C"
    assert solve("!a@B#c%") == "!A@b#C%"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_letter():
    assert solve("a") == "A"
    assert solve("A") == "a"

def test_solve_single_symbol():
    assert solve("!") == "!"
    assert solve("1") == "1"

def test_solve_long_string():
    assert solve("ThisIsALongStringWithLettersAndSymbols123") == "tHISiSaLONGsTRINGwITHlETTERSANDSMBOLS123"

def test_solve_string_with_spaces():
    assert solve("Hello World") == "hELLO wORLD"

def test_solve_string_with_unicode():
    assert solve("你好世界") == "你好世界"
    assert solve("你好世界123") == "你好世界123"
    assert solve("你好世界a") == "你好世界A"
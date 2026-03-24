import pytest

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "^%$#@!"
    assert solve("") == ""

def test_solve_all_letters_lower():
    assert solve("ab") == "AB"
    assert solve("abcdef") == "ABCDEF"

def test_solve_all_letters_upper():
    assert solve("ABC") == "abc"
    assert solve("DEF") == "def"

def test_solve_mixed_letters_and_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("a!B@c") == "A!b@C"
    assert solve("1a2B3c") == "1A2B3c"
    assert solve("a1B2c3") == "A1B2c3"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_letter():
    assert solve("a") == "A"
    assert solve("A") == "a"

def test_solve_single_symbol():
    assert solve("!") == "!"
    assert solve("#") == "#"

def test_solve_long_string():
    assert solve("ThisIsALongStringWithLettersAndSymbols!@#") == "tHISisALONGSTRINGWITHLETTERSANDSMBOLS!@#"

def test_solve_string_with_spaces():
    assert solve("Hello World") == "hELLO wORLD"

def test_solve_string_with_unicode():
    assert solve("你好世界") == "你好世界"
    assert solve("你好世界a") == "你好世界A"
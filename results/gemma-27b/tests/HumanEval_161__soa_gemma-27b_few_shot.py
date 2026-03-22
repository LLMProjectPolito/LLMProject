import pytest

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_lowercase_letters():
    assert solve("ab") == "AB"

def test_solve_mixed_case_letters():
    assert solve("aB") == "Ab"

def test_solve_with_special_characters():
    assert solve("#a@C") == "#A@c"

def test_solve_mixed_string():
    assert solve("a1b2c") == "A1B2C"

def test_solve_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_solve_string_with_numbers_and_letters():
    assert solve("1a2b3c") == "1A2B3C"

def test_solve_string_with_only_special_characters():
    assert solve("!@#$%^") == "^%$#@!"

def test_solve_long_string():
    assert solve("ThisIsALongString") == "tHISiSaLONGsTRING"

def test_solve_string_with_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_solve_string_with_mixed_unicode_and_ascii():
    assert solve("a你好b世界") == "A你好B世界"
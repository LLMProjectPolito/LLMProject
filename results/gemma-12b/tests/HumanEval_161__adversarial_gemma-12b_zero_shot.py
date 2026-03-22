import pytest
from your_module import solve  # Replace your_module

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "^%$#@!"
    assert solve("") == ""

def test_solve_all_letters_lower():
    assert solve("ab") == "AB"
    assert solve("abcdef") == "ABCDEF"
    assert solve("hello") == "HELLO"

def test_solve_all_letters_upper():
    assert solve("AB") == "ab"
    assert solve("ABCDEF") == "abcdef"
    assert solve("WORLD") == "world"

def test_solve_mixed_letters_and_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("1a2B3c") == "1A2b3C"
    assert solve("!A@b#C$d") == "!a@B#c$D"
    assert solve("a1B2c3D") == "A1b2C3d"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_string_with_spaces():
    assert solve("a b c") == "A B C"
    assert solve("  a  b  c  ") == "  A  B  C  "

def test_solve_string_with_numbers_and_symbols():
    assert solve("123abc456DEF") == "123ABC456def"
    assert solve("!@#abcDEF$%^") == "!@#ABCDEF$%^"

def test_solve_long_string():
    long_string = "This is a long string with some letters and numbers 1234567890!@#$"
    expected_result = "tHIS IS A LONG STRING WITH SOME LETTERS AND NUMBERS 1234567890!@#$"
    assert solve(long_string) == expected_result

def test_solve_unicode_string():
    assert solve("你好世界") == "你好世界"
    assert solve("你好a世界") == "你好A世界"

def test_solve_string_with_special_characters():
    assert solve("a\nb") == "A\nB"
    assert solve("a\tb") == "A\tB"
    assert solve("a\"b") == "A\"B"
    assert solve("a'b") == "A'B"
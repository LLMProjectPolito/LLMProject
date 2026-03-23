import pytest

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_all_letters_lowercase():
    assert solve("ab") == "AB"

def test_solve_all_letters_uppercase():
    assert solve("AB") == "ab"

def test_solve_mixed_case_letters():
    assert solve("aB") == "Ab"

def test_solve_mixed_letters_and_numbers():
    assert solve("#a@C") == "#A@c"

def test_solve_letters_with_special_characters():
    assert solve("!a?B") == "!A?b"

def test_solve_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_solve_string_with_leading_and_trailing_spaces():
    assert solve("  ab  ") == "  AB  "

def test_solve_string_with_only_special_characters():
    assert solve("!@#$%^") == "^%$#@!"

def test_solve_long_string():
    assert solve("ThisIsALongString") == "tHISiSaLONGsTRING"

def test_solve_string_with_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_solve_string_with_mixed_unicode_and_ascii():
    assert solve("a你好b") == "A你好B"
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
    assert solve("a1b2c") == "A1B2c"

def test_solve_string_with_numbers_and_special_chars():
    assert solve("1#2$a") == "1#2$A"

def test_solve_string_with_only_special_chars():
    assert solve("!@#$") == "$#@!"

def test_solve_long_string():
    assert solve("ThisIsALongString") == "tHISiSaLONGsTRING"

def test_solve_string_with_spaces():
    assert solve("a b c") == "A b C"

def test_solve_string_with_unicode_characters():
    assert solve("你好世界") == "你好世界"

def test_solve_string_with_mixed_unicode_and_ascii():
    assert solve("a你好b") == "A你好B"

def test_solve_all_letters_lowercase():
    assert solve("ab") == "AB"

def test_solve_all_letters_uppercase():
    assert solve("AB") == "ab"

def test_solve_mixed_letters_and_numbers():
    assert solve("#a@C") == "#A@c"

def test_solve_letters_with_special_characters():
    assert solve("!a?B") == "!A?b"

def test_solve_string_with_leading_and_trailing_spaces():
    assert solve("  ab  ") == "  AB  "

def test_solve_string_with_only_uppercase_letters():
    assert solve("ABC") == "abc"

def test_solve_string_with_special_chars_and_letters():
    assert solve("!A@b#C$") == "!a@B#c$"

def test_solve_long_string():
    assert solve("ThisIsALongStringWithLettersAndNumbers123") == "tHISiSaLONGsTRINGwITHlETTERSaNDnUMBERS123"

def test_solve_string_with_mixed_unicode_and_ascii():
    assert solve("a你好b世界") == "A你好B世界"
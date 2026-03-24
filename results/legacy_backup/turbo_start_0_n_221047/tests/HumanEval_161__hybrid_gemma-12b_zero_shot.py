import pytest
from your_module import solve  # Replace your_module

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "!@#$%^"
    assert solve("1!2@3#") == "3#2@1!"
    assert solve("12345!@#$") == "54321!@#$"

def test_all_lowercase():
    assert solve("abc") == "ABC"
    assert solve("hello") == "HELLO"
    assert solve("abcdefghijklmnopqrstuvwxyz") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def test_all_uppercase():
    assert solve("ABC") == "abc"
    assert solve("WORLD") == "world"
    assert solve("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "abcdefghijklmnopqrstuvwxyz"

def test_mixed_case():
    assert solve("aBc") == "AbC"
    assert solve("HeLlO") == "hElLo"
    assert solve("aBcDeFgHiJkLmNoPqRsTuVwXyZ") == "AbCdEfGhIjKlMnOpQrStUvWxYz"

def test_mixed_case_with_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("1a2B3c") == "1A2B3C"
    assert solve("!a@B#c$") == "!A@b#C$"
    assert solve("1!a@B#c$2") == "1!A@b#C$2"

def test_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"
    assert solve("  a b  ") == "  A B  "
    assert solve("Hello World") == "hELLO wORLD"
    assert solve("  a b c  ") == "  A B C  "

def test_string_with_numbers_and_symbols():
    assert solve("123abc456DEF") == "123ABC456def"
    assert solve("!@#abcDEF$%^") == "!@#ABCDEF$%^"

def test_long_string():
    long_string = "This is a long string with mixed case letters and numbers 1234567890!@#$"
    expected_result = "tHIS IS A LONG STRING WITH MIXED CASE LETTERS AND NUMBERS 1234567890!@#$"
    assert solve(long_string) == expected_result
    assert solve("ThisIsALongStringWithMixedCaseAndSymbols123!") == "tHISisAlongstringwithmixedcaseandsymbols123!"

def test_unicode_characters():
    assert solve("你好世界") == "你好世界"
    assert solve("你好World") == "你好WORLD"
    assert solve("World你好") == "WORLD你好"
    assert solve("a你好b") == "A你好B"

def test_special_characters():
    assert solve("!@#$%^&*()") == "!@#$%^&*()"
    assert solve("a!b@c#d$e%f^g&h*i(") == "A!B@C#D$E%F^G&H*I("

def test_all_digits():
    assert solve("1234") == "4321"
    assert solve("007") == "700"
    assert solve("9876543210") == "0123456789"

def test_all_lowercase_letters():
    assert solve("abc") == "ABC"
    assert solve("xyz") == "XYZ"

def test_all_uppercase_letters():
    assert solve("ABC") == "abc"
    assert solve("XYZ") == "xyz"

def test_mixed_letters_and_digits():
    assert solve("a1b2c") == "A1B2C"

def test_mixed_letters_symbols_and_digits():
    assert solve("!a@B#c$") == "!A@b#C$"

def test_symbols_only():
    assert solve("!@#$%^") == "!@#$%^"

def test_mixed_case_and_symbols():
    assert solve("HeLlO!") == "hElLo!"
    assert solve("WoRlD?") == "wOrLd?"

def test_edge_case_single_letter():
    assert solve("a") == "A"
    assert solve("A") == "a"

def test_complex_string():
    assert solve("aBcDeFgHiJkLmNoPqRsTuVwXyZ123!@#$") == "AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$"
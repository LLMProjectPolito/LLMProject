import pytest

def test_empty_string():
    assert solve("") == ""

def test_only_letters_lowercase():
    assert solve("abc") == "ABC"

def test_only_letters_uppercase():
    assert solve("ABC") == "abc"

def test_mixed_case_letters():
    assert solve("aBc") == "AbC"

def test_only_numbers():
    assert solve("1234") == "4321"

def test_only_special_characters():
    assert solve("#@%$") == "#@%$"

def test_mixed_letters_numbers():
    assert solve("a1b2c") == "A1B2C"

def test_mixed_letters_special_characters():
    assert solve("a#b$c%") == "A#B$C%"

def test_mixed_all_characters():
    assert solve("a1#b2$c%") == "A1#B2$C%"

def test_letters_at_beginning():
    assert solve("abc123") == "ABC123"

def test_letters_at_end():
    assert solve("123abc") == "123ABC"

def test_letters_in_middle():
    assert solve("123abc456") == "123ABC456"

def test_no_letters():
    assert solve("1234#@") == "#@4321"

def test_single_letter():
    assert solve("a") == "A"

def test_single_number():
    assert solve("1") == "1"

def test_single_special_character():
    assert solve("#") == "#"

def test_long_string_with_letters():
    long_string = "a" * 1000 + "123"
    expected_string = "A" * 1000 + "123"
    assert solve(long_string) == expected_string

def test_long_string_no_letters():
    long_string = "1" * 1000 + "#@%"
    expected_string = "#@%" + "1" * 1000
    assert solve(long_string) == expected_string
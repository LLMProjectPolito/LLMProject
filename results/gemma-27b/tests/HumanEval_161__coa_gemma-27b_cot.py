import pytest
import math


# Focus: Character Type Handling
import pytest

def test_no_letters():
    assert solve("1234") == "4321"

def test_all_letters():
    assert solve("ab") == "AB"

def test_mixed_characters():
    assert solve("#a@C") == "#A@c"

def test_empty_string():
    assert solve("") == ""

def test_single_letter_lowercase():
    assert solve("a") == "A"

def test_single_letter_uppercase():
    assert solve("A") == "a"

def test_numbers_and_letters():
    assert solve("a1b2C") == "A1B2c"

def test_special_characters_and_letters():
    assert solve("!a@B#") == "!A@b#"

# Focus: Empty/All Non-Letter Strings
import pytest

def test_empty_string():
    assert solve("") == ""

def test_all_non_letter_strings():
    assert solve("1234") == "4321"

def test_all_non_letter_strings_with_symbols():
    assert solve("#$%^") == "^%$#"

# Focus: Mixed Case & Non-Letter Characters
import pytest

def test_mixed_case_non_letter_characters():
    assert solve("#a@C") == "#A@c"

def test_only_non_letter_characters():
    assert solve("1234") == "4321"

def test_mixed_case_and_numbers():
    assert solve("a1B2c") == "A1b2C"
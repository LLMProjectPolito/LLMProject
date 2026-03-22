import pytest
import math


# Focus: Character Type Handling
def test_character_type_handling_letters():
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"
    assert solve("HeLlO") == "hElLo"

def test_character_type_handling_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "^%$#@!"
    assert solve("") == ""

def test_character_type_handling_mixed():
    assert solve("a1b2c") == "A1B2C"
    assert solve("1a2b3c") == "1A2B3C"
    assert solve("a1@b2#c") == "A1@B2#C"

# Focus: Empty/All Non-Letter Strings
def test_solve_empty_string():
    assert solve("") == ""

def test_solve_all_non_letter_strings():
    assert solve("1234") == "4321"

def test_solve_all_non_letter_strings_with_symbols():
    assert solve("#$%^") == "^%$#"

# Focus: Mixed Case & Non-Letter Characters
def test_mixed_case_non_letter_characters_1():
    assert solve("#a@C") == "#A@c"

def test_mixed_case_non_letter_characters_2():
    assert solve("1234") == "4321"

def test_mixed_case_non_letter_characters_3():
    assert solve("aBcDeFg") == "AbCdEfG"
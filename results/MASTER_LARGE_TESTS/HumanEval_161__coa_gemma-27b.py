import pytest
import math


# Focus: Character Type/Case Sensitivity
def test_case_sensitivity_lowercase():
    assert solve("ab") == "AB"

def test_case_sensitivity_uppercase():
    assert solve("AB") == "ab"

def test_case_sensitivity_mixed_case():
    assert solve("#a@C") == "#A@c"

# Focus: Empty/All Non-Letter Strings
def test_empty_string():
    assert solve("") == ""

def test_all_non_letter_strings():
    assert solve("1234") == "4321"

def test_mixed_non_letter_strings():
    assert solve("!@#$%^") == "^%$#@!"

# Focus: Mixed Letter and Non-Letter Strings
def test_mixed_string_1():
    assert solve("#a@C") == "#A@c"

def test_mixed_string_2():
    assert solve("a1b2c") == "A1B2C"

def test_mixed_string_3():
    assert solve("1a2B3c") == "1A2b3C"
import pytest
import math


# Focus: Boundary Values
def test_boundary_empty_string():
    assert solve("") == ""

def test_boundary_single_letter():
    assert solve("a") == "A"
    assert solve("A") == "a"

def test_boundary_single_non_letter():
    assert solve("1") == "1"
    assert solve("#") == "#"

# Focus: Type Scenarios
def test_type_scenario_all_letters():
    assert solve("abc") == "ABC"

def test_type_scenario_mixed_letters_and_numbers():
    assert solve("a1b2c") == "A1B2C"

def test_type_scenario_special_characters_and_letters():
    assert solve("#a@C") == "#A@c"

# Focus: Logic Branches
def test_solve_all_letters():
    assert solve("ab") == "AB"
    assert solve("aB") == "Ab"
    assert solve("aBcDeFg") == "AbCdEfG"

def test_solve_no_letters():
    assert solve("1234") == "4321"
    assert solve("!@#$%^") == "!@#$%^"

def test_solve_mixed_letters_and_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("1a2B3c") == "1A2b3C"
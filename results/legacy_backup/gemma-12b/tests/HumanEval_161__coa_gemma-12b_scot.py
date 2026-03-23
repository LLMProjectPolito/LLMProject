import pytest
import math


# Focus: Boundary Values
def test_solve_empty_string():
    assert solve("") == ""

def test_solve_all_numbers():
    assert solve("12345") == "54321"

def test_solve_all_letters_lower():
    assert solve("abc") == "ABC"

def test_solve_all_letters_upper():
    assert solve("ABC") == "abc"

# Focus: Type Scenarios
def test_solve_no_letters_reverse():
    assert solve("1234") == "4321"

def test_solve_all_letters_reverse_case():
    assert solve("ab") == "AB"

def test_solve_mixed_letters_and_symbols_reverse_case():
    assert solve("#a@C") == "#A@c"

# Focus: Logic Branches
def test_solve_no_letters_reverse():
    assert solve("1234") == "4321"

def test_solve_all_letters_reverse_case():
    assert solve("ab") == "AB"

def test_solve_mixed_letters_and_symbols_reverse_case():
    assert solve("#a@C") == "#A@c"
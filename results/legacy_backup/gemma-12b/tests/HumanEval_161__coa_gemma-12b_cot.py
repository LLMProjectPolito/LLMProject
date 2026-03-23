import pytest
import math


# Focus: Boundary Values
def test_solve_empty_string():
    assert solve("") == ""

def test_solve_all_numbers():
    assert solve("12345") == "54321"

def test_solve_all_lowercase():
    assert solve("abc") == "ABC"

def test_solve_all_uppercase():
    assert solve("ABC") == "abc"

def test_solve_mixed_case_and_symbols():
    assert solve("#a@C") == "#A@c"

def test_solve_single_letter():
    assert solve("a") == "A"

def test_solve_single_number():
    assert solve("1") == "1"

def test_solve_single_symbol():
    assert solve("#") == "#"

# Focus: Type Scenarios
import pytest

def test_solve_no_letters_reverse():
    assert solve("1234") == "4321"

def test_solve_all_letters_case_swap():
    assert solve("ab") == "AB"

def test_solve_mixed_letters_and_symbols_case_swap():
    assert solve("#a@C") == "#A@c"

# Focus: Logic Branches
def test_solve_no_letters_reverse():
    assert solve("1234") == "4321"

def test_solve_all_letters_case_swap():
    assert solve("ab") == "AB"

def test_solve_mixed_letters_and_symbols_case_swap():
    assert solve("#a@C") == "#A@c"
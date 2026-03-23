import pytest
import math


# Focus: Boundary Values
def test_solve_empty_string():
    assert solve("") == ""

def test_solve_string_with_only_numbers():
    assert solve("1234") == "4321"

def test_solve_string_with_only_special_characters():
    assert solve("#$%^") == "#$%^"

# Focus: Type Scenarios
def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_all_letters():
    assert solve("ab") == "AB"

def test_solve_mixed():
    assert solve("#a@C") == "#A@c"

# Focus: Logic Branches
def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_all_letters():
    assert solve("ab") == "AB"

def test_solve_mixed():
    assert solve("#a@C") == "#A@c"
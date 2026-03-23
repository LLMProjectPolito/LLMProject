import pytest
import math


# Focus: Boundary Values
def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_lowercase():
    assert solve("ab") == "AB"

def test_solve_mixed_case():
    assert solve("#a@C") == "#A@c"

# Focus: Type Scenarios
def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_lowercase():
    assert solve("ab") == "AB"

def test_solve_mixed_case():
    assert solve("#a@C") == "#A@c"

# Focus: Logic Branches
def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_lowercase():
    assert solve("ab") == "AB"

def test_solve_mixed_case():
    assert solve("#a@C") == "#A@c"
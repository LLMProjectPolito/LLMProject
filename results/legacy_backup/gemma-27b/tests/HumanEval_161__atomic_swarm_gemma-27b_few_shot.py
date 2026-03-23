import pytest
import math

def test_solve_basic():
    assert solve("ab") == "AB"

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_no_letters():
    assert solve("1234") == "4321"
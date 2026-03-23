import pytest

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_all_letters():
    assert solve("ab") == "AB"

def test_solve_mixed():
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_letter():
    assert solve("a") == "A"

def test_solve_single_non_letter():
    assert solve("1") == "1"

def test_solve_long_string():
    assert solve("Hello, World!") == "hELLO, wORLD!"

def test_solve_all_non_letters():
    assert solve("!@#$%^&*()") == ")(&^%$#@!"

def test_solve_single_uppercase_letter():
    assert solve("A") == "a"

def test_solve_single_lowercase_letter():
    assert solve("a") == "A"
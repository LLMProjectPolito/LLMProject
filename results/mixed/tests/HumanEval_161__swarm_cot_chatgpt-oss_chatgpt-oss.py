import pytest

def test_solve_whitespace_only_reverses_order():
    """String contains only whitespace characters (no letters), should be reversed."""
    assert solve(" \t\n") == "\n\t "

def test_solve_empty_string():
    """Edge case: empty input should return an empty string."""
    assert solve("") == ""
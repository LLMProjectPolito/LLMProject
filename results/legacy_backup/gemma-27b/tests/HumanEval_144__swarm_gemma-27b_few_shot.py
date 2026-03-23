import pytest

def test_simplify_large_numbers():
    assert simplify("123456789/987654321", "987654321/123456789") == True
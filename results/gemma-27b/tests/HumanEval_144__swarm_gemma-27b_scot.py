import pytest

def test_simplify_large_numbers_with_common_factor():
    assert simplify("1000/2", "2/1") == True

def test_simplify_edge_case():
    assert simplify("2/4", "6/3") == True

def test_simplify_large_common_factor():
    assert simplify("2/4", "6/3") == True
import pytest

def test_simplify_large_common_factor():
    assert simplify("2/4", "6/3") == True

def test_edge_case_large_prime_denominator():
    assert simplify("1/7", "14/1") == False
    assert simplify("1/7", "7/1") == True
    assert simplify("1/11", "22/1") == True
    assert simplify("1/13", "26/1") == True
    assert simplify("1/17", "34/1") == True
    assert simplify("1/19", "38/1") == True
    assert simplify("1/23", "46/1") == True
    assert simplify("1/29", "58/1") == True
    assert simplify("1/31", "62/1") == True
    assert simplify("1/37", "74/1") == True
    assert simplify("1/41", "82/1") == True
    assert simplify("1/43", "86/1") == True
    assert simplify("1/47", "94/1") == True
    assert simplify("1/53", "106/1") == True
    assert simplify("1/59", "118/1") == True
    assert simplify("1/61", "122/1") == True
    assert simplify("1/67", "134/1") == True
    assert simplify("1/71", "142/1") == True
    assert simplify("1/73", "146/1") == True
    assert simplify("1/79", "158/1") == True
    assert simplify("1/83", "166/1") == True
    assert simplify("1/89", "178/1") == True
    assert simplify("1/97", "194/1") == True
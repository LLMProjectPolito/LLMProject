
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

import pytest

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0

def test_get_max_triples_one():
    assert get_max_triples(1) == 0

def test_get_max_triples_two():
    assert get_max_triples(2) == 0

def test_get_max_triples_three():
    assert get_max_triples(3) == 1

def test_get_max_triples_four():
    assert get_max_triples(4) == 1

def test_get_max_triples_five():
    assert get_max_triples(5) == 1

def test_get_max_triples_six():
    assert get_max_triples(6) == 3

def test_get_max_triples_seven():
    assert get_max_triples(7) == 6

def test_get_max_triples_eight():
    assert get_max_triples(8) == 10

def test_get_max_triples_nine():
    assert get_max_triples(9) == 16

def test_get_max_triples_ten():
    assert get_max_triples(10) == 22

def test_get_max_triples_large():
    assert get_max_triples(100) == 161700

def test_get_max_triples_mod_values():
    n = 1000
    result = get_max_triples(n)
    assert isinstance(result, int)
    assert result >= 0

def test_get_max_triples_edge_case():
    assert get_max_triples(1001) == 1671706
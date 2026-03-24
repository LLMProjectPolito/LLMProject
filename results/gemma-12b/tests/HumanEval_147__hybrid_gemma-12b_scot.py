
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
from your_module import get_max_triples  # Replace your_module

def test_get_max_triples_n_0():
    assert get_max_triples(0) == 0

def test_get_max_triples_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n_4():
    assert get_max_triples(4) == 0

def test_get_max_triples_n_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_6():
    assert get_max_triples(6) == 2

def test_get_max_triples_n_7():
    assert get_max_triples(7) == 3

def test_get_max_triples_n_8():
    assert get_max_triples(8) == 4

def test_get_max_triples_n_9():
    assert get_max_triples(9) == 6

def test_get_max_triples_n_10():
    assert get_max_triples(10) == 8

def test_get_max_triples_n_15():
    assert get_max_triples(15) == 24

def test_get_max_triples_n_20():
    assert get_max_triples(20) == 135

def test_get_max_triples_n_no_triples():
    assert get_max_triples(4) == 0

def test_get_max_triples_n_many_triples():
    assert get_max_triples(15) == 24
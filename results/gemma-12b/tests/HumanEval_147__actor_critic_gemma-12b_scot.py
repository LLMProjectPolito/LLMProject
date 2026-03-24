
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

def test_get_max_triples_n_negative():
    assert get_max_triples(-1) == 0

def test_get_max_triples_n_equals_0():
    assert get_max_triples(0) == 0

def test_get_max_triples_n_equals_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_equals_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_equals_3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n_equals_4():
    assert get_max_triples(4) == 0

def test_get_max_triples_n_equals_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_equals_6():
    assert get_max_triples(6) == 2

def test_get_max_triples_n_equals_7():
    assert get_max_triples(7) == 3

def test_get_max_triples_n_equals_10():
    assert get_max_triples(10) == 10

def test_get_max_triples_n_equals_15():
    assert get_max_triples(15) == 45

def test_get_max_triples_n_equals_20():
    assert get_max_triples(20) == 114

def test_get_max_triples_n_equals_100():
    assert get_max_triples(100) == 3316
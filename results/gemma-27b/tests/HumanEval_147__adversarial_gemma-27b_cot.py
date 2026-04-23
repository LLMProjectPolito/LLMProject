
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

def test_get_max_triples_small():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 1

def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_larger():
    assert get_max_triples(6) == 3
    assert get_max_triples(7) == 6
    assert get_max_triples(8) == 10
    assert get_max_triples(9) == 16

def test_get_max_triples_mod_3():
    n = 10
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    assert get_max_triples(n) == count

def test_get_max_triples_large_n():
    n = 20
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    assert get_max_triples(n) == count

def test_get_max_triples_n_is_3k():
    assert get_max_triples(9) == 16
    assert get_max_triples(12) == 36

def test_get_max_triples_n_is_3k_plus_1():
    assert get_max_triples(10) == 20
    assert get_max_triples(13) == 45

def test_get_max_triples_n_is_3k_plus_2():
    assert get_max_triples(11) == 30
    assert get_max_triples(14) == 56
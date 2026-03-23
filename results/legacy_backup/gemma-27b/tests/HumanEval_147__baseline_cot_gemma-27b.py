import pytest

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
    if n < 3:
        return 0
    return n * (n - 1) * (n - 2) // 6

def test_basic_cases():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 1
    assert get_max_triples(4) == 4
    assert get_max_triples(5) == 10

def test_edge_cases():
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_larger_values():
    assert get_max_triples(10) == 120
    assert get_max_triples(20) == 1140
    assert get_max_triples(50) == 19600

def test_n_choose_3():
    assert get_max_triples(6) == 20
    assert get_max_triples(7) == 35
    assert get_max_triples(8) == 56
    assert get_max_triples(9) == 84

def test_specific_cases():
    assert get_max_triples(15) == 455
    assert get_max_triples(25) == 2300
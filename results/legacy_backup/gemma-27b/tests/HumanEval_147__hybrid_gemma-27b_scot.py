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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def test_get_max_triples_zero():
    assert get_max_triples(0) == 0

def test_get_max_triples_one():
    assert get_max_triples(1) == 0

def test_get_max_triples_two():
    assert get_max_triples(2) == 0

def test_get_max_triples_five():
    assert get_max_triples(5) == 1

def test_get_max_triples_six():
    assert get_max_triples(6) == 3

def test_get_max_triples_seven():
    assert get_max_triples(7) == 6

def test_get_max_triples_ten():
    assert get_max_triples(10) == 20

def test_get_max_triples_large():
    assert get_max_triples(20) == 481
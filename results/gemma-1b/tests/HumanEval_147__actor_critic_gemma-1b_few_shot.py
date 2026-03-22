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
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def test_get_max_triples():
    assert get_max_triples(5) == 1
    assert get_max_triples(10) == 2
    assert get_max_triples(1) == 1
    assert get_max_triples(2) == 1
    assert get_max_triples(3) == 1
    assert get_max_triples(4) == 2
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 2
    assert get_max_triples(7) == 1
    assert get_max_triples(8) == 2
    assert get_max_triples(9) == 1
    assert get_max_triples(10) == 2
    assert get_max_triples(11) == 1
    assert get_max_triples(12) == 2
    assert get_max_triples(13) == 1
    assert get_max_triples(14) == 2
    assert get_max_triples(15) == 1
    assert get_max_triples(16) == 2
    assert get_max_triples(17) == 1
    assert get_max_triples(18) == 2
    assert get_max_triples(19) == 1
    assert get_max_triples(20) == 2
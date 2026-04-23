
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

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 4),
    (9, 5),
    (10, 6)
])
def test_get_max_triples(n, expected):
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n", [1,2,3,4,5,6,7,8,9,10])
def test_get_max_triples_large_n(n, expected):
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n", [10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
def test_get_max_triples_larger_n(n, expected):
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n", [20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
def test_get_max_triples_even_larger_n(n, expected):
    assert get_max_triples(n) == expected
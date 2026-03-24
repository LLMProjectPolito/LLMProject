
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

def slow_get_max_triples(n):
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
    (3, 1),
    (4, 0),
    (5, 1),
    (6, 2),
    (7, 5),
    (8, 8),
    (9, 15),
    (10, 21)
])
def test_small_n(n, expected):
    assert get_max_triples(n) == expected

def test_n_equals_1():
    assert get_max_triples(1) == 0

def test_n_equals_2():
    assert get_max_triples(2) == 0

def test_n_equals_3():
    assert get_max_triples(3) == 1

def test_n_equals_4():
    assert get_max_triples(4) == 0

def test_n_equals_5():
    assert get_max_triples(5) == 1

def test_large_n():
    n = 20
    expected = slow_get_max_triples(n)
    assert get_max_triples(n) == expected

def test_modulo_pattern():
    n = 10
    a = [i * i - i + 1 for i in range(1, n + 1)]
    modulos = [x % 3 for x in a]
    assert modulos == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]

def test_zero_result():
    assert get_max_triples(4) == 0
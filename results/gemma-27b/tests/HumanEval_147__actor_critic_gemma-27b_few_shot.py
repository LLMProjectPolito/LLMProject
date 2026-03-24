
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

def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_base_case():
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0

def test_get_max_triples_with_n_equals_6():
    assert get_max_triples(6) == 20

def test_get_max_triples_with_n_equals_7():
    assert get_max_triples(7) == 35

def test_get_max_triples_with_n_equals_8():
    assert get_max_triples(8) == 56

def test_get_max_triples_with_n_equals_9():
    assert get_max_triples(9) == 84

def test_get_max_triples_with_n_equals_10():
    assert get_max_triples(10) == 120

def test_get_max_triples_with_n_equals_11():
    assert get_max_triples(11) == 165

def test_get_max_triples_with_n_equals_12():
    assert get_max_triples(12) == 220

def test_get_max_triples_with_n_equals_15():
    assert get_max_triples(15) == 455

def test_get_max_triples_with_n_equals_20():
    assert get_max_triples(20) == 1140

def test_get_max_triples_large_n():
    assert get_max_triples(30) == 4060  # Check for performance issues with larger n

def test_get_max_triples_remainder_distribution():
    # Test case where many values have the same remainder when divided by 3
    n = 10
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # In this case, a[i] % 3 will be 1, 0, 1, 1, 0, 1, 1, 0, 1, 1
    assert get_max_triples(n) == 120
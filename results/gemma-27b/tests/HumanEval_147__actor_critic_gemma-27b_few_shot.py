
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

# Base Cases
def test_get_max_triples_base_cases():
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0

# Small Values
def test_get_max_triples_small_values():
    assert get_max_triples(4) == 0
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 20
    assert get_max_triples(7) == 35
    assert get_max_triples(8) == 56
    assert get_max_triples(9) == 84
    assert get_max_triples(10) == 120

# Larger Values
def test_get_max_triples_larger_values():
    assert get_max_triples(11) == 165
    assert get_max_triples(12) == 220
    assert get_max_triples(15) == 455
    assert get_max_triples(20) == 1140
    assert get_max_triples(50) == 19600  # Added larger value
    assert get_max_triples(100) == 161700 # Added larger value
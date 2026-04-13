
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

# Optimized Solution (O(n^2))
def get_max_triples_optimized(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    rem0 = 0
    rem1 = 0
    rem2 = 0
    for x in a:
        if x % 3 == 0:
            rem0 += 1
        elif x % 3 == 1:
            rem1 += 1
        else:
            rem2 += 1
    
    ans = 0
    ans += rem0 * (rem0 - 1) * (rem0 - 2) // 6
    ans += rem1 * (rem1 - 1) * (rem1 - 2) // 6
    ans += rem2 * (rem2 - 1) * (rem2 - 2) // 6
    ans += rem0 * rem1 * rem2
    return ans

def test_get_max_triples_example():
    assert get_max_triples_optimized(5) == 1
    assert get_max_triples(5) == 1

def test_get_max_triples_small_values():
    assert get_max_triples_optimized(4) == 0
    assert get_max_triples(4) == 0

def test_get_max_triples_larger_values():
    assert get_max_triples_optimized(6) == 20
    assert get_max_triples(6) == 20
    assert get_max_triples_optimized(7) == 35
    assert get_max_triples(7) == 35
    assert get_max_triples_optimized(8) == 56
    assert get_max_triples(8) == 56
    assert get_max_triples_optimized(9) == 84
    assert get_max_triples(9) == 84
    assert get_max_triples_optimized(10) == 120
    assert get_max_triples(10) == 120
    assert get_max_triples_optimized(11) == 165
    assert get_max_triples(11) == 165
    assert get_max_triples_optimized(12) == 220
    assert get_max_triples(12) == 220
    assert get_max_triples_optimized(13) == 286
    assert get_max_triples(13) == 286
    assert get_max_triples_optimized(14) == 364
    assert get_max_triples(14) == 364
    assert get_max_triples_optimized(15) == 455
    assert get_max_triples(15) == 455

def test_get_max_triples_large_n():
    assert get_max_triples_optimized(100) == 161700
    assert get_max_triples(100) == 161700

def test_get_max_triples_16():
    assert get_max_triples_optimized(16) == 560
    assert get_max_triples(16) == 560

def test_get_max_triples_17():
    assert get_max_triples_optimized(17) == 680
    assert get_max_triples(17) == 680

def test_get_max_triples_multiple_of_3():
    assert get_max_triples_optimized(30) == 4060
    assert get_max_triples(30) == 4060

def test_get_max_triples_1000():
    assert get_max_triples_optimized(1000) == 166667000
    assert get_max_triples(1000) == 166667000
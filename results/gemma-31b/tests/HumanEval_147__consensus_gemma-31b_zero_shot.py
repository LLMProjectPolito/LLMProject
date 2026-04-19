
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
from math import comb

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (-5, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
    (7, 10),
    (8, 11),
    (9, 21),
    (10, 36),
])
def test_get_max_triples_parametrized(n, expected):
    """Test various values of n based on the derived mathematical formula:
    C0 = (n + 1) // 3
    C1 = n - C0
    Result = comb(C0, 3) + comb(C1, 3)
    """
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """Test with larger n to ensure efficiency and correctness using math.comb."""
    # n = 100
    # C0 = 101 // 3 = 33
    # C1 = 100 - 33 = 67
    assert get_max_triples(100) == comb(33, 3) + comb(67, 3)
    
    # n = 1000
    # C0 = 1001 // 3 = 333
    # C1 = 1000 - 333 = 667
    assert get_max_triples(1000) == comb(333, 3) + comb(667, 3)

def test_get_max_triples_consistency():
    """Test that increasing n monotonically increases or maintains the count."""
    results = [get_max_triples(n) for n in range(1, 50)]
    for i in range(1, len(results)):
        assert results[i] >= results[i-1]

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
import math

@pytest.mark.parametrize("n, expected", [
    (2, 0),  # Small n: array length smaller than required triple size (3)
    (3, 0),  # Boundary n: smallest n where a triple can be formed, but sum is not a multiple of 3
    (8, 11), # n=8: c0=3, c1=5 -> combinations(3, 3) + combinations(5, 3) = 1 + 10 = 11
])
def test_get_max_triples(n, expected):
    assert get_max_triples(n) == expected
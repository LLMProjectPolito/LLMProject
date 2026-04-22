
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

def get_expected(n):
    """
    Helper to calculate the expected number of triples using the mathematical pattern.
    a[i] % 3 is 0 if i % 3 == 2, and 1 otherwise.
    The number of 0s (c0) in the first n elements is (n + 1) // 3.
    The number of 1s (c1) is n - c0.
    """
    if n < 3:
        return 0
    c0 = (n + 1) // 3
    c1 = n - c0
    return comb(c0, 3) + comb(c1, 3)

def test_get_max_triples_example():
    """Test the specific example provided in the problem description."""
    # a = [1, 3, 7, 13, 21], n = 5
    # a % 3 = [1, 0, 1, 1, 0]
    # Triples: (1, 7, 13) -> 1+7+13 = 21 (multiple of 3)
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n, expected", [
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
    """Test various values of n including small edge cases and sequence progression."""
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """Test larger values of n to ensure efficiency and correctness."""
    assert get_max_triples(100) == 53361
    assert get_max_triples(1000) == get_expected(1000)

def test_get_max_triples_consistency():
    """Verify that the function output matches the mathematical model for a range of n."""
    for n in range(1, 100):
        assert get_max_triples(n) == get_expected(n)

def test_get_max_triples_monotonicity():
    """Tests that the number of triples is non-decreasing as n increases."""
    for n in range(1, 100):
        assert get_max_triples(n) <= get_max_triples(n + 1)
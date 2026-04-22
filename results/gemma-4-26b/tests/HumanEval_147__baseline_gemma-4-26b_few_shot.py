
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

@pytest.mark.parametrize("n, expected", [
    (1, 0),      # a = [1], no triples possible
    (2, 0),      # a = [1, 3], no triples possible
    (3, 0),      # a = [1, 3, 7], sum = 11 (not multiple of 3)
    (4, 1),      # a = [1, 3, 7, 13], triple (1, 7, 13) sum = 21
    (5, 1),      # a = [1, 3, 7, 13, 21], triple (1, 7, 13) sum = 21
    (6, 4),      # a = [1, 3, 7, 13, 21, 31], triples: (1,7,13), (1,7,31), (1,13,31), (7,13,31)
    (10, 36),    # c1=7, c0=3 -> comb(7,3) + comb(3,3) = 35 + 1 = 36
    (100, 53361) # c1=67, c0=33 -> comb(67,3) + comb(33,3) = 47905 + 5456 = 53361
])
def test_get_max_triples_logic(n, expected):
    """Tests the core logic with various values of n including small, example, and larger values."""
    assert get_max_triples(n) == expected

def test_get_max_triples_minimum_input():
    """Tests the smallest possible valid input."""
    assert get_max_triples(1) == 0

def test_get_max_triples_pattern_consistency():
    """
    Verifies the mathematical pattern: 
    a[i] % 3 follows the sequence 1, 0, 1, 1, 0, 1, 1, 0, 1...
    The number of triples should only depend on counts of 0s and 1s.
    """
    # For n=9, c1=6, c0=3. Triples = comb(6,3) + comb(3,3) = 20 + 1 = 21
    assert get_max_triples(9) == 21
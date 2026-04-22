
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
def test_get_max_triples_small_values(n, expected):
    """Tests small values of n to ensure basic logic and edge cases (n < 3) are correct."""
    assert get_max_triples(n) == expected

def test_get_max_triples_example():
    """Tests the specific example provided in the problem description."""
    # n = 5, a = [1, 3, 7, 13, 21], remainders = [1, 0, 1, 1, 0]
    # Only (1, 7, 13) works -> (1, 1, 1) mod 3
    assert get_max_triples(5) == 1

def test_get_max_triples_large_values():
    """Tests larger values of n to ensure performance and correct combination handling."""
    # For n = 100:
    # c0 (indices i where i % 3 == 2): 2, 5, ..., 98 -> 33 elements
    # c1 (the rest): 100 - 33 = 67 elements
    # Result: comb(33, 3) + comb(67, 3) = 5456 + 47905 = 53361
    assert get_max_triples(100) == 53361
    
    # For n = 1000:
    # c0 (indices i where i % 3 == 2): 2, 5, ..., 998 -> 333 elements
    # c1 (the rest): 1000 - 333 = 667 elements
    # Result: comb(333, 3) + comb(667, 3) = 6099006 + 49234605 = 55333611
    assert get_max_triples(1000) == 55333611

def test_get_max_triples_type_integrity():
    """Ensures the function returns an integer."""
    result = get_max_triples(10)
    assert isinstance(result, int)
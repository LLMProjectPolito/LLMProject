
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
    (100, 53361),
])
def test_get_max_triples_parametrized(n, expected):
    """Tests the get_max_triples function with various inputs based on the logic:
    a[i] mod 3 is 0 if i % 3 == 2, else 1.
    Total triples = comb(C0, 3) + comb(C1, 3).
    """
    assert get_max_triples(n) == expected

def test_get_max_triples_too_small():
    """Test cases where n is smaller than 3, making it impossible to form a triple."""
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_minimum_triple():
    """Test n=3, where only one triple exists but it does not sum to a multiple of 3."""
    # a = [1, 3, 7] -> mods [1, 0, 1]. Sum = 2 mod 3.
    assert get_max_triples(3) == 0

def test_get_max_triples_large_n():
    """Test larger values of n to ensure performance and robustness."""
    # n = 1000
    # C0 = (1000 + 1) // 3 = 333
    # C1 = 1000 - 333 = 667
    # comb(333, 3) = 6100746
    # comb(667, 3) = 49234495
    # Expected = 55335241
    assert get_max_triples(1000) == 55335241

def test_get_max_triples_very_large_n():
    """Test with a very large n to verify complexity is not O(n^3)."""
    n = 10**6
    c0 = n // 3
    c1 = n - c0
    expected = (c0 * (c0 - 1) * (c0 - 2) // 6) + (c1 * (c1 - 1) * (c1 - 2) // 6)
    assert get_max_triples(n) == expected

def test_get_max_triples_type_consistency():
    """Ensure the function returns an integer."""
    result = get_max_triples(5)
    assert isinstance(result, int)
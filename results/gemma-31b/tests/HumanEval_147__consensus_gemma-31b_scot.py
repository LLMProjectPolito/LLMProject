
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
    (1, 0),   # Not enough elements for a triple
    (2, 0),   # Not enough elements for a triple
    (3, 0),   # a = [1, 3, 7] -> mods [1, 0, 1]. No triples.
    (4, 1),   # a = [1, 3, 7, 13] -> mods [1, 0, 1, 1]. Triple (1, 7, 13)
    (5, 1),   # a = [1, 3, 7, 13, 21] -> mods [1, 0, 1, 1, 0]. Triple (1, 7, 13)
    (6, 4),   # mods [1, 0, 1, 1, 0, 1]. c0=2, c1=4. comb(2,3)+comb(4,3) = 0 + 4 = 4
    (7, 10),  # mods [1, 0, 1, 1, 0, 1, 1]. c0=2, c1=5. comb(2,3)+comb(5,3) = 0 + 10 = 10
    (8, 11),  # mods [1, 0, 1, 1, 0, 1, 1, 0]. c0=3, c1=5. comb(3,3)+comb(5,3) = 1 + 10 = 11
    (9, 21),  # mods [1, 0, 1, 1, 0, 1, 1, 0, 1]. c0=3, c1=6. comb(3,3)+comb(6,3) = 1 + 20 = 21
    (10, 36), # mods [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]. c0=3, c1=7. comb(3,3)+comb(7,3) = 1 + 35 = 36
])
def test_get_max_triples_values(n, expected):
    """Test various small values of n to verify the combination logic."""
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """
    Test with a larger n to ensure the logic scales.
    For n = 100:
    c0 = (100 + 1) // 3 = 33
    c1 = 100 - 33 = 67
    Result = comb(33, 3) + comb(67, 3) = 5456 + 47905 = 53361
    """
    assert get_max_triples(100) == 53361

def test_get_max_triples_type_consistency():
    """Ensure the output is always an integer."""
    assert isinstance(get_max_triples(10), int)
    assert isinstance(get_max_triples(100), int)

def test_get_max_triples_monotonicity():
    """Increasing n should never decrease the number of valid triples."""
    for n in range(1, 50):
        assert get_max_triples(n + 1) >= get_max_triples(n)
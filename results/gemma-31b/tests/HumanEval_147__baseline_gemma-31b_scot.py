
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

# The function get_max_triples is already defined in the environment.
# We are writing the test suite for it.

@pytest.mark.parametrize("n, expected", [
    (1, 0),  # Not enough elements for a triple
    (2, 0),  # Not enough elements for a triple
    (3, 0),  # a = [1, 3, 7] -> mods [1, 0, 1]. Sums: 1+0+1=2. No triples.
    (4, 1),  # a = [1, 3, 7, 13] -> mods [1, 0, 1, 1]. Triple (1, 7, 13) sum mod 3 = 0.
    (5, 1),  # Example case: a = [1, 3, 7, 13, 21] -> mods [1, 0, 1, 1, 0]. Triple (1, 7, 13) sum mod 3 = 0.
    (6, 4),  # a = [1, 3, 7, 13, 21, 31] -> mods [1, 0, 1, 1, 0, 1]. 
             # C0 = 2 (3, 21), C1 = 4 (1, 7, 13, 31).
             # Comb(2, 3) + Comb(4, 3) = 0 + 4 = 4.
])
def test_get_max_triples_parametrized(n, expected):
    """Test various small to medium values of n to verify correctness."""
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """
    Test with a larger n to ensure the logic scales.
    For n = 100:
    i % 3 == 2: i in {2, 5, ..., 98}. Count C0 = (98-2)//3 + 1 = 33.
    i % 3 == 0 or 1: Count C1 = 100 - 33 = 67.
    Result = Comb(33, 3) + Comb(67, 3)
    Comb(33, 3) = (33 * 32 * 31) / 6 = 5456
    Comb(67, 3) = (67 * 66 * 65) / 6 = 47905
    Total = 53361
    """
    n = 100
    expected = 53361
    assert get_max_triples(n) == expected

def test_get_max_triples_return_type():
    """Ensure the function returns an integer."""
    result = get_max_triples(10)
    assert isinstance(result, int)

def test_get_max_triples_positive_n():
    """Ensure the function handles the minimum positive integer input."""
    assert get_max_triples(1) == 0

def test_get_max_triples_consistency():
    """Verify that increasing n monotonically increases or keeps the count same."""
    prev_result = get_max_triples(10)
    next_result = get_max_triples(11)
    assert next_result >= prev_result
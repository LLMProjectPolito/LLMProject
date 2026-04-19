
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

def test_get_max_triples_example():
    """Test the example provided in the problem description."""
    # n = 5 -> a = [1, 3, 7, 13, 21]
    # Mod 3: [1, 0, 1, 1, 0]
    # Triples with sum % 3 == 0: (1, 7, 13) -> (1+1+1)%3 == 0
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n, expected", [
    (1, 0), # Not enough elements for a triple
    (2, 0), # Not enough elements for a triple
    (3, 0), # a = [1, 3, 7] -> mod 3: [1, 0, 1]. Sum = 2.
    (4, 1), # a = [1, 3, 7, 13] -> mod 3: [1, 0, 1, 1]. Triple (1, 7, 13)
    (6, 4), # a = [1, 3, 7, 13, 21, 31] -> mod 3: [1, 0, 1, 1, 0, 1]
            # Count 0s: 2, Count 1s: 4. Comb(2, 3) + Comb(4, 3) = 0 + 4 = 4
])
def test_get_max_triples_small_values(n, expected):
    """Test various small values of n to verify boundary conditions and logic."""
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """
    Test a larger value of n.
    For n = 10:
    i = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    a[i] mod 3: 1, 0, 1, 1, 0, 1, 1, 0, 1, 1
    Count of 0s: 3 (i=2, 5, 8)
    Count of 1s: 7 (i=1, 3, 4, 6, 7, 9, 10)
    Triples: Comb(3, 3) + Comb(7, 3) = 1 + (7*6*5)/(3*2*1) = 1 + 35 = 36
    """
    assert get_max_triples(10) == 36

def test_get_max_triples_positive_integer():
    """Ensure the function handles the minimum positive integer input."""
    assert get_max_triples(1) == 0

def test_get_max_triples_consistency():
    """Verify that increasing n monotonically increases or maintains the count."""
    prev_result = 0
    for n in range(1, 20):
        current_result = get_max_triples(n)
        assert current_result >= prev_result
        prev_result = current_result
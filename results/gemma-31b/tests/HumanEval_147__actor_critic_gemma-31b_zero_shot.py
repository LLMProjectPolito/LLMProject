
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
from itertools import combinations

def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.
    """
    if n < 3:
        return 0
    
    # Analysis of a[i] % 3:
    # i % 3 == 0: a[i] = 0^2 - 0 + 1 = 1 (mod 3)
    # i % 3 == 1: a[i] = 1^2 - 1 + 1 = 1 (mod 3)
    # i % 3 == 2: a[i] = 2^2 - 2 + 1 = 3 = 0 (mod 3)
    # Thus, a[i] is 0 mod 3 if i % 3 == 2, and 1 mod 3 otherwise.
    
    # Count of elements where a[i] % 3 == 0
    c0 = (n + 1) // 3
    # Count of elements where a[i] % 3 == 1
    c1 = n - c0
    
    def combinations_3(count):
        if count < 3:
            return 0
        return count * (count - 1) * (count - 2) // 6

    return combinations_3(c0) + combinations_3(c1)

@pytest.mark.parametrize("n, expected", [
    (1, 0),   # Too few elements for a triple
    (2, 0),   # Too few elements for a triple
    (3, 0),   # a = [1, 3, 7] -> mods [1, 0, 1]. Sum = 2.
    (4, 1),   # a = [1, 3, 7, 13] -> mods [1, 0, 1, 1]. Triple (1, 7, 13) sum mod 3 = 0.
    (5, 1),   # Example case: a = [1, 3, 7, 13, 21] -> mods [1, 0, 1, 1, 0]. Triple (1, 7, 13).
    (6, 4),   # c0=2, c1=4 -> comb(2,3) + comb(4,3) = 0 + 4 = 4
    (7, 10),  # c0=2, c1=5 -> comb(2,3) + comb(5,3) = 0 + 10 = 10
    (8, 11),  # c0=3, c1=5 -> comb(3,3) + comb(5,3) = 1 + 10 = 11
    (9, 21),  # c0=3, c1=6 -> comb(3,3) + comb(6,3) = 1 + 20 = 21
])
def test_get_max_triples_standard_cases(n, expected):
    """Test standard small values of n including the provided example."""
    assert get_max_triples(n) == expected

def test_get_max_triples_brute_force_comparison():
    """
    Verify the optimized logic against a brute-force implementation 
    for a medium-sized n to avoid tautological testing.
    """
    def brute_force_get_max_triples(n):
        a = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for triple in combinations(a, 3):
            if sum(triple) % 3 == 0:
                count += 1
        return count

    # Test for a medium range of n to ensure the mathematical logic holds
    for n in range(3, 50):
        assert get_max_triples(n) == brute_force_get_max_triples(n)

def test_get_max_triples_large_n_performance():
    """Test with a very large n to ensure efficiency (O(1) time complexity)."""
    n = 10**12
    # This should return almost instantly if the implementation is O(1)
    result = get_max_triples(n)
    assert isinstance(result, int)
    assert result > 0
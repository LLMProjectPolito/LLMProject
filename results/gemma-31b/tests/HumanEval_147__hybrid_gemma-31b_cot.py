
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

def calculate_expected(n):
    """
    Helper to calculate the expected number of triples for verification.
    The sequence is a[i] = i^2 - i + 1.
    Modulo 3 analysis:
    - i % 3 == 0 -> a[i] % 3 = 1
    - i % 3 == 1 -> a[i] % 3 = 1
    - i % 3 == 2 -> a[i] % 3 = 0
    
    A triple sums to a multiple of 3 if:
    1. All three are 0 mod 3: comb(C0, 3)
    2. All three are 1 mod 3: comb(C1, 3)
    3. One of each (0, 1, 2 mod 3): C0 * C1 * C2 (C2 is always 0)
    """
    if n < 3:
        return 0
    
    # C0: count of i in [1, n] such that i % 3 == 2
    c0 = (n + 1) // 3
    # C1: count of i in [1, n] such that i % 3 != 2
    c1 = n - c0
    
    def combinations_3(k):
        if k < 3:
            return 0
        return k * (k - 1) * (k - 2) // 6
    
    return combinations_3(c0) + combinations_3(c1)

class TestGetMaxTriples:
    """Comprehensive test suite for get_max_triples function."""

    @pytest.mark.parametrize("n, expected", [
        (1, 0),   # Too small
        (2, 0),   # Too small
        (3, 0),   # C0=1, C1=2 -> 0 + 0 = 0
        (4, 1),   # C0=1, C1=3 -> 0 + 1 = 1
        (5, 1),   # C0=2, C1=3 -> 0 + 1 = 1
        (6, 4),   # C0=2, C1=4 -> 0 + 4 = 4
        (7, 10),  # C0=2, C1=5 -> 0 + 10 = 10
        (8, 11),  # C0=3, C1=5 -> 1 + 10 = 11
        (9, 21),  # C0=3, C1=6 -> 1 + 20 = 21
        (10, 36), # C0=3, C1=7 -> 1 + 35 = 36
    ])
    def test_small_values(self, n, expected):
        """Test the function with small known values including edge cases."""
        assert get_max_triples(n) == expected

    @pytest.mark.parametrize("n", [
        30, 100, 500, 1000, 10000
    ])
    def test_larger_values(self, n):
        """Test the function with larger values using the mathematical helper."""
        assert get_max_triples(n) == calculate_expected(n)

    def test_very_large_n(self):
        """
        Test with a very large n to ensure O(1) or O(log n) efficiency 
        and verify Python's arbitrary-precision integers.
        """
        n = 10**9
        assert get_max_triples(n) == calculate_expected(n)

    def test_modulo_patterns(self):
        """Verify correctness across different modulo 3 residues of n."""
        # n = 3k
        assert get_max_triples(3) == calculate_expected(3)
        assert get_max_triples(6) == calculate_expected(6)
        assert get_max_triples(9) == calculate_expected(9)
        
        # n = 3k + 1
        assert get_max_triples(4) == calculate_expected(4)
        assert get_max_triples(7) == calculate_expected(7)
        assert get_max_triples(10) == calculate_expected(10)
        
        # n = 3k + 2
        assert get_max_triples(2) == calculate_expected(2)
        assert get_max_triples(5) == calculate_expected(5)
        assert get_max_triples(8) == calculate_expected(8)

    def test_minimum_positive_integer(self):
        """Verify the smallest possible positive integer input."""
        assert get_max_triples(1) == 0
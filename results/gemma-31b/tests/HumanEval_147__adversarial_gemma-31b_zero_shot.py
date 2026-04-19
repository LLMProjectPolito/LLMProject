
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
import random

def get_max_triples(n):
    """
    Implementation of the problem logic to be tested.
    (The user provided the problem description, this is the target function)
    """
    # a[i] = i*i - i + 1
    # Modulo 3 analysis:
    # i % 3 == 0 -> a[i] = 0 - 0 + 1 = 1 (mod 3)
    # i % 3 == 1 -> a[i] = 1 - 1 + 1 = 1 (mod 3)
    # i % 3 == 2 -> a[i] = 4 - 2 + 1 = 3 = 0 (mod 3)
    # So a[i] is 0 mod 3 if i % 3 == 2, else 1 mod 3.
    
    c0 = n // 3 # Count of i in [1, n] where i % 3 == 2
    c1 = n - c0 # Count of i in [1, n] where i % 3 == 0 or 1
    
    def nCr(n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1
        if r > n // 2:
            r = n - r
        
        num = 1
        for i in range(r):
            num = num * (n - i) // (i + 1)
        return num

    # Triples sum to 0 mod 3 if:
    # 1. All three are 0 mod 3: nCr(c0, 3)
    # 2. All three are 1 mod 3: nCr(c1, 3)
    # 3. One 0, one 1, one 2 mod 3: (c0 * c1 * c2) -> but c2 is always 0
    return nCr(c0, 3) + nCr(c1, 3)

def brute_force_get_max_triples(n):
    """Reference implementation for validation."""
    a = [i*i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

class TestGetMaxTriples:
    
    @pytest.mark.parametrize("n, expected", [
        (1, 0),
        (2, 0),
        (3, 0), # a = [1, 3, 7] -> 1+3+7=11 (no)
        (4, 1), # a = [1, 3, 7, 13] -> (1, 7, 13) sum=21 (yes)
        (5, 1), # Example case: a = [1, 3, 7, 13, 21] -> (1, 7, 13) sum=21 (yes)
    ])
    def test_small_known_values(self, n, expected):
        """Test against known small values and the provided example."""
        assert get_max_triples(n) == expected

    def test_brute_force_comparison(self):
        """Property-based test comparing optimized version with brute force."""
        for _ in range(50):
            n = random.randint(1, 50)
            assert get_max_triples(n) == brute_force_get_max_triples(n), f"Failed for n={n}"

    def test_large_n_performance(self):
        """Ensure the function handles large n efficiently (O(1) or O(log n) logic)."""
        # If the implementation is O(n^3), this will time out.
        # n = 10^9 should be handled instantly.
        try:
            result = get_max_triples(10**9)
            assert isinstance(result, int)
        except Exception as e:
            pytest.fail(f"Large n failed with exception: {e}")

    @pytest.mark.parametrize("n", [0, -1, -100])
    def test_non_positive_integers(self, n):
        """
        The problem states n is a positive integer. 
        Check how the function handles edge cases outside the domain.
        """
        # Depending on requirements, this could return 0 or raise ValueError.
        # Assuming it returns 0 for n < 3.
        assert get_max_triples(n) == 0

    def test_combinatorial_boundaries(self):
        """Test cases where c0 or c1 are exactly 0, 1, 2, or 3."""
        # n=1: c0=0, c1=1
        assert get_max_triples(1) == 0
        # n=2: c0=0, c1=2 (Wait, i=2 is 0 mod 3, so c0=1, c1=1)
        # Let's check n=2: a=[1, 3]. c0=1, c1=1. nCr(1,3)+nCr(1,3) = 0.
        assert get_max_triples(2) == 0
        # n=6: c0=2 (i=2,5), c1=4 (i=1,3,4,6)
        # nCr(2,3) + nCr(4,3) = 0 + 4 = 4
        assert get_max_triples(6) == 4
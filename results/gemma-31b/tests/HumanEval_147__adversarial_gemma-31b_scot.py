
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
import math

# Reference implementation for validation
def reference_get_max_triples(n):
    if n < 3:
        return 0
    # a[i] % 3 == 0 if i % 3 == 2
    # a[i] % 3 == 1 if i % 3 == 0 or i % 3 == 1
    c0 = (n + 1) // 3
    c1 = n - c0
    
    def nCr(n, r):
        if r > n:
            return 0
        return math.comb(n, r)
    
    return nCr(c0, 3) + nCr(c1, 3)

class TestGetMaxTriples:
    
    @pytest.mark.parametrize("n, expected", [
        (1, 0),
        (2, 0),
    ])
    def test_boundary_conditions(self, n, expected):
        """Test cases where n is too small to form a triple."""
        assert get_max_triples(n) == expected

    def test_example_case(self):
        """Test the example provided in the problem description."""
        # n = 5 -> a = [1, 3, 7, 13, 21]
        # Mod 3: [1, 0, 1, 1, 0]
        # C0 = 2, C1 = 3
        # comb(2, 3) + comb(3, 3) = 0 + 1 = 1
        assert get_max_triples(5) == 1

    @pytest.mark.parametrize("n", [3, 4, 6, 7, 8, 9, 10])
    def test_small_values(self, n):
        """Test a variety of small n values against the reference formula."""
        assert get_max_triples(n) == reference_get_max_triples(n)

    def test_large_input(self):
        """Test with a larger n to ensure efficiency and correctness."""
        n = 1000
        # C0 = 1001 // 3 = 333
        # C1 = 1000 - 333 = 667
        # Result = comb(333, 3) + comb(667, 3)
        expected = reference_get_max_triples(n)
        assert get_max_triples(n) == expected

    @pytest.mark.parametrize("n", range(1, 100))
    def test_exhaustive_range(self, n):
        """Exhaustively test all n from 1 to 100."""
        assert get_max_triples(n) == reference_get_max_triples(n)

    def test_type_safety(self):
        """Ensure the function handles positive integers as specified."""
        # The problem states n is a positive integer.
        # We check if it handles a typical positive integer correctly.
        assert isinstance(get_max_triples(10), int)
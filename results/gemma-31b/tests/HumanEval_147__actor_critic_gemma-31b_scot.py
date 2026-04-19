
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

def calculate_expected(n):
    """
    Helper to calculate expected result based on mathematical derivation:
    a[i] % 3 == 0 if i % 3 == 2, else a[i] % 3 == 1.
    """
    # Count of i in [1, n] such that i % 3 == 2
    c0 = (n + 1) // 3
    # Count of i in [1, n] such that i % 3 == 1 or 0
    c1 = n - c0
    
    # math.comb(n, k) returns 0 if k > n, handling cases where n < 3 automatically
    return math.comb(c0, 3) + math.comb(c1, 3)

class TestGetMaxTriples:
    
    def test_example_case(self):
        """Verify the example provided in the problem description."""
        # n = 5 -> a = [1, 3, 7, 13, 21]
        # Mod 3: [1, 0, 1, 1, 0]
        # c0 = 2, c1 = 3. comb(2,3) + comb(3,3) = 0 + 1 = 1.
        assert get_max_triples(5) == 1

    @pytest.mark.parametrize("n", [0, 1, 2])
    def test_edge_cases(self, n):
        """Test the lower boundary of the input domain."""
        assert get_max_triples(n) == 0

    def test_minimum_triple_size(self):
        """Test the smallest possible n that can form a triple."""
        # n = 3 -> a = [1, 3, 7]. Mod 3: [1, 0, 1]. c0=1, c1=2. Result: 0
        assert get_max_triples(3) == 0
        # n = 4 -> a = [1, 3, 7, 13]. Mod 3: [1, 0, 1, 1]. c0=1, c1=3. Result: 1
        assert get_max_triples(4) == 1

    @pytest.mark.parametrize("n", [6, 7, 8, 9, 10, 15, 20, 100])
    def test_various_n(self, n):
        """Test a variety of n values against the derived mathematical formula."""
        expected = calculate_expected(n)
        assert get_max_triples(n) == expected

    @pytest.mark.timeout(1)
    def test_large_n(self):
        """
        Test with a very large n to ensure the implementation is O(1).
        The timeout ensures that an O(n) implementation fails the test.
        """
        n = 10**9
        expected = calculate_expected(n)
        assert get_max_triples(n) == expected
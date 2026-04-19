
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

class TestGetMaxTriples:
    """
    Superior test suite for get_max_triples(n).
    
    Logic:
    a[i] = i^2 - i + 1
    a[i] % 3 == 0 if i % 3 == 2
    a[i] % 3 == 1 if i % 3 == 0 or i % 3 == 1
    
    Total triples = comb(C0, 3) + comb(C1, 3)
    where C0 is count of i in [1, n] such that i % 3 == 2.
    """

    @pytest.mark.parametrize("n, expected", [
        (1, 0),  # C0=0, C1=1 -> 0+0=0
        (2, 0),  # C0=1, C1=1 -> 0+0=0
        (3, 0),  # C0=1, C1=2 -> 0+0=0
        (4, 1),  # C0=1, C1=3 -> 0+1=1
        (5, 1),  # C0=2, C1=3 -> 0+1=1 (Example Case)
        (6, 4),  # C0=2, C1=4 -> 0+4=4
        (7, 10), # C0=2, C1=5 -> 0+10=10
        (8, 11), # C0=3, C1=5 -> 1+10=11
        (9, 21), # C0=3, C1=6 -> 1+20=21
        (10, 36),# C0=3, C1=7 -> 1+35=36
    ])
    def test_small_values(self, n, expected):
        """Test basic functionality with small n, including the provided example."""
        assert get_max_triples(n) == expected

    def test_large_value(self):
        """
        Test with n = 100.
        C0 = (100 + 1) // 3 = 33
        C1 = 100 - 33 = 67
        Expected = comb(33, 3) + comb(67, 3) = 5456 + 47905 = 53361
        """
        n = 100
        expected = 53361
        assert get_max_triples(n) == expected

    def test_mathematical_consistency(self):
        """
        Validate the function against the combinatorial formula for a range of values.
        """
        for n in range(1, 101):
            # C0: count of i in 1..n where i % 3 == 2
            c0 = (n + 1) // 3
            c1 = n - c0
            expected = math.comb(c0, 3) + math.comb(c1, 3)
            assert get_max_triples(n) == expected, f"Failed for n={n}"

    def test_monotonicity(self):
        """The number of triples should be non-decreasing as n increases."""
        results = [get_max_triples(n) for n in range(1, 50)]
        assert results == sorted(results), "The result sequence must be non-decreasing"

    def test_return_type(self):
        """Ensure the function returns an integer."""
        assert isinstance(get_max_triples(10), int)

    def test_edge_cases(self):
        """Test for n <= 0. No triples can be formed."""
        assert get_max_triples(0) == 0
        assert get_max_triples(-1) == 0
        assert get_max_triples(-100) == 0

    def test_invalid_input_types(self):
        """Ensure the function handles unexpected types by raising an error."""
        with pytest.raises((TypeError, ValueError)):
            get_max_triples("5")
        with pytest.raises((TypeError, ValueError)):
            get_max_triples(None)
        with pytest.raises((TypeError, ValueError)):
            get_max_triples(5.5)
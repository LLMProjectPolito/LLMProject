
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

def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
    For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.
    
    Analysis:
    a[i] mod 3:
    i % 3 == 1: 1^2 - 1 + 1 = 1 (mod 3)
    i % 3 == 2: 2^2 - 2 + 1 = 3 = 0 (mod 3)
    i % 3 == 0: 3^2 - 3 + 1 = 7 = 1 (mod 3)
    
    Pattern: 1, 0, 1 repeating every 3.
    C0 (count of 0 mod 3) = (n + 1) // 3
    C1 (count of 1 mod 3) = n - C0
    C2 (count of 2 mod 3) = 0
    
    A triple sum is 0 mod 3 if residues are (0,0,0), (1,1,1), or (0,1,2).
    Since C2 = 0, total triples = comb(C0, 3) + comb(C1, 3).
    """
    if n < 3:
        return 0
    
    c0 = (n + 1) // 3
    c1 = n - c0
    
    return math.comb(c0, 3) + math.comb(c1, 3)

class TestGetMaxTriples:
    """
    Superior test suite merging comprehensive standard cases, 
    boundary analysis, property tests, and large-scale verification.
    """

    @pytest.mark.parametrize("n, expected", [
        (1, 0),   # Too small for a triple
        (2, 0),   # Too small for a triple
        (3, 0),   # a = [1, 3, 7] -> mod [1, 0, 1] -> C0=1, C1=2 -> 0+0 = 0
        (4, 1),   # a = [1, 3, 7, 13] -> mod [1, 0, 1, 1] -> C0=1, C1=3 -> 0+1 = 1
        (5, 1),   # Example case: C0=2, C1=3 -> 0+1 = 1
        (6, 4),   # C0=2, C1=4 -> 0+4 = 4
        (7, 10),  # C0=2, C1=5 -> 0+10 = 10
        (8, 11),  # C0=3, C1=5 -> 1+10 = 11
        (9, 21),  # C0=3, C1=6 -> 1+20 = 21
        (10, 36), # C0=3, C1=7 -> 1+35 = 36
        (11, 39), # C0=4, C1=7 -> 4+35 = 39
        (12, 60), # C0=4, C1=8 -> 4+56 = 60
    ])
    def test_standard_cases(self, n, expected):
        """Test a wide range of small to medium inputs to verify the combinatorial logic."""
        assert get_max_triples(n) == expected

    def test_example_consistency(self):
        """Manually verify the example n=5 to ensure the logic matches the problem description."""
        # n=5, a = [1, 3, 7, 13, 21]
        # Triples summing to multiple of 3: (1, 7, 13) = 21.
        # All others: (1,3,7)=11, (1,3,13)=17, (1,3,21)=25, (1,7,21)=29, (1,13,21)=35, 
        # (3,7,13)=23, (3,7,21)=31, (3,13,21)=37, (7,13,21)=41.
        assert get_max_triples(5) == 1

    def test_boundary_counts(self):
        """Specifically test cases where C0 or C1 exactly hit the minimum threshold for a triple (3)."""
        # C1 = 3 occurs at n=4 (C0=1, C1=3)
        assert get_max_triples(4) == math.comb(1, 3) + math.comb(3, 3)
        # C0 = 3 occurs at n=8 (C0=3, C1=5)
        assert get_max_triples(8) == math.comb(3, 3) + math.comb(5, 3)

    def test_large_n(self):
        """Test with a large value of n to ensure efficiency and correctness using math.comb."""
        n = 1000
        c0 = (n + 1) // 3
        c1 = n - c0
        expected = math.comb(c0, 3) + math.comb(c1, 3)
        assert get_max_triples(n) == expected

    def test_property_non_negative(self):
        """The result should never be negative for any positive integer n."""
        for n in range(1, 101):
            assert get_max_triples(n) >= 0

    def test_monotonicity(self):
        """The number of triples should be non-decreasing as n increases."""
        prev_result = 0
        for n in range(1, 100):
            current_result = get_max_triples(n)
            assert current_result >= prev_result, f"Failed monotonicity at n={n}"
            prev_result = current_result
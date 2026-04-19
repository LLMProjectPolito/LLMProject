
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

# The function get_max_triples is assumed to be defined in the environment.
# The logic for get_max_triples(n) is:
# a[i] = i*i - i + 1
# a[i] mod 3:
# i % 3 == 0 -> 0 - 0 + 1 = 1
# i % 3 == 1 -> 1 - 1 + 1 = 1
# i % 3 == 2 -> 4 - 2 + 1 = 3 = 0
# Let C0 be count of i in [1, n] where i % 3 == 2.
# Let C1 be count of i in [1, n] where i % 3 == 0 or 1.
# C0 = (n + 1) // 3
# C1 = n - C0
# Triples sum to multiple of 3 if:
# 1. All three are 0 mod 3: comb(C0, 3)
# 2. All three are 1 mod 3: comb(C1, 3)
# 3. One of each (0, 1, 2 mod 3): C0 * C1 * C2 (but C2 is always 0)
# Total = comb(C0, 3) + comb(C1, 3)

@pytest.mark.parametrize("n, expected", [
    (1, 0),   # C0=0, C1=1 -> 0 + 0 = 0
    (2, 0),   # C0=1, C1=1 -> 0 + 0 = 0
    (3, 0),   # C0=1, C1=2 -> 0 + 0 = 0
    (4, 1),   # C0=1, C1=3 -> 0 + 1 = 1
    (5, 1),   # C0=2, C1=3 -> 0 + 1 = 1
    (6, 4),   # C0=2, C1=4 -> 0 + 4 = 4
    (7, 10),  # C0=2, C1=5 -> 0 + 10 = 10
    (8, 11),  # C0=3, C1=5 -> 1 + 10 = 11
    (9, 21),  # C0=3, C1=6 -> 1 + 20 = 21
    (10, 36), # C0=3, C1=7 -> 1 + 35 = 36
])
def test_get_max_triples_small_values(n, expected):
    """Test the function with small values of n to verify basic logic and edge cases."""
    assert get_max_triples(n) == expected

def test_get_max_triples_large_value():
    """Test the function with a larger value of n to ensure efficiency and correctness."""
    # n = 100
    # C0 = (100 + 1) // 3 = 33
    # C1 = 100 - 33 = 67
    # comb(33, 3) = (33 * 32 * 31) / 6 = 11 * 16 * 31 = 5456
    # comb(67, 3) = (67 * 66 * 65) / 6 = 67 * 11 * 65 = 47905
    # Total = 5456 + 47905 = 53361
    assert get_max_triples(100) == 53361

def test_get_max_triples_very_large_value():
    """Test the function with a very large value of n."""
    # n = 1000
    # C0 = (1000 + 1) // 3 = 333
    # C1 = 1000 - 333 = 667
    # comb(333, 3) = (333 * 332 * 331) / 6 = 6099066
    # comb(667, 3) = (667 * 666 * 665) / 6 = 49234695
    # Total = 6099066 + 49234695 = 55333761
    assert get_max_triples(1000) == 55333761

def test_get_max_triples_minimum_n():
    """Test the absolute minimum positive integer n."""
    assert get_max_triples(1) == 0

def test_get_max_triples_boundary_triples():
    """Test n=3, the smallest n that could potentially form a triple."""
    # a = [1, 3, 7] -> mod 3: [1, 0, 1]. Sum = 2. Not multiple of 3.
    assert get_max_triples(3) == 0
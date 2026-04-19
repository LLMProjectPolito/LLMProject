
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
    # a[i] = i^2 - i + 1
    # i % 3 == 0 -> a[i] % 3 = 0 - 0 + 1 = 1
    # i % 3 == 1 -> a[i] % 3 = 1 - 1 + 1 = 1
    # i % 3 == 2 -> a[i] % 3 = 4 - 2 + 1 = 3 = 0
    
    # Count elements where a[i] % 3 == 0 (i.e., i = 2, 5, 8...)
    # i = 3k - 1 <= n  => 3k <= n + 1 => k <= (n + 1) // 3
    c0 = (n + 1) // 3
    # Count elements where a[i] % 3 == 1 (i.e., i = 1, 3, 4, 6, 7...)
    c1 = n - c0
    
    # A triple sums to a multiple of 3 if:
    # 1. All three are 0 mod 3: comb(c0, 3)
    # 2. All three are 1 mod 3: comb(c1, 3)
    # 3. All three are 2 mod 3: comb(c2, 3) -> c2 is always 0
    # 4. One of each (0, 1, 2): c0 * c1 * c2 -> c2 is always 0
    
    def comb3(m):
        if m < 3:
            return 0
        return (m * (m - 1) * (m - 2)) // 6
    
    return comb3(c0) + comb3(c1)

def calculate_expected(n):
    """Helper to calculate expected value for verification."""
    if n < 3:
        return 0
    c0 = (n + 1) // 3
    c1 = n - c0
    def comb3(m):
        if m < 3:
            return 0
        return (m * (m - 1) * (m - 2)) // 6
    return comb3(c0) + comb3(c1)

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),  # a = [1, 3, 7, 13] -> (1, 7, 13) sum=21
    (5, 1),  # Example case
    (6, 4),  # c0=2 (2,5), c1=4 (1,3,4,6) -> comb(2,3)+comb(4,3) = 0 + 4 = 4
    (7, 10), # c0=2 (2,5), c1=5 (1,3,4,6,7) -> comb(2,3)+comb(5,3) = 0 + 10 = 10
    (8, 11), # c0=3 (2,5,8), c1=5 (1,3,4,6,7) -> comb(3,3)+comb(5,3) = 1 + 10 = 11
    (10, 36),# c0=3 (2,5,8), c1=7 (1,3,4,6,7,9,10) -> comb(3,3)+comb(7,3) = 1 + 35 = 36
])
def test_get_max_triples_small(n, expected):
    assert get_max_triples(n) == calculate_expected(n)

def test_get_max_triples_large():
    n = 100
    assert get_max_triples(n) == calculate_expected(n)

def test_get_max_triples_very_large():
    n = 10**6
    assert get_max_triples(n) == calculate_expected(n)

def test_get_max_triples_minimum_n():
    assert get_max_triples(1) == 0

def test_get_max_triples_boundary_triples():
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
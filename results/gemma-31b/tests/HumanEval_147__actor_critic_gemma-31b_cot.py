
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

def nCr(n, r):
    """Helper function to calculate combinations."""
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if r > n // 2:
        r = n - r
    
    num = 1
    for i in range(r):
        num = num * (n - i) // (i + 1)
    return num

def calculate_expected(n):
    """
    Logic:
    a[i] = i*i - i + 1
    a[i] % 3:
    i % 3 == 0: 0 - 0 + 1 = 1
    i % 3 == 1: 1 - 1 + 1 = 1
    i % 3 == 2: 4 - 2 + 1 = 3 = 0
    
    So a[i] is 0 mod 3 if i % 3 == 2, and 1 mod 3 otherwise.
    c0 = count of i in [1, n] where i % 3 == 2
    c1 = count of i in [1, n] where i % 3 == 0 or 1
    
    Triples sum to 0 mod 3 if:
    1. All three are 0 mod 3: nCr(c0, 3)
    2. All three are 1 mod 3: nCr(c1, 3)
    3. One of each (0, 1, 2 mod 3): c0 * c1 * c2 (but c2 is always 0)
    """
    c0 = (n + 1) // 3
    c1 = n - c0
    return nCr(c0, 3) + nCr(c1, 3)

@pytest.mark.parametrize("n, expected", [
    (1, 0),   # Too small for a triple
    (2, 0),   # Too small for a triple
    (3, 0),   # a = [1, 3, 7] -> mods [1, 0, 1]. Sums: 1+0+1=2. No triples.
    (4, 1),   # a = [1, 3, 7, 13] -> mods [1, 0, 1, 1]. Triple (1, 7, 13) sums to 21.
    (5, 1),   # Example case: a = [1, 3, 7, 13, 21] -> mods [1, 0, 1, 1, 0]. Triple (1, 7, 13).
    (6, 4),   # c0=2, c1=4 -> nCr(2,3) + nCr(4,3) = 0 + 4 = 4
    (7, 10),  # c0=2, c1=5 -> nCr(2,3) + nCr(5,3) = 0 + 10 = 10
    (8, 11),  # c0=3, c1=5 -> nCr(3,3) + nCr(5,3) = 1 + 10 = 11
    (9, 21),  # c0=3, c1=6 -> nCr(3,3) + nCr(6,3) = 1 + 20 = 21
    (10, 36), # c0=3, c1=7 -> nCr(3,3) + nCr(7,3) = 1 + 35 = 36
    (11, 39), # c0=4, c1=7 -> nCr(4,3) + nCr(7,3) = 4 + 35 = 39
])
def test_get_max_triples_various_n(n, expected):
    """Test the function with a variety of small to medium inputs."""
    from solution import get_max_triples
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """Test the function with a larger input to ensure efficiency and correctness."""
    from solution import get_max_triples
    n = 100
    # c0 = (100+1)//3 = 33
    # c1 = 100 - 33 = 67
    # expected = nCr(33, 3) + nCr(67, 3) = 5456 + 47905 = 53361
    expected = calculate_expected(n)
    assert get_max_triples(n) == expected

def test_get_max_triples_very_large_n():
    """Test the function with a very large input."""
    from solution import get_max_triples
    n = 10**6
    expected = calculate_expected(n)
    assert get_max_triples(n) == expected

def test_get_max_triples_minimum_positive():
    """Test the smallest possible positive integer input."""
    from solution import get_max_triples
    assert get_max_triples(1) == 0
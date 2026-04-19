
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

def test_get_max_triples_small_n():
    """Test cases where n is too small to form a triple or no triples sum to a multiple of 3."""
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0

@pytest.mark.parametrize("n, expected", [
    (4, 1),   # C0=1, C1=3 -> comb(1,3) + comb(3,3) = 0 + 1 = 1
    (5, 1),   # C0=2, C1=3 -> comb(2,3) + comb(3,3) = 0 + 1 = 1
    (6, 4),   # C0=2, C1=4 -> comb(2,3) + comb(4,3) = 0 + 4 = 4
    (7, 10),  # C0=2, C1=5 -> comb(2,3) + comb(5,3) = 0 + 10 = 10
    (8, 11),  # C0=3, C1=5 -> comb(3,3) + comb(5,3) = 1 + 10 = 11
    (9, 21),  # C0=3, C1=6 -> comb(3,3) + comb(6,3) = 1 + 20 = 21
    (10, 36), # C0=3, C1=7 -> comb(3,3) + comb(7,3) = 1 + 35 = 36
])
def test_get_max_triples_parametrized(n, expected):
    """Test a range of small to medium values of n."""
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """Test with larger values of n to ensure efficiency and correctness."""
    def nCr(n, r):
        if r > n: return 0
        if r < 0: return 0
        num = 1
        for i in range(r):
            num = num * (n - i) // (i + 1)
        return num

    def calculate_expected(n):
        c0 = (n + 1) // 3
        c1 = n - c0
        return nCr(c0, 3) + nCr(c1, 3)

    # Test n=100: C0=33, C1=67 -> 5456 + 47905 = 53361
    assert get_max_triples(100) == 53361
    # Test n=1000: C0=333, C1=667
    assert get_max_triples(1000) == calculate_expected(1000)

def test_get_max_triples_type_safety():
    """Ensure the function handles invalid input types by raising TypeError."""
    with pytest.raises(TypeError):
        get_max_triples("5")
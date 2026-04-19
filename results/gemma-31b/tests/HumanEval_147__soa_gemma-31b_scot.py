
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

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
    (7, 10),
    (8, 11),
    (9, 21),
    (10, 36),
    (11, 56),
    (12, 84),
    (15, 221), # c0 = 5, c1 = 10 -> comb(5, 3) + comb(10, 3) = 10 + 120 = 130. 
               # Wait, let's re-calc: n=15. i=2,5,8,11,14 are 0 mod 3. c0=5. c1=10. 
               # 10 + (10*9*8/6) = 10 + 120 = 130.
])
def test_get_max_triples_small_values(n, expected):
    """Test the function with small values of n to verify basic logic."""
    # Recalculating n=15: c0 = floor(16/3) = 5. c1 = 15 - 5 = 10.
    # comb(5, 3) = 10. comb(10, 3) = 120. Total = 130.
    # Let's adjust the parametrization for n=15.
    if n == 15:
        expected = 130
    assert get_max_triples(n) == expected

def test_get_max_triples_example():
    """Test the specific example provided in the problem description."""
    assert get_max_triples(5) == 1

def test_get_max_triples_large_n():
    """Test with a larger n to ensure efficiency and correctness."""
    # n = 100
    # c0 = floor(101/3) = 33
    # c1 = 100 - 33 = 67
    # comb(33, 3) = (33 * 32 * 31) / 6 = 11 * 16 * 31 = 5456
    # comb(67, 3) = (67 * 66 * 65) / 6 = 67 * 11 * 65 = 47905
    # Total = 5456 + 47905 = 53361
    assert get_max_triples(100) == 53361

def test_get_max_triples_minimum_n():
    """Test the minimum positive integer n."""
    assert get_max_triples(1) == 0

def test_get_max_triples_no_triples():
    """Test values of n where no triples can be formed (n < 3)."""
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_first_triple():
    """Test the smallest n that produces at least one triple."""
    # n=4: a=[1, 3, 7, 13], a%3=[1, 0, 1, 1]. Triple (1, 7, 13) sum=21.
    assert get_max_triples(4) == 1
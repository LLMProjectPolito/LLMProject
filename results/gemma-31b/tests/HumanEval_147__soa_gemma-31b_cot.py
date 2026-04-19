
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
])
def test_get_max_triples_small_values(n, expected):
    """
    Test the function with small values of n to verify correctness.
    The logic is based on the property that a[i] = i^2 - i + 1 mod 3:
    - If i % 3 == 2, a[i] % 3 == 0
    - If i % 3 == 0 or 1, a[i] % 3 == 1
    - a[i] % 3 is never 2.
    The sum of three numbers is a multiple of 3 if:
    - All three are 0 mod 3: combinations(C0, 3)
    - All three are 1 mod 3: combinations(C1, 3)
    Where C0 is the count of i in [1, n] such that i % 3 == 2,
    and C1 is the count of i in [1, n] such that i % 3 != 2.
    """
    assert get_max_triples(n) == expected

def test_get_max_triples_example():
    """Test the specific example provided in the problem description."""
    assert get_max_triples(5) == 1

def test_get_max_triples_large_n():
    """
    Test with a larger n to ensure the function handles larger combinations.
    For n = 100:
    C0 = (100 + 1) // 3 = 33
    C1 = 100 - 33 = 67
    Result = comb(33, 3) + comb(67, 3)
    comb(33, 3) = (33 * 32 * 31) / 6 = 5456
    comb(67, 3) = (67 * 66 * 65) / 6 = 47905
    Total = 5456 + 47905 = 53361
    """
    assert get_max_triples(100) == 53361

def test_get_max_triples_minimum_n():
    """Test the smallest possible positive integer n."""
    assert get_max_triples(1) == 0

def test_get_max_triples_boundary_combinations():
    """
    Test cases where C0 or C1 are exactly 3.
    C0 = 3 when (n+1)//3 = 3 => n=8 or n=9.
    C1 = 3 when n - (n+1)//3 = 3 => n=4 or n=5.
    """
    # n=4: C0=1, C1=3 -> comb(1,3)+comb(3,3) = 0 + 1 = 1
    assert get_max_triples(4) == 1
    # n=8: C0=3, C1=5 -> comb(3,3)+comb(5,3) = 1 + 10 = 11
    assert get_max_triples(8) == 11
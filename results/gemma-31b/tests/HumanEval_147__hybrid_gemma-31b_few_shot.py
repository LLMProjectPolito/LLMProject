
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

def get_max_triples(n: int) -> int:
    """
    Calculates the number of triples (a[i], a[j], a[k]) where i < j < k
    and a[i] + a[j] + a[k] is a multiple of 3, given a[i] = i*i - i + 1.
    
    Logic:
    a[i] % 3 follows the pattern: 1, 0, 1, 1, 0, 1, ...
    - Remainder 0 occurs when i % 3 == 2.
    - Remainder 1 occurs when i % 3 == 1 or 0.
    - Remainder 2 never occurs.
    
    A sum of three integers is divisible by 3 if:
    1. All three have the same remainder mod 3.
    2. All three have different remainders mod 3 (0, 1, 2).
    
    Since remainder 2 is impossible, we only count combinations of three 0s or three 1s.
    """
    if n < 3:
        return 0

    # Count elements with remainder 0 and 1
    c0 = n // 3
    c1 = n - c0

    def nCr_3(m):
        """Helper to calculate combinations of m choose 3."""
        if m < 3:
            return 0
        return m * (m - 1) * (m - 2) // 6

    return nCr_3(c0) + nCr_3(c1)

# --- Superior Pytest Suite ---

@pytest.mark.parametrize("n, expected", [
    # Edge cases: Not enough elements to form a triple
    (1, 0),
    (2, 0),
    # Small cases: Triples exist but may not sum to multiple of 3
    (3, 0),  # mods: [1, 0, 1] -> sum=2
    (4, 1),  # mods: [1, 0, 1, 1] -> (1,1,1) is 1 way
    (5, 1),  # mods: [1, 0, 1, 1, 0] -> (1,1,1) is 1 way
    # Moderate cases: Testing combinatorial growth
    (6, 4),  # c0=2, c1=4 -> 0 + 4 = 4
    (7, 10), # c0=2, c1=5 -> 0 + 10 = 10
    (8, 20), # c0=2, c1=6 -> 0 + 20 = 20
    (9, 21), # c0=3, c1=6 -> 1 + 20 = 21
    (10, 36),# c0=3, c1=7 -> 1 + 35 = 36
])
def test_get_max_triples_parametrized(n, expected):
    """Test a wide range of small to medium values to ensure logic correctness."""
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    """
    Verify efficiency and correctness for larger n.
    n = 100:
    c0 = 100 // 3 = 33
    c1 = 100 - 33 = 67
    nCr(33, 3) = (33 * 32 * 31) / 6 = 5456
    nCr(67, 3) = (67 * 66 * 65) / 6 = 47905
    Total = 53361
    """
    assert get_max_triples(100) == 53361

def test_get_max_triples_extreme_large():
    """Ensure the function handles very large n without timing out (O(1) complexity)."""
    # n = 10^6
    # c0 = 333,333; c1 = 666,667
    # This tests that we aren't using a loop to count remainders.
    result = get_max_triples(10**6)
    assert result > 0
    assert isinstance(result, int)
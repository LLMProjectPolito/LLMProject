
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

def brute_force_get_max_triples(n):
    """
    Reference implementation to verify the correctness of get_max_triples.
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def calculate_expected(n):
    """
    Mathematical formula for the number of triples.
    a[i] % 3 is 0 if i % 3 == 2, else 1.
    C0 = count of i in [1, n] where i % 3 == 2.
    C1 = count of i in [1, n] where i % 3 == 0 or 1.
    Triples are (0,0,0) or (1,1,1).
    """
    c0 = (n + 1) // 3
    c1 = n - c0
    
    def nCr(n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1
        if r > n // 2:
            r = n - r
        
        num = 1
        for i in range(r):
            num = num * (n - i) // (i + 1)
        return num

    return nCr(c0, 3) + nCr(c1, 3)

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
])
def test_small_values(n, expected):
    """Test small values of n where the result can be manually verified."""
    assert get_max_triples(n) == expected

def test_example_case():
    """Test the specific example provided in the problem description."""
    assert get_max_triples(5) == 1

def test_brute_force_comparison():
    """Compare the function output with a brute-force implementation for a range of n."""
    for n in range(1, 50):
        assert get_max_triples(n) == brute_force_get_max_triples(n), f"Failed for n={n}"

@pytest.mark.parametrize("n", [
    100, 
    1000, 
    10000, 
    100000
])
def test_large_values(n):
    """Test larger values of n using the mathematical formula to ensure efficiency and correctness."""
    assert get_max_triples(n) == calculate_expected(n)

def test_boundary_conditions():
    """Test minimum positive integer n."""
    assert get_max_triples(1) == 0

def test_performance():
    """Ensure the function handles very large n without timing out (O(1) or O(log n) expected)."""
    import time
    start_time = time.time()
    get_max_triples(10**12)
    end_time = time.time()
    # The function should be nearly instantaneous for large n if implemented mathematically
    assert end_time - start_time < 0.1

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
import time
from math import comb

# --- Implementation (Target of the tests) ---

def get_max_triples(n):
    """
    Implementation of the function to be tested.
    a[i] = i*i - i + 1
    a[i] % 3 pattern: [1, 0, 1, 1, 0, 1, 1, 0, ...]
    The only possible remainders are 0 and 1.
    A triple sums to a multiple of 3 if it is (0,0,0) or (1,1,1).
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    count0 = 0
    count1 = 0
    # The sequence a[i] % 3 only results in 0 or 1.
    # a[i] % 3 == 0 if i % 3 == 2
    # a[i] % 3 == 1 if i % 3 == 1 or i % 3 == 0
    for i in range(1, n + 1):
        if i % 3 == 2:
            count0 += 1
        else:
            count1 += 1
            
    def nCr(n_val, r):
        if r > n_val:
            return 0
        if r == 0 or r == n_val:
            return 1
        if r > n_val // 2:
            r = n_val - r
        
        numerator = 1
        for i in range(r):
            numerator = numerator * (n_val - i) // (i + 1)
        return numerator

    return nCr(count0, 3) + nCr(count1, 3)


# --- Test Suite ---

def calculate_expected_math(n):
    """
    Mathematical O(1) helper to calculate the expected value.
    Used to verify the correctness of the implementation for large N.
    """
    if n < 3:
        return 0
    # Count of i in [1, n] where i % 3 == 2
    c0 = (n + 1) // 3
    # Count of i in [1, n] where i % 3 != 2
    c1 = n - c0
    return comb(c0, 3) + comb(c1, 3)

@pytest.mark.parametrize("n, expected", [
    (1, 0),      # Minimum input
    (2, 0),      # Edge case: no triples possible
    (3, 0),      # Edge case: sum is not multiple of 3
    (4, 1),      # a mod 3 = [1, 0, 1, 1] -> (1,1,1)
    (5, 1),      # Example from problem description
    (6, 4),      # a mod 3 = [1, 0, 1, 1, 0, 1] -> comb(2,3) + comb(4,3) = 4
    (7, 10),     # a mod 3 = [1, 0, 1, 1, 0, 1, 1] -> comb(2,3) + comb(5,3) = 10
    (8, 11),     # a mod 3 = [1, 0, 1, 1, 0, 1, 1, 0] -> comb(3,3) + comb(5,3) = 11
    (9, 21),     # a mod 3 = [1, 0, 1, 1, 0, 1, 1, 0, 1] -> comb(3,3) + comb(6,3) = 21
    (10, 36),    # a mod 3 = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1] -> comb(3,3) + comb(7,3) = 36
])
def test_get_max_triples_standard_cases(n, expected):
    """Test small values of n including edge cases and known patterns."""
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n", [100, 1000, 10000])
def test_get_max_triples_large_values(n):
    """Test larger values of n to ensure mathematical correctness against O(1) logic."""
    assert get_max_triples(n) == calculate_expected_math(n)

def test_get_max_triples_very_large_n():
    """Test a very large n to ensure Python's arbitrary-precision integers handle the result."""
    n = 10**5
    expected = calculate_expected_math(n)
    assert get_max_triples(n) == expected

def test_get_max_triples_performance():
    """Ensure the O(n) implementation completes within a reasonable time frame."""
    start_time = time.time()
    result = get_max_triples(10**6)
    end_time = time.time()
    
    assert isinstance(result, int)
    assert (end_time - start_time) < 0.5  # Should easily pass under 500ms

def test_get_max_triples_invalid_inputs():
    """Test that the function raises appropriate errors for invalid input types and values."""
    with pytest.raises((ValueError, TypeError)):
        get_max_triples(0)
    with pytest.raises((ValueError, TypeError)):
        get_max_triples(-5)
    with pytest.raises(TypeError):
        get_max_triples("5")
    with pytest.raises(TypeError):
        get_max_triples(5.5)

def test_get_max_triples_consistency():
    """Verify that the function output is idempotent (consistent across multiple calls)."""
    n = 50
    first_call = get_max_triples(n)
    for _ in range(10):
        assert get_max_triples(n) == first_call
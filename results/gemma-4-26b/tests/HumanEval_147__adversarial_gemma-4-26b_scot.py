
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

def brute_force_get_max_triples(n):
    """
    A brute-force O(n^3) implementation used as a reference for testing.
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def test_example_case():
    """Verify the example provided in the problem description."""
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n", [1, 2, 3])
def test_edge_cases(n):
    """Test cases where n is too small to form any triple."""
    assert get_max_triples(n) == 0

@pytest.mark.parametrize("n", range(4, 31))
def test_small_n_brute_force(n):
    """Compare the function output against a brute-force implementation for small n."""
    assert get_max_triples(n) == brute_force_get_max_triples(n)

@pytest.mark.parametrize("n, expected", [
    (10, 36),   # c0=3 (i=2,5,8), c1=7 (i=1,3,4,6,7,9,10). comb(3,3)+comb(7,3) = 1 + 35 = 36
    (100, 53361) # c0=33, c1=67. comb(33,3)+comb(67,3) = 5456 + 47905 = 53361
])
def test_mathematical_consistency(n, expected):
    """Verify against manually calculated combinatorial results."""
    assert get_max_triples(n) == expected

def test_large_n_performance():
    """
    Test with a large n to ensure the implementation is not O(n^3).
    If the implementation is O(n^3), this will take a very long time.
    """
    # For n=1000, c0 = (1000+1)//3 = 333, c1 = 1000-333 = 667
    # Expected: comb(333, 3) + comb(667, 3)
    expected = math.comb(333, 3) + math.comb(667, 3)
    assert get_max_triples(1000) == expected

def test_input_type_integrity():
    """Ensure the function handles standard integer inputs correctly."""
    # This is a sanity check for basic integer behavior
    try:
        result = get_max_triples(10)
        assert isinstance(result, int)
    except Exception as e:
        pytest.fail(f"get_max_triples raised {type(e).__name__} unexpectedly!")
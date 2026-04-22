
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

# The function is assumed to be imported from the target module
# from solution import get_max_triples

def oracle_brute_force(n):
    """
    A slow but mathematically certain implementation used as a reference 
    to verify the correctness of the optimized function.
    """
    if n < 3:
        return 0
    a = [(i * i - i + 1) for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def test_example_case():
    """Tests the specific example provided in the problem description."""
    from solution import get_max_triples
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n", [1, 2])
def test_n_less_than_three(n):
    """Tests that n < 3 returns 0 as no triples can be formed."""
    from solution import get_max_triples
    assert get_max_triples(n) == 0

@pytest.mark.parametrize("n", [3, 4, 6, 10])
def test_small_n_values(n):
    """Tests small values of n against the brute force oracle."""
    from solution import get_max_triples
    assert get_max_triples(n) == oracle_brute_force(n)

@pytest.mark.parametrize("n", [7, 15, 25, 50])
def test_medium_n_values(n):
    """Tests medium values of n to ensure logic holds as the pattern scales."""
    from solution import get_max_triples
    assert get_max_triples(n) == oracle_brute_force(n)

def test_large_n_performance_and_logic():
    """
    Tests a larger n. 
    Since the brute force is O(n^3), we use a mathematical property 
    to verify a larger n to ensure the optimized solution is correct.
    Property: a[i] % 3 is 0 if i % 3 == 2, else 1.
    """
    from solution import get_max_triples
    n = 100
    
    # Calculate expected using the mathematical pattern
    # count0: number of i in [1, n] where i % 3 == 2
    # count1: number of i in [1, n] where i % 3 != 2
    count0 = (n + 1) // 3
    count1 = n - count0
    
    # Combinations: C(count0, 3) + C(count1, 3)
    def combinations_3(m):
        if m < 3:
            return 0
        return (m * (m - 1) * (m - 2)) // 6

    expected = combinations_3(count0) + combinations_3(count1)
    assert get_max_triples(n) == expected

def test_invalid_input_types():
    """
    Tests how the function handles non-integer or non-positive inputs.
    Note: Depending on requirements, this might expect an exception or 0.
    """
    from solution import get_max_triples
    with pytest.raises((TypeError, ValueError)):
        get_max_triples("5")
    with pytest.raises((ValueError, AssertionError)):
        # Assuming the function requires positive integers
        get_max_triples(-1)
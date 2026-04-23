
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

# STEP 1: REASONING
# The problem asks for the number of triples (a[i], a[j], a[k]) such that i < j < k 
# and (a[i] + a[j] + a[k]) % 3 == 0, where a[i] = i*i - i + 1.
#
# Let's analyze a[i] modulo 3:
# i % 3 == 1: a[i] = 1^2 - 1 + 1 = 1 (mod 3)
# i % 3 == 2: a[i] = 2^2 - 2 + 1 = 3 = 0 (mod 3)
# i % 3 == 0: a[i] = 0^2 - 0 + 1 = 1 (mod 3)
#
# The values in the array modulo 3 can only be 0 or 1.
# For the sum of three numbers to be a multiple of 3, the possible combinations of (mod 3) values are:
# 1. (0, 0, 0) -> 0 + 0 + 0 = 0 (mod 3)
# 2. (1, 1, 1) -> 1 + 1 + 1 = 3 = 0 (mod 3)
# Note: (0, 1, 2) is impossible because no element is 2 (mod 3).
#
# Therefore, the total count is:
# Combinations(count_of_0s, 3) + Combinations(count_of_1s, 3)
#
# count_of_0s: number of i in [1, n] where i % 3 == 2.
# count_of_1s: number of i in [1, n] where i % 3 == 1 or i % 3 == 0.

# STEP 2: PLAN
# 1. test_get_max_triples_edge_cases: Test n < 3 where no triples can exist.
# 2. test_get_max_triples_minimal_n: Test n = 3 where no valid triples exist.
# 3. test_get_max_triples_example: Test the provided example n = 5.
# 4. test_get_max_triples_standard: Test small values of n (6, 10) with known results.
# 5. test_get_max_triples_large: Test a larger value of n (100) to ensure scalability and correctness.

# STEP 3: CODE

@pytest.mark.parametrize("n, expected", [
    (1, 0),  # Only one element, no triples
    (2, 0),  # Only two elements, no triples
    (3, 0),  # a % 3 = [1, 0, 1]. Sums: 1+0+1=2. No triples.
    (4, 1),  # a % 3 = [1, 0, 1, 1]. Triple (1, 1, 1) exists.
    (5, 1),  # Example case: a % 3 = [1, 0, 1, 1, 0]. Triple (1, 1, 1) exists.
    (6, 4),  # a % 3 = [1, 0, 1, 1, 0, 1]. C0=2, C1=4. Comb(2,3)+Comb(4,3) = 0 + 4 = 4.
    (10, 36), # C0=3 (i=2,5,8), C1=7. Comb(3,3)+Comb(7,3) = 1 + 35 = 36.
    (100, 53361), # C0=33, C1=67. Comb(33,3)+Comb(67,3) = 5456 + 47905 = 53361.
])
def test_get_max_triples_scenarios(n, expected):
    """
    Tests various scenarios including edge cases, the example case, 
    and larger values to verify the mathematical logic.
    """
    assert get_max_triples(n) == expected

def test_get_max_triples_type_safety():
    """
    Ensures the function handles the input type correctly (basic sanity check).
    """
    # This is a sanity check to ensure the function doesn't crash on valid positive integers.
    try:
        get_max_triples(1)
    except Exception as e:
        pytest.fail(f"get_max_triples raised {type(e).__name__} unexpectedly!")

def test_get_max_triples_monotonicity():
    """
    The number of triples should be non-decreasing as n increases.
    """
    results = []
    for n in range(1, 20):
        results.append(get_max_triples(n))
    
    for i in range(len(results) - 1):
        assert results[i] <= results[i+1], f"Result decreased at n={i+2}"
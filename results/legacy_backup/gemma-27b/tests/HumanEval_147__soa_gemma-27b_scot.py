import pytest

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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function calculates the number of triples (a[i], a[j], a[k]) in an array 'a'
# where i < j < k and the sum a[i] + a[j] + a[k] is divisible by 3.
# The array 'a' is generated based on the input 'n' using the formula a[i] = i*i - i + 1.
# Constraints: n is a positive integer.

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Basic test case with n = 5 (example from the problem description)
# 2. Test case with n = 1 (no triples possible)
# 3. Test case with n = 2 (no triples possible)
# 4. Test case with n = 3 (small case to verify logic)
# 5. Test case with n = 4 (small case to verify logic)
# 6. Test case with n = 6 (larger case)
# 7. Test case with n = 7 (larger case)
# 8. Test case with n = 8 (larger case)
# 9. Edge case: n = 0 (should return 0, although problem states n is positive)
# 10. Test case to check for large n (performance)

# STEP 3: CODE - Write the high-quality pytest suite.
@pytest.mark.parametrize("n, expected", [
    (5, 1),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (6, 20),
    (7, 35),
    (8, 56),
    (0, 0),
    (10, 120)
])
def test_get_max_triples(n, expected):
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n", [15, 20])
def test_get_max_triples_large_n(n):
    result = get_max_triples(n)
    assert isinstance(result, int)
    assert result >= 0
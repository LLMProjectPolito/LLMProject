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

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Basic test case (n = 5)
# 2. Small test case (n = 1, n = 2, n = 3)
# 3. Larger test case (n = 10, n = 20)
# 4. Edge case (n = 0) - should return 0
# 5. Test cases where the result is 0
# 6. Test cases with different remainders when divided by 3

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
    (9, 84),
    (10, 120),
    (20, 1330),
    (0, 0),
    (11, 165),
    (12, 220)
])
def test_get_max_triples(n, expected):
    assert get_max_triples(n) == expected

def test_get_max_triples_large_n():
    assert get_max_triples(30) == 4060

def test_get_max_triples_zero_n():
    assert get_max_triples(0) == 0
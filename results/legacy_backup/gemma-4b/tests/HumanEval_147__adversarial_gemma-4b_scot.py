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

### SCoT Steps:

# STEP 1: REASONING
# The function `get_max_triples(n)` calculates the number of triples (i, j, k) in an array `a` of length `n` such that `i < j < k` and `a[i] + a[j] + a[k]` is divisible by 3.
# The array `a` is generated as `a[i] = i * i - i + 1`.
# We need to test various scenarios including edge cases like n = 1, n = 2, n = 3, and n = 4.
# We also need to consider cases where the sum of the elements is divisible by 3, and cases where it is not.
# The core logic is to iterate through all possible triples (i, j, k) where i < j < k and check if their sum is divisible by 3.

# STEP 2: PLAN
# Test cases:
# 1. n = 1: Should return 0 (no triples possible)
# 2. n = 2: Should return 0 (no triples possible)
# 3. n = 3: Should return 0 (no triples possible)
# 4. n = 4: Should return 1 (a = [1, 3, 7, 13], (1, 3, 7) sum is 11, not divisible by 3. (1,3,13) sum is 17, not divisible by 3. (1,7,13) sum is 21, divisible by 3. (3,7,13) sum is 23, not divisible by 3. )
# 5. n = 5: Should return 1 (a = [1, 3, 7, 13, 21], (1, 7, 13) sum is 21, divisible by 3)
# 6. n = 6: Should return 4 (a = [1, 3, 7, 13, 21, 31], several triples sum to a multiple of 3)

# Test functions:
# test_n_1
# test_n_2
# test_n_3
# test_n_4
# test_n_5
# test_n_6

# STEP 3: CODE
###
def test_n_1():
    assert get_max_triples(1) == 0

def test_n_2():
    assert get_max_triples(2) == 0

def test_n_3():
    assert get_max_triples(3) == 0

def test_n_4():
    assert get_max_triples(4) == 1

def test_n_5():
    assert get_max_triples(5) == 1

def test_n_6():
    assert get_max_triples(6) == 4
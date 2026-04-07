
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
# We need to test different values of `n` and verify that the returned count is correct.
# We should consider edge cases like n = 1, n = 2, and n = 3.
# We should also consider larger values of n to ensure the code is efficient.

# STEP 2: PLAN
# Test cases:
# - n = 1: Should return 0
# - n = 2: Should return 0
# - n = 3: Should return 0
# - n = 4: Should return 0
# - n = 5: Should return 1
# - n = 6: Should return 2
# - n = 7: Should return 3
# - n = 8: Should return 4

# Test functions:
# - test_n_1()
# - test_n_2()
# - test_n_3()
# - test_n_4()
# - test_n_5()
# - test_n_6()
# - test_n_7()
# - test_n_8()

# STEP 3: CODE
def test_n_1():
    assert get_max_triples(1) == 0

def test_n_2():
    assert get_max_triples(2) == 0

def test_n_3():
    assert get_max_triples(3) == 0

def test_n_4():
    assert get_max_triples(4) == 0

def test_n_5():
    assert get_max_triples(5) == 1

def test_n_6():
    assert get_max_triples(6) == 2

def test_n_7():
    assert get_max_triples(7) == 3

def test_n_8():
    assert get_max_triples(8) == 4
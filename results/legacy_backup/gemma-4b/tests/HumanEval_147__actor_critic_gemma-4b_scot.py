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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `get_max_triples(n)` calculates the number of triples (i, j, k)
# in an array `a` of length `n` such that `a[i] + a[j] + a[k]` is divisible by 3,
# with the constraint that `i < j < k`. The array `a` is generated as `a[i] = i*i - i + 1`.
# We need to test various input values of `n` and ensure the function returns the correct count.
# Edge cases include n = 1, n = 2, n = 3, and n = 4.  Also, we should consider cases where
# the elements of the array are all multiples of 3, or none are.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_array: Test with n = 0 (should return 0).
# test_n_equals_1: Test with n = 1 (should return 0).
# test_n_equals_2: Test with n = 2 (should return 0).
# test_n_equals_3: Test with n = 3 (should return 0).
# test_n_equals_4: Test with n = 4 (should return 1).
# test_n_equals_5: Test with n = 5 (should return 1).
# test_n_equals_6: Test with n = 6 (should return 4).
# test_n_equals_7: Test with n = 7 (should return 6).
# test_n_equals_8: Test with n = 8 (should return 10).
# test_n_equals_9: Test with n = 9 (should return 18).
# test_n_equals_10: Test with n = 10 (should return 31).

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_array():
    assert get_max_triples(0) == 0

def test_n_equals_1():
    assert get_max_triples(1) == 0

def test_n_equals_2():
    assert get_max_triples(2) == 0

def test_n_equals_3():
    assert get_max_triples(3) == 0

def test_n_equals_4():
    assert get_max_triples(4) == 1

def test_n_equals_5():
    assert get_max_triples(5) == 1

def test_n_equals_6():
    assert get_max_triples(6) == 4

def test_n_equals_7():
    assert get_max_triples(7) == 6

def test_n_equals_8():
    assert get_max_triples(8) == 10

def test_n_equals_9():
    assert get_max_triples(9) == 18

def test_n_equals_10():
    assert get_max_triples(10) == 31
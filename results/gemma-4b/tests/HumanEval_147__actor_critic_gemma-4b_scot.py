
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `get_max_triples(n)` calculates the number of triples (i, j, k)
# in an array `a` of length `n` such that `a[i] + a[j] + a[k]` is divisible by 3,
# with the constraint that `i < j < k`. The array `a` is generated as `a[i] = i*i - i + 1`.
# We need to test various input values of `n`, including edge cases like n = 0, n = 1,
# and n = 2, and also test cases where the generated array `a` has elements that
# are multiples of 3, and cases where they are not.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_array: Test with n = 0.
# test_single_element_array: Test with n = 1.
# test_two_element_array: Test with n = 2.
# test_small_array: Test with n = 5 (example from the prompt).
# test_large_array: Test with n = 10.
# test_all_multiples_of_3: Test with n such that all elements of a are multiples of 3.
# test_no_triples: Test with n such that no triples sum to a multiple of 3.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_array():
    assert get_max_triples(0) == 0

def test_single_element_array():
    assert get_max_triples(1) == 0

def test_two_element_array():
    assert get_max_triples(2) == 0

def test_small_array():
    assert get_max_triples(5) == 1

def test_large_array():
    assert get_max_triples(10) == 10

def test_all_multiples_of_3():
    n = 3
    a = [1, 3, 7]
    assert get_max_triples(n) == 0

def test_no_triples():
    n = 4
    a = [1, 2, 4, 7]
    assert get_max_triples(n) == 0

def test_n_equals_6():
    assert get_max_triples(6) == 6

def test_n_equals_7():
    assert get_max_triples(7) == 10
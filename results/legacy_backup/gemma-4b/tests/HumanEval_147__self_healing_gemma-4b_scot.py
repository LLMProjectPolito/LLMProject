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
    a = [i*i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

### SCoT Steps:
# STEP 1: REASONING - The function calculates the number of triples (i, j, k) such that i < j < k and a[i] + a[j] + a[k] is divisible by 3, where a[i] = i*i - i + 1.
# We need to test various input values of n and verify that the function returns the correct count of triples.
# We should consider edge cases like n = 1, n = 2, and n = 3.
# We should also consider cases where the number of triples is 0 or a larger number.

# STEP 2: PLAN -
# test_get_max_triples_n1: Test with n = 1.
# test_get_max_triples_n2: Test with n = 2.
# test_get_max_triples_n3: Test with n = 3.
# test_get_max_triples_n4: Test with n = 4.
# test_get_max_triples_n5: Test with n = 5.
# test_get_max_triples_n6: Test with n = 6.

# STEP 3: CODE -
def test_get_max_triples_n1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n4():
    assert get_max_triples(4) == 0

def test_get_max_triples_n5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n6():
    assert get_max_triples(6) == 2
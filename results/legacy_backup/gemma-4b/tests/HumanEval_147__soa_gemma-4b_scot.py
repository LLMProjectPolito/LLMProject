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
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `get_max_triples(n)` calculates the number of triples (i, j, k) in an array `a` of length `n` such that `i < j < k` and `a[i] + a[j] + a[k]` is divisible by 3.
### The array `a` is generated as `a[i] = i*i - i + 1`.
### The test suite should cover various cases, including small values of `n`, cases where the number of triples is 0, and cases where the number of triples is greater than 0.
### We need to test the array generation and the triple counting logic.

### STEP 2: PLAN - List test functions names and scenarios.
### test_empty_array
### test_n_equals_1
### test_n_equals_2
### test_n_equals_3
### test_n_equals_4
### test_n_equals_5
### test_n_equals_6
### test_n_equals_7

### STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_array():
    assert get_max_triples(0) == 0

def test_n_equals_1():
    assert get_max_triples(1) == 0

def test_n_equals_2():
    assert get_max_triples(2) == 0

def test_n_equals_3():
    assert get_max_triples(3) == 0

def test_n_equals_4():
    assert get_max_triples(4) == 0

def test_n_equals_5():
    assert get_max_triples(5) == 1

def test_n_equals_6():
    assert get_max_triples(6) == 2

def test_n_equals_7():
    assert get_max_triples(7) == 4
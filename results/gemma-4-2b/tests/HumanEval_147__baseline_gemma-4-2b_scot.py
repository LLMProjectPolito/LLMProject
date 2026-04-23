
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

# STEP 1: REASONING
# The function `get_max_triples(n)` calculates the number of triples (a[i], a[j], a[k])
# where i < j < k and a[i] + a[j] + a[k] is a multiple of 3.
# The values of a[i] are i*i - i + 1.
# We need to analyze the values of a[i] modulo 3 to determine the possible combinations
# that sum to a multiple of 3.
# The values of a[i] can be categorized as follows:
# - a[i] % 3 = 1 if i % 3 = 1
# - a[i] % 3 = 2 if i % 3 = 2
# - a[i] % 3 = 0 if i % 3 = 0
# The sum of three numbers is a multiple of 3 if:
# 1. All three numbers are divisible by 3 (0 + 0 + 0)
# 2. All three numbers have remainder 1 when divided by 3 (1 + 1 + 1)
# 3. All three numbers have remainder 2 when divided by 3 (2 + 2 + 2)
# 4. One number has remainder 0, one has remainder 1, and one has remainder 2 (0 + 1 + 2)
# We need to count the number of triples that satisfy these conditions.

# STEP 2: PLAN
# Test cases:
# 1. n = 1: Should return 0
# 2. n = 2: Should return 0
# 3. n = 3: Should return 1
# 4. n = 4: Should return 1
# 5. n = 5: Should return 1
# 6. n = 6: Should return 2
# 7. n = 7: Should return 2
# 8. n = 8: Should return 2
# 9. n = 9: Should return 3
# 10. n = 10: Should return 3

# STEP 3: CODE
import pytest

def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.
    """
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def test_get_max_triples_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_3():
    assert get_max_triples(3) == 1

def test_get_max_triples_4():
    assert get_max_triples(4) == 1

def test_get_max_triples_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_6():
    assert get_max_triples(6) == 2

def test_get_max_triples_7():
    assert get_max_triples(7) == 2

def test_get_max_triples_8():
    assert get_max_triples(8) == 2

def test_get_max_triples_9():
    assert get_max_triples(9) == 3

def test_get_max_triples_10():
    assert get_max_triples(10) == 3
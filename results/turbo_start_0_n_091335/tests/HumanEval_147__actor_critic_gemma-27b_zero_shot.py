import pytest
import time

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

def test_n_equals_zero():
    assert get_max_triples(0) == 0

def test_small_n():
    assert get_max_triples(4) == 0

def test_example():
    assert get_max_triples(5) == 1

def test_larger_n():
    assert get_max_triples(6) == 20
    assert get_max_triples(7) == 35
    assert get_max_triples(8) == 56
    assert get_max_triples(9) == 84
    assert get_max_triples(10) == 120

def test_pattern_verification():
    assert get_max_triples(11) == 165
    assert get_max_triples(12) == 220
    assert get_max_triples(13) == 286
    assert get_max_triples(14) == 364
    assert get_max_triples(15) == 455

def test_large_n():
    assert get_max_triples(20) == 1140
    assert get_max_triples(50) == 19600

def test_same_remainder():
    n = 10
    a = [i * i - i + 1 for i in range(1, n + 1)]
    remainder_counts = {}
    for x in a:
        remainder = x % 3
        remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1
    
    if 0 in remainder_counts and 1 in remainder_counts and 2 in remainder_counts:
        assert get_max_triples(n) > 0
    else:
        assert get_max_triples(n) == 0

@pytest.mark.parametrize("n", [100, 200])
def test_very_large_n(n):
    # This test is primarily to check for performance issues (execution time) or integer overflows when calculating the sum of triples.
    # The expected values are pre-calculated.
    start_time = time.time()
    result = get_max_triples(n)
    end_time = time.time()
    execution_time = end_time - start_time

    if n == 100:
        assert result == 161700
    elif n == 200:
        assert result == 1313400
    
    # Add a performance check.  Adjust the threshold as needed.
    assert execution_time < 5, f"Execution time for n={n} is {execution_time} seconds, which exceeds the threshold."
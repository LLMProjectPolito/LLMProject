
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
import time

def get_max_triples(n):
    """
    Placeholder for the actual implementation.
    The user should replace this with their actual function.
    """
    pass

@pytest.mark.parametrize("n, expected", [
    (0, 0),        # n=0: No elements
    (1, 0),        # n=1: No triples possible
    (2, 0),        # n=2: No triples possible
    (3, 0),        # n=3: a=[1, 3, 7], a%3=[1, 0, 1], 0s:1, 1s:2 -> 1C3 + 2C3 = 0
    (4, 1),        # n=4: a%3=[1, 0, 1, 1], 0s:1, 1s:3 -> 1C3 + 3C3 = 1
    (5, 1),        # n=5: a%3=[1, 0, 1, 1, 0], 0s:2, 1s:3 -> 2C3 + 3C3 = 1
    (6, 4),        # n=6: a%3=[1, 0, 1, 1, 0, 1], 0s:2, 1s:4 -> 2C3 + 4C3 = 4
    (8, 11),       # n=8: a%3=[1, 0, 1, 1, 0, 1, 1, 0], 0s:3, 1s:5 -> 3C3 + 5C3 = 11
    (10, 36),      # n=10: a%3=[1, 0, 1, 1, 0, 1, 1, 0, 1, 1], 0s:3, 1s:7 -> 1 + 35 = 36
    (15, 130),     # n=15: a%3: 0s:5, 1s:10 -> 5C3 + 10C3 = 10 + 120 = 130
    (20, 321),     # n=20: a%3: 0s:7, 1s:13 -> 7C3 + 13C3 = 35 + 286 = 321
])
def test_get_max_triples_logic(n, expected):
    """
    Tests the core logic of the function across various values of n,
    including edge cases and small values.
    """
    assert get_max_triples(n) == expected

def test_get_max_triples_large_input():
    """
    Tests the function with a large input to ensure:
    1. Correctness of the result (handling large combinatorial values).
    2. Efficiency (O(1) or O(log n) complexity) via timing.
    """
    n = 1000000
    # Mathematical derivation for n = 1,000,000:
    # a[i] = i^2 - i + 1
    # a[i] % 3 is 0 if i % 3 == 2, and 1 otherwise (since i % 3 is 0 or 1).
    #
    # For n = 1,000,000:
    # Count of i in [1, n] where i % 3 == 2: 333,333
    # Count of i in [1, n] where i % 3 != 2: 666,667
    # Total triples = (333,333 choose 3) + (666,667 choose 3)
    # Result = 6172781481481485 + 49382814814814850 = 55555596296296335
    expected = 55555596296296335
    
    start_time = time.perf_counter()
    result = get_max_triples(n)
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    
    assert result == expected, f"Expected {expected}, but got {result}"
    
    # A threshold of 0.01s is used to ensure the implementation is not O(n) or O(n^2).
    # An O(n) implementation for n=1,000,000 would likely exceed this threshold.
    assert duration < 0.01, f"Efficiency test failed: execution took {duration:.6f}s"
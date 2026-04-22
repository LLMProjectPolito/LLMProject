
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

def test_get_max_triples_example():
    """
    Tests the specific example provided in the problem description.
    For n=5, a = [1, 3, 7, 13, 21], a mod 3 = [1, 0, 1, 1, 0].
    The only triple summing to a multiple of 3 is (1, 7, 13) -> (1, 1, 1) mod 3.
    """
    assert get_max_triples(5) == 1

def test_get_max_triples_small_n():
    """Tests cases where n is too small to form any triple (n < 3) or n=0."""
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_boundary_n3():
    """
    Tests n=3, the minimum size for a triple.
    For n=3, a = [1, 3, 7], so a mod 3 = [1, 0, 1].
    No combination of three elements sums to a multiple of 3.
    """
    assert get_max_triples(3) == 0

@pytest.mark.parametrize("n, expected", [
    (4, 1),   # a mod 3: [1, 0, 1, 1] -> comb(1,3) + comb(3,3) = 0 + 1 = 1
    (6, 4),   # a mod 3: [1, 0, 1, 1, 0, 1] -> comb(2,3) + comb(4,3) = 0 + 4 = 4
    (7, 10),  # a mod 3: [1, 0, 1, 1, 0, 1, 1] -> comb(2,3) + comb(5,3) = 0 + 10 = 10
    (8, 11),  # a mod 3: [1, 0, 1, 1, 0, 1, 1, 0] -> comb(3,3) + comb(5,3) = 1 + 10 = 11
])
def test_get_max_triples_various_n(n, expected):
    """Tests various values of n to ensure mathematical correctness for the sequence a[i]."""
    assert get_max_triples(n) == expected

def test_get_max_triples_n10():
    """
    Tests n=10 to verify the specific sequence logic.
    The sequence a[i] mod 3 follows the pattern: 1, 0, 1, 1, 0, 1, 1, 0, 1, 1...
    For n=10:
    - Count of 0s (where i % 3 == 2): 3 (i=2, 5, 8)
    - Count of 1s (where i % 3 != 2): 7 (i=1, 3, 4, 6, 7, 9, 10)
    - Total triples: comb(3, 3) + comb(7, 3) = 1 + 35 = 36
    """
    assert get_max_triples(10) == 36

def test_get_max_triples_large_n():
    """
    Tests a large n to ensure the algorithm handles growth and avoids integer overflow.
    For n=1000:
    - The sequence a[i] mod 3 repeats (1, 0, 1) every 3 elements.
    - Count of 0s: 1000 // 3 = 333
    - Count of 1s: 1000 - 333 = 667
    - Total triples: comb(333, 3) + comb(667, 3)
    - comb(333, 3) = (333 * 332 * 331) / 6 = 6,101,546
    - comb(667, 3) = (667 * 666 * 665) / 6 = 49,234,105
    - Expected = 55,335,651
    """
    assert get_max_triples(1000) == 55335651
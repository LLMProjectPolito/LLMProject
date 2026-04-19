
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

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
    (7, 10),
    (8, 11),
    (9, 21),
    (10, 36),
    (11, 39),
    (12, 60),
    (13, 88),
    (14, 94),
    (15, 130),
    (16, 175),
    (17, 185),
    (18, 240),
    (19, 306),
    (20, 321),
])
def test_get_max_triples_small_to_medium(n, expected):
    """Test the function with a range of small to medium values of n."""
    assert get_max_triples(n) == expected

def test_get_max_triples_example():
    """Test the specific example provided in the docstring."""
    assert get_max_triples(5) == 1

def test_get_max_triples_large_n():
    """Test the function with larger values of n to ensure efficiency and correctness."""
    # For n = 100:
    # c0 (i % 3 == 2) = 33 (2, 5, ..., 98)
    # c1 (i % 3 != 2) = 67
    # Combinations: comb(33, 3) + comb(67, 3) = 5456 + 47905 = 53361
    assert get_max_triples(100) == 53361

    # For n = 1000:
    # c0 (i % 3 == 2) = 333 (2, 5, ..., 998)
    # c1 (i % 3 != 2) = 667
    # Combinations: comb(333, 3) + comb(667, 3) = 6099066 + 49234705 = 55333771
    assert get_max_triples(1000) == 55333771

def test_get_max_triples_minimum_n():
    """Test the absolute minimum positive integer n."""
    assert get_max_triples(1) == 0

def test_get_max_triples_below_triple_threshold():
    """Test n values where it is impossible to form a triple."""
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
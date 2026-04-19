
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

def test_get_max_triples_small_n():
    """Test cases where n is too small to form a triple or no triples sum to a multiple of 3."""
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0

def test_get_max_triples_example():
    """Test the example provided in the docstring."""
    # n = 5, a = [1, 3, 7, 13, 21]
    # Mod 3: [1, 0, 1, 1, 0]
    # Triples summing to 0 mod 3: (1, 1, 1) -> (1, 7, 13)
    assert get_max_triples(5) == 1

def test_get_max_triples_n_4():
    """Test n = 4."""
    # n = 4, a = [1, 3, 7, 13]
    # Mod 3: [1, 0, 1, 1]
    # Triple: (1, 1, 1) -> (1, 7, 13)
    assert get_max_triples(4) == 1

def test_get_max_triples_n_6():
    """Test n = 6."""
    # n = 6, a = [1, 3, 7, 13, 21, 31]
    # Mod 3: [1, 0, 1, 1, 0, 1]
    # c0 = 2, c1 = 4
    # Combinations: comb(2, 3) + comb(4, 3) = 0 + 4 = 4
    assert get_max_triples(6) == 4

def test_get_max_triples_n_8():
    """Test n = 8."""
    # n = 8
    # c0 = floor((8+1)/3) = 3
    # c1 = 8 - 3 = 5
    # Combinations: comb(3, 3) + comb(5, 3) = 1 + 10 = 11
    assert get_max_triples(8) == 11

def test_get_max_triples_large_n():
    """Test a larger value of n to ensure mathematical correctness."""
    # n = 100
    # c0 = floor(101/3) = 33
    # c1 = 100 - 33 = 67
    # comb(33, 3) = (33 * 32 * 31) / 6 = 5456
    # comb(67, 3) = (67 * 66 * 65) / 6 = 47905
    # Total = 53361
    assert get_max_triples(100) == 53361

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
    (7, 4),
    (8, 11),
    (9, 11),
    (10, 20),
])
def test_get_max_triples_parametrized(n, expected):
    """Parametrized tests for various small values of n."""
    assert get_max_triples(n) == expected
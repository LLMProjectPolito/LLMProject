
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
    (7, 4),
    (8, 11),
    (9, 11),
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
def test_get_max_triples(n, expected):
    """
    Test get_max_triples with various values of n.
    The logic is based on the property that a[i] = i^2 - i + 1 mod 3 is:
    - 0 if i % 3 == 2
    - 1 otherwise
    The number of triples is combinations(count_0, 3) + combinations(count_1, 3).
    """
    assert get_max_triples(n) == expected

def test_get_max_triples_example():
    """Test the specific example provided in the problem description."""
    assert get_max_triples(5) == 1

def test_get_max_triples_large_n():
    """
    Test with a larger n to ensure the logic holds.
    For n = 100:
    c0 = floor((100 + 1) / 3) = 33
    c1 = 100 - 33 = 67
    Triples = comb(33, 3) + comb(67, 3)
    comb(33, 3) = (33 * 32 * 31) / 6 = 11 * 16 * 31 = 5456
    comb(67, 3) = (67 * 66 * 65) / 6 = 67 * 11 * 65 = 47905
    Total = 5456 + 47905 = 53361
    """
    assert get_max_triples(100) == 53361

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
    if n < 3:
        return 0

    a = [(i * i - i + 1) for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def calculate_a(n):
    """Calculates the array 'a' used in get_max_triples."""
    return [(i * i - i + 1) for i in range(1, n + 1)]


@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 4),
    (9, 6),
    (10, 8),
    (20, 135)
])
def test_get_max_triples(n, expected):
    """Tests get_max_triples with various inputs."""
    assert get_max_triples(n) == expected


def test_get_max_triples_zero():
    """Tests a case where the answer is 0."""
    assert get_max_triples(3) == 0

def test_get_max_triples_larger_number():
    """Tests a case where the answer is a larger number."""
    assert get_max_triples(10) == 8

def test_get_max_triples_with_precalculated_array():
    """Tests get_max_triples with a precalculated array."""
    a = calculate_a(5)
    # Manually calculate the expected value for n=5
    expected = 1
    assert get_max_triples(5) == expected
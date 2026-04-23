
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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
    ],
)
def test_n_small(n, expected):
    assert get_max_triples(n) == expected

def test_n_equals_five():
    assert get_max_triples(5) == 1

def test_n_equals_six_remainder():
    assert get_max_triples(6) == 7

def test_n_equals_seven():
    assert get_max_triples(7) == 15

def test_n_equals_eight():
    assert get_max_triples(8) == 26

def test_n_equals_ten():
    assert get_max_triples(10) == 55

def test_n_equals_200():
    assert get_max_triples(200) == 13466700

def test_n_equals_100():
    assert get_max_triples(100) == 16170000

def test_n_equals_500():
    assert get_max_triples(500) == 20416667000

def test_invalid_input_negative():
    assert get_max_triples(-1) == 0

def test_invalid_input_non_integer():
    assert get_max_triples(3.14) == 0
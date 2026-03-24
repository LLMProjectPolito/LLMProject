
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

def test_invalid_input():
    with pytest.raises(TypeError):
        get_max_triples(3.14)
    with pytest.raises(ValueError):
        get_max_triples(-1)

def test_n_less_than_three():
    assert get_max_triples(0) == 0
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_n_equals_five():
    assert get_max_triples(5) == 10

def test_n_equals_six():
    assert get_max_triples(6) == 20

def test_n_equals_seven():
    assert get_max_triples(7) == 35

def test_n_equals_eight():
    assert get_max_triples(8) == 56

def test_n_equals_ten():
    assert get_max_triples(10) == 120

def test_n_equals_two_hundred():
    assert get_max_triples(200) == 1313400

def test_n_equals_nine():
    assert get_max_triples(9) == 84

def test_n_equals_one_thousand():
    assert get_max_triples(1000) == 166167000

def test_n_equals_two_thousand():
    assert get_max_triples(2000) == 1331334000
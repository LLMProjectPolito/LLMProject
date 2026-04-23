
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


def test_get_max_triples_n_less_than_3():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0

def test_get_max_triples_n_equals_3():
    a = [1, 3, 7]
    assert get_max_triples(3) == 0

def test_get_max_triples_n_equals_4():
    a = [1, 3, 7, 13]
    assert get_max_triples(4) == 0

def test_get_max_triples_n_equals_5():
    a = [1, 3, 7, 13, 21]
    assert get_max_triples(5) == 1

def test_get_max_triples_n_equals_10():
    a = [1, 3, 7, 13, 21, 31, 43, 57, 73, 91]
    assert get_max_triples(10) == 5

def test_get_max_triples_n_equals_20():
    a = [(i * i - i + 1) for i in range(1, 21)]
    assert get_max_triples(20) == 125

def test_get_max_triples_no_triples_sum_to_multiple_of_3():
    a = [1, 2, 4, 5, 7, 8, 10, 11]
    assert get_max_triples(len(a)) == 0

def test_get_max_triples_many_triples_sum_to_multiple_of_3():
    a = [1, 4, 7, 2, 5, 8, 3, 6, 9]
    assert get_max_triples(len(a)) == 84

def test_get_max_triples_negative_input():
    with pytest.raises(TypeError):  # Or ValueError, depending on desired behavior
        get_max_triples(-1)

def test_get_max_triples_zero_input():
    with pytest.raises(TypeError):  # Or ValueError, depending on desired behavior
        get_max_triples(0)
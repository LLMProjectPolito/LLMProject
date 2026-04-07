
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_n1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n4():
    assert get_max_triples(4) == 0

def test_get_max_triples_n6():
    assert get_max_triples(6) == 20

def test_get_max_triples_n7():
    assert get_max_triples(7) == 35

def test_get_max_triples_n8():
    assert get_max_triples(8) == 56

def test_get_max_triples_n9():
    assert get_max_triples(9) == 84

def test_get_max_triples_n10():
    assert get_max_triples(10) == 120

def test_get_max_triples_n11():
    assert get_max_triples(11) == 165

def test_get_max_triples_n12():
    assert get_max_triples(12) == 220

def test_get_max_triples_large_n():
    assert get_max_triples(20) == 1330

def test_get_max_triples_mod_3_distribution():
    # Test cases to check the distribution of remainders when divided by 3
    # This helps ensure the logic correctly counts triples based on remainders
    n = 15
    result = get_max_triples(n)
    assert result == 455

    n = 18
    result = get_max_triples(n)
    assert result == 816

def test_get_max_triples_edge_case():
    # Test with a slightly larger n to check for potential overflow issues
    n = 30
    result = get_max_triples(n)
    assert result == 4060

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
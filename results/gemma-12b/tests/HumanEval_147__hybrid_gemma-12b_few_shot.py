
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
from typing import List

def get_max_triples(n: int) -> int:
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

@pytest.fixture
def sample_array():
    """Fixture to generate a sample array for testing."""
    return [i * i - i + 1 for i in range(1, 6)]  # Example array from the problem description


# Tests for get_max_triples
def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_small():
    assert get_max_triples(3) == 0

def test_get_max_triples_larger():
    assert get_max_triples(10) == 11

def test_get_max_triples_n_equals_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_equals_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_with_fixture():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_equals_6():
    assert get_max_triples(6) == 17

def test_get_max_triples_n_equals_7():
    assert get_max_triples(7) == 26

def test_get_max_triples_n_equals_8():
    assert get_max_triples(8) == 37

def test_get_max_triples_n_5(sample_array):
    assert get_max_triples(5) == 1

# Palindrome tests
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Max element tests
def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
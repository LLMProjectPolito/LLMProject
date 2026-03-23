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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Triples Tests
def test_get_max_triples_n_5(sample_array):
    """Test case for n = 5, as described in the problem."""
    assert get_max_triples(5) == 1

def test_get_max_triples_n_1():
    """Test case for n = 1. Should return 0 as no triples are possible."""
    assert get_max_triples(1) == 0

def test_get_max_triples_n_2():
    """Test case for n = 2. Should return 0 as no triples are possible."""
    assert get_max_triples(2) == 0

def test_get_max_triples_n_3():
    """Test case for n = 3."""
    assert get_max_triples(3) == 0

def test_get_max_triples_n_4():
    """Test case for n = 4."""
    assert get_max_triples(4) == 0

def test_get_max_triples_n_6():
    """Test case for n = 6."""
    assert get_max_triples(6) == 2

def test_get_max_triples_n_7():
    """Test case for n = 7."""
    assert get_max_triples(7) == 3

def test_get_max_triples_large_n():
    """Test case for a larger n to check performance and correctness."""
    assert get_max_triples(10) == 6

def test_get_max_triples_n_100():
    """Test case for a larger n to check performance and correctness."""
    assert get_max_triples(100) == 1617


# Palindrome Tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Max Tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
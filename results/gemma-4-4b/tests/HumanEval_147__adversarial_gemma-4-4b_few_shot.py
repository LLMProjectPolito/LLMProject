
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Race car') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('Madam, I\'m Adam') == True

def test_is_palindrome_edge_cases():
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('redder') == True
    assert is_palindrome('reviver') == True
    assert is_palindrome('detartrated') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 2, 8, 1, 9]) == 9
    assert get_max([10, 5, 20, 15]) == 20
    assert get_max([1]) == 1

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-5, -2, -8, -1, -9]) == -1
    assert get_max([-10, -5, -20, -15]) == -5

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4, -5]) == 4
    assert get_max([1, -2, 3, -4, 5]) == 5
    assert get_max([-10, 5, -20, 15]) == 15

def test_get_max_duplicate():
    assert get_max([1, 1, 1]) == 1
    assert get_max([5, 5, 5]) == 5
    assert get_max([-1, -1, -1]) == -1
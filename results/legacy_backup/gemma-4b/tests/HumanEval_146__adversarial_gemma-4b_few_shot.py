import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) > 0 and (int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0):
                count += 1
    return count


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('RaCeCaR') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([-1, -2, -3]) == -1

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-1, 2, -3]) == 2

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4
    assert get_max([1, -2, 3, -4]) == 3

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_none():
    assert specialFilter([-2, -4, -6]) == 0

def test_specialFilter_mixed():
    assert specialFilter([11, 13, 15, 17, 19, 22, 24, 26]) == 4

def test_specialFilter_edge_cases():
    assert specialFilter([11, 13, 15, 17, 19]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 5
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61]) == 5
import pytest

def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    total_sum = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total_sum += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total_sum += num**3
        else:
            total_sum += num
    return total_sum

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Pytest Suite for sum_squares

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 144

def test_sum_squares_multiple_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 222

def test_sum_squares_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 210

def test_sum_squares_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 160

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 3090000

def test_sum_squares_zeroes():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_single_element():
    assert sum_squares([5]) == 5

def test_sum_squares_negative_and_positive():
    assert sum_squares([-2, 3, -4, 5, -6]) == -2 + 9 - 64 + 25 - 216

def test_sum_squares_floats_converted_to_int():
    assert sum_squares([1.0, 2.0, 3.0]) == 6

def test_sum_squares_with_duplicates():
    assert sum_squares([1, 1, 1, 1, 1]) == 5

def test_sum_squares_long_list():
    long_list = list(range(1, 21))
    expected_sum = 0
    for i, num in enumerate(long_list):
        if i % 3 == 0:
            expected_sum += num**2
        elif i % 4 == 0 and i % 3 != 0:
            expected_sum += num**3
        else:
            expected_sum += num
    assert sum_squares(long_list) == expected_sum


# Pytest Suite for is_palindrome

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == False # Spaces are not ignored

def test_palindrome_single_char():
    assert is_palindrome('a') == True

# Pytest Suite for get_max

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_duplicates():
    assert get_max([1, 1, 1, 1]) == 1
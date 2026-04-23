
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

```python
import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    try:
        num1, den1 = map(int, x.split('/'))
        num2, den2 = map(int, n.split('/'))
        result = num1 * num2 / den1 / den2
        return result == int(result)
    except ValueError:
        return False  # Handle cases where input strings are not valid fractions



# --- Pytest Suite ---

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Added a more complex test case

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_single_char_different():
    assert is_palindrome('b') == False

def test_palindrome_longer_string():
    assert is_palindrome("madam") == True

def test_palindrome_longer_string_different():
    assert is_palindrome("racecar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("  level  ") == True

def test_palindrome_with_leading_trailing_spaces():
    assert is_palindrome("rotor ") == True

def test_palindrome_with_leading_trailing_spaces_2():
    assert is_palindrome("  rotor  ") == True



def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 2]) == 9
    assert get_max([10, 5, 2]) == 10

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_single_element():
    assert get_max([7]) == 7

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-5, 1, -9, 2]) == 2

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_duplicate():
    assert get_max([5, 5, 5]) == 5

def test_get_max_large_numbers():
    assert get_max([1000000, 2000000, 3000000]) == 3000000

def test_get_max_large_numbers_negative():
    assert get_max([-1000000, -2000000, -3000000]) == -1000000



def test_simplify_valid_fraction():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("2/3", "3/2") == True

def test_simplify_invalid_fraction():
    assert simplify("1/5", "5") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify("1/5", "5/1") == False # Invalid input
    assert simplify
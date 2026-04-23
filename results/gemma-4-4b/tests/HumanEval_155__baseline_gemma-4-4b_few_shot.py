
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    num_str = str(abs(num))  # Handle negative numbers
    for digit in num_str:
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('Racecar') == True
    assert is_palindrome('') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == False #with spaces and punctuation

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 2, 8, 1, 9]) == 9
    assert get_max([10, 5, 20, 1]) == 20

def test_get_max_empty():
    assert get_max([]) == None

def test_even_odd_count_positive():
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(1357) == (0, 5)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(222) == (3, 0)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-1357) == (0, 5)
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)
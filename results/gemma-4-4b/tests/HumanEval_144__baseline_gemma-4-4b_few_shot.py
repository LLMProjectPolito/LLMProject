
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
    def fraction_to_float(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator / denominator

    x_float = fraction_to_float(x)
    n_float = fraction_to_float(n)
    product = x_float * n_float
    return product.is_integer()

def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True
    assert is_palindrome('madam') == True
    assert is_palindrome('A man, a plan, a canal: Panama') == False #case sensitive
    assert is_palindrome('racecar') == True

def test_get_max():
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) == None
    assert get_max([5, 2, 8, 1, 9]) == 9
    assert get_max([10]) == 10
    assert get_max([-1, -5, -2]) == -1

def test_simplify():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "2/1") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/3", "1/3") == True
    assert simplify("1/4", "2/2") == True
    assert simplify("1/4", "3/2") == False
    assert simplify("1/1", "1/1") == True
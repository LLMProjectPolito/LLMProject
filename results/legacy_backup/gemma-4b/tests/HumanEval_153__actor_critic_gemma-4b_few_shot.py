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

def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    strongest_extension = None
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam.') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_is_palindrome_non_palindrome():
    assert is_palindrome('Python') == False

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_single():
    assert get_max([5]) == 5

def test_Strongest_Extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_Strongest_Extension_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_Strongest_Extension_empty_extensions():
    assert Strongest_Extension('my_class', []) == 'my_class.None'

def test_Strongest_Extension_all_uppercase():
    assert Strongest_Extension('my_class', ['ABC', 'DEF']) == 'my_class.ABC'

def test_Strongest_Extension_all_lowercase():
    assert Strongest_Extension('my_class', ['abc', 'def']) == 'my_class.abc'

def test_Strongest_Extension_mixed_case_and_numbers():
    assert Strongest_Extension('my_class', ['a1B', 'b2C']) == 'my_class.a1B'

def test_Strongest_Extension_complex_extension():
    assert Strongest_Extension('my_class', ['ExtensionWithNumbers123', 'AnotherExtension']) == 'my_class.ExtensionWithNumbers123'
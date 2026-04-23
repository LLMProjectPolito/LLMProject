
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

import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
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
        cap = 0
        sm = 0
        for char in extension:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1

        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


class TestIsPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

    def test_palindrome_single_char(self):
        assert is_palindrome('a') == True

    def test_palindrome_mixed_case(self):
        assert is_palindrome('Racecar') == True

    def test_palindrome_with_spaces(self):
        assert is_palindrome('A man, a plan, a canal: Panama') == False

    def test_palindrome_with_special_chars(self):
        assert is_palindrome('Madam, I\'m Adam') == False

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) is None

    def test_max_single_element(self):
        assert get_max([5]) == 5

    def test_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4

class TestStrongest_Extension:
    def test_example_case(self):
        assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

    def test_empty_extensions(self):
        assert Strongest_Extension('test', []) == 'test. '

    def test_same_strength(self):
        assert Strongest_Extension('class', ['A', 'B']) == 'class.A'

    def test_mixed_case_extensions(self):
        assert Strongest_Extension('test', ['Test', 'tEst']) == 'test.Test'

    def test_long_extensions(self):
        assert Strongest_Extension('test', ['ExtremelyLongExtension123', 'Short']) == 'test.ExtremelyLongExtension123'

    def test_all_lowercase_extensions(self):
        assert Strongest_Extension('test', ['lowercase', 'another']) == 'test.lowercase'

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
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    if strongest_extension:
        return f"{class_name}.{strongest_extension}"
    else:
        return f"{class_name}.None"  # Handle the case where extensions is empty


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Suite 1 Tests
def test_strongest_extension_basic():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_strongest_extension_example():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_strongest_extension_same_strength():
    assert Strongest_Extension("TestClass", ["AA", "BB", "CC"]) == "TestClass.AA"

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension("Class", ["AAAA", "BBB", "CCCC"]) == "Class.AAAA"

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension("Class", ["aaaa", "bbbb", "cccc"]) == "Class.aaaa"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("Class", ["aA", "bB", "cC"]) == "Class.aA"

def test_strongest_extension_with_numbers():
    assert Strongest_Extension("Class", ["A1", "B2", "C3"]) == "Class.A1"

def test_strongest_extension_with_special_characters():
    assert Strongest_Extension("Class", ["!A", "#B", "$C"]) == "Class.!A"

def test_strongest_extension_long_extensions():
    assert Strongest_Extension("Class", ["ThisIsALongExtension", "AnotherLongExtension"]) == "Class.ThisIsALongExtension"

def test_strongest_extension_equal_strength_and_length():
    assert Strongest_Extension("Class", ["AA", "BB"]) == "Class.AA"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Class", ["be", "aa"]) == "Class.be"

# Suite 2 Tests
def test_strongest_extension_negative_strength_suite2():
    assert Strongest_Extension("Class", ["abc", "DEF"]) == "Class.DEF"

def test_strongest_extension_mixed_case_suite2():
    assert Strongest_Extension("Class", ["aBc", "DeF"]) == "Class.DeF"

def test_strongest_extension_all_uppercase_suite2():
    assert Strongest_Extension("Class", ["ABC", "DEF"]) == "Class.ABC"

def test_strongest_extension_all_lowercase_suite2():
    assert Strongest_Extension("Class", ["abc", "def"]) == "Class.abc"

def test_strongest_extension_with_numbers_suite2():
    assert Strongest_Extension("Class", ["A12", "b34"]) == "Class.A12"

def test_strongest_extension_with_special_characters_suite2():
    assert Strongest_Extension("Class", ["A!", "b?"]) == "Class.A!"

def test_strongest_extension_long_extensions_suite2():
    assert Strongest_Extension("Class", ["ThisIsALongExtension", "AnotherLongExtension"]) == "Class.ThisIsALongExtension"

def test_strongest_extension_duplicate_extensions_suite2():
    assert Strongest_Extension("Class", ["AA", "AA", "BB"]) == "Class.AA"

def test_strongest_extension_class_with_special_characters_suite2():
    assert Strongest_Extension("My_Class!", ["AA", "BB"]) == "My_Class!.AA"

# Palindrome Tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Get Max Tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None
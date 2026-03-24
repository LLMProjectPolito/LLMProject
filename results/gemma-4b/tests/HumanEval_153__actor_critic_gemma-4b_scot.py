
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
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


### SCoT Steps:

# STEP 1: REASONING
# The function takes a class name and a list of extensions. It calculates the strength of each extension based on the difference between uppercase and lowercase letters. It returns the name of the strongest extension in the format "ClassName.StrongestExtensionName". If multiple extensions have the same strength, it returns the first one encountered.
# Edge cases to consider:
# 1. Empty extensions list: Should return the class name.
# 2. Extensions with no uppercase letters: Should return the first extension.
# 3. Extensions with no lowercase letters: Should return the first extension.
# 4. Extensions with equal strength: Should return the first one.
# 5. Class name is empty string: Should return an empty string.
# 6. Extensions with mixed case and special characters.

# STEP 2: PLAN
# Test functions:
# - test_empty_extensions: Tests the case where the extensions list is empty.
# - test_no_uppercase: Tests the case where all extensions have no uppercase letters.
# - test_no_lowercase: Tests the case where all extensions have no lowercase letters.
# - test_equal_strength: Tests the case where multiple extensions have the same strength.
# - test_mixed_case: Tests the case where extensions have mixed case.
# - test_class_name_empty: Tests the case where the class name is empty.
# - test_single_extension: Tests the case with a single extension.
# - test_multiple_extensions: Tests the case with multiple extensions.
# - test_complex_extension: Tests an extension with special characters and mixed case.

# STEP 3: CODE
###
def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class."

def test_no_uppercase():
    assert Strongest_Extension("my_class", ["abc", "def"]) == "my_class.abc"

def test_no_lowercase():
    assert Strongest_Extension("my_class", ["ABC", "DEF"]) == "my_class.ABC"

def test_equal_strength():
    assert Strongest_Extension("my_class", ["AA", "BB"]) == "my_class.AA"

def test_mixed_case():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_class_name_empty():
    assert Strongest_Extension("", ["AA", "BB"]) == ".AA"

def test_single_extension():
    assert Strongest_Extension("my_class", ["AA"]) == "my_class.AA"

def test_multiple_extensions():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_complex_extension():
    assert Strongest_Extension("my_class", ["aA", "bB", "cC"]) == "my_class.aA"
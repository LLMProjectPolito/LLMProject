
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
# The function takes a class name and a list of extensions. It calculates the strength of each extension based on the difference between uppercase and lowercase letters. It returns the strongest extension in the format "ClassName.StrongestExtensionName".
# Edge cases to consider:
# 1. Empty extensions list: Should return the class name itself.
# 2. Extensions with equal strength: Should return the first one encountered.
# 3. Extensions with no uppercase or lowercase letters: Should return the first one encountered.
# 4. Class name is empty string: Should return an empty string.
# 5. Extensions with only uppercase or only lowercase letters.

# STEP 2: PLAN
# Test functions:
# 1. test_empty_extensions: Tests the case where the extensions list is empty.
# 2. test_single_extension: Tests the case where there is only one extension.
# 3. test_multiple_extensions_different_strengths: Tests the case where there are multiple extensions with different strengths.
# 4. test_multiple_extensions_equal_strengths: Tests the case where there are multiple extensions with the same strength.
# 5. test_extension_with_no_uppercase: Tests the case where an extension has no uppercase letters.
# 6. test_extension_with_no_lowercase: Tests the case where an extension has no lowercase letters.
# 7. test_extension_with_only_uppercase: Tests the case where an extension has only uppercase letters.
# 8. test_extension_with_only_lowercase: Tests the case where an extension has only lowercase letters.
# 9. test_empty_class_name: Tests the case where the class name is empty.

# STEP 3: CODE
###
def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class."

def test_single_extension():
    assert Strongest_Extension("Slices", ["SErviNGSliCes"]) == "Slices.SErviNGSliCes"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_multiple_extensions_equal_strengths():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_extension_with_no_uppercase():
    assert Strongest_Extension("my_class", ["bee", "zzz"]) == "my_class.bee"

def test_extension_with_no_lowercase():
    assert Strongest_Extension("my_class", ["AAA", "BBB"]) == "my_class.AAA"

def test_extension_with_only_uppercase():
    assert Strongest_Extension("my_class", ["ABC", "DEF"]) == "my_class.ABC"

def test_extension_with_only_lowercase():
    assert Strongest_Extension("my_class", ["abc", "def"]) == "my_class.abc"

def test_empty_class_name():
    assert Strongest_Extension("", ["AA", "BB"]) == ""
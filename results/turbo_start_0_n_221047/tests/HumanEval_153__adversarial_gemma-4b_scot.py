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
# The function `Strongest_Extension` takes a class name and a list of extensions.
# It calculates the strength of each extension based on the difference between
# the number of uppercase and lowercase letters. It returns the name of the
# strongest extension in the format "ClassName.StrongestExtensionName".
# If multiple extensions have the same strength, it returns the first one.
# We need to test various scenarios including:
# 1. Empty extension list.
# 2. Single extension.
# 3. Multiple extensions with different strengths.
# 4. Multiple extensions with the same strength.
# 5. Extensions with only uppercase letters.
# 6. Extensions with only lowercase letters.
# 7. Extensions with mixed case letters.

# STEP 2: PLAN
# Test functions:
# - test_empty_extensions: Tests the case where the extensions list is empty.
# - test_single_extension: Tests the case where there is only one extension.
# - test_multiple_extensions_different_strengths: Tests the case where extensions
#   have different strengths.
# - test_multiple_extensions_same_strength: Tests the case where extensions have
#   the same strength.
# - test_all_uppercase_extensions: Tests the case where all extensions are uppercase.
# - test_all_lowercase_extensions: Tests the case where all extensions are lowercase.
# - test_mixed_case_extensions: Tests the case where extensions have mixed case.
# - test_class_name_empty: Tests the case where the class name is empty.

# STEP 3: CODE
# pytest suite
def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class."

def test_single_extension():
    assert Strongest_Extension("my_class", ["AA"]) == "my_class.AA"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_all_uppercase_extensions():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_all_lowercase_extensions():
    assert Strongest_Extension("my_class", ["aa", "bb", "cc"]) == "my_class.aa"

def test_mixed_case_extensions():
    assert Strongest_Extension("my_class", ["Aa", "Bb", "Cc"]) == "my_class.Aa"

def test_class_name_empty():
    assert Strongest_Extension("", ["AA", "BB"]) == ""
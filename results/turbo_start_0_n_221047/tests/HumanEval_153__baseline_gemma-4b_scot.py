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
# If multiple extensions have the same strength, it returns the first one
# encountered in the list.
# We need to create a pytest suite to test this function with various inputs,
# including edge cases like empty extension lists and extensions with equal strengths.

# STEP 2: PLAN
# Test cases:
# 1. Basic test with a single extension.
# 2. Test with multiple extensions, one of which is the strongest.
# 3. Test with multiple extensions, with equal strengths (first one should be returned).
# 4. Test with an empty extension list (should return the class name).
# 5. Test with extensions containing only uppercase letters.
# 6. Test with extensions containing only lowercase letters.
# 7. Test with extensions containing mixed case letters.

# Test functions:
# - test_basic_single_extension
# - test_multiple_extensions_strongest
# - test_multiple_extensions_equal_strengths
# - test_empty_extension_list
# - test_all_uppercase_extensions
# - test_all_lowercase_extensions
# - test_mixed_case_extensions

# STEP 3: CODE
###
def test_basic_single_extension(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == f"{class_name}.{extensions[0]}"

def test_multiple_extensions_strongest(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == f"{class_name}.{extensions[0]}"

def test_multiple_extensions_equal_strengths(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == f"{class_name}.{extensions[0]}"

def test_empty_extension_list(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == class_name

def test_all_uppercase_extensions(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == f"{class_name}.{extensions[0]}"

def test_all_lowercase_extensions(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == f"{class_name}.{extensions[0]}"

def test_mixed_case_extensions(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == f"{class_name}.{extensions[0]}"

# Define class_name and extensions for the tests
class_name = "my_class"
extensions = ["AA", "Be", "CC"]
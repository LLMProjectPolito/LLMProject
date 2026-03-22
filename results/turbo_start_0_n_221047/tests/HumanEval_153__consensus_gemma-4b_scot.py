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
# STEP 1: REASONING - The function calculates the strength of each extension based on the difference between uppercase and lowercase letters. It then finds the extension with the maximum strength and returns the formatted string. Edge cases include empty extension list, extensions with equal strengths, and extensions with no uppercase or lowercase letters.
# STEP 2: PLAN -
# Test cases:
# 1. Basic test with a single extension.
# 2. Test with multiple extensions, one of which is the strongest.
# 3. Test with multiple extensions having the same strength (should return the first one).
# 4. Test with an empty extension list (should return the class name).
# 5. Test with extensions containing only uppercase letters.
# 6. Test with extensions containing only lowercase letters.
# 7. Test with extensions containing a mix of uppercase and lowercase letters.
# 8. Test with a class name containing special characters.
# 9. Test with extensions with zero strength.
# 10. Test with a class name and extensions with similar strengths.
# STEP 3: CODE -
###

def test_basic_single_extension():
    assert Strongest_Extension("Slices", ["SErviNGSliCes"]) == "Slices.SErviNGSliCes"

def test_multiple_extensions_strongest_first():
    assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_empty_extension_list():
    assert Strongest_Extension("Slices", []) == "Slices."

def test_extensions_only_uppercase():
    assert Strongest_Extension("my_class", ["ABC", "DEF"]) == "my_class.ABC"

def test_extensions_only_lowercase():
    assert Strongest_Extension("my_class", ["abc", "def"]) == "my_class.abc"

def test_extensions_mixed_case():
    assert Strongest_Extension("my_class", ["aBc", "DeF"]) == "my_class.aBc"

def test_class_name_with_special_characters():
    assert Strongest_Extension("My Class!", ["abc", "DEF"]) == "My Class!.abc"

def test_extensions_with_zero_strength():
    assert Strongest_Extension("my_class", ["abc", "DEF"]) == "my_class.abc"

def test_similar_strengths():
    assert Strongest_Extension("my_class", ["AA", "BB"]) == "my_class.AA"

def test_complex_extension():
    assert Strongest_Extension("Data", ["DataScience", "Analytics", "MachineLearning"]) == "Data.DataScience"

def test_empty_class_name():
    assert Strongest_Extension("", ["AA", "BB"]) == ""
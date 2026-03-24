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
    strongest_extension = ""
    max_strength = float('-inf')
    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + "." + strongest_extension

### SCoT Steps:
# STEP 1: REASONING - The function takes a class name and a list of extensions. It calculates the strength of each extension (CAP - SM) and returns the extension with the highest strength. If multiple extensions have the same strength, it returns the first one encountered. The function should handle empty extension lists gracefully.
# STEP 2: PLAN -
# Test cases:
# 1. Basic test with a single extension and positive strength.
# 2. Test with multiple extensions, one with higher strength.
# 3. Test with multiple extensions, with the same strength (first one should be returned).
# 4. Test with an empty extension list.
# 5. Test with extensions containing only uppercase letters.
# 6. Test with extensions containing only lowercase letters.
# 7. Test with mixed case extensions.
# 8. Test with extensions containing numbers and special characters.
# STEP 3: CODE -
# def test_basic_positive_strength():
#     assert Strongest_Extension("Slices", ["SErviNGSliCes"]) == "Slices.SErviNGSliCes"
# def test_multiple_extensions_higher_strength():
#     assert Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"
# def test_multiple_extensions_same_strength():
#     assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"
# def test_empty_extension_list():
#     assert Strongest_Extension("my_class", []) == "my_class."
# def test_all_uppercase_extensions():
#     assert Strongest_Extension("my_class", ["ABC", "DEF"]) == "my_class.ABC"
# def test_all_lowercase_extensions():
#     assert Strongest_Extension("my_class", ["abc", "def"]) == "my_class.abc"
# def test_mixed_case_extensions():
#     assert Strongest_Extension("my_class", ["aBc", "DeF"]) == "my_class.aBc"
# def test_extensions_with_numbers_and_special_characters():
#     assert Strongest_Extension("my_class", ["A1B", "b2C"]) == "my_class.A1B"
# def test_single_extension():
#     assert Strongest_Extension("my_class", ["A"]) == "my_class.A"
# def test_single_extension_lowercase():
#     assert Strongest_Extension("my_class", ["a"]) == "my_class.a"
# def test_complex_extension():
#     assert Strongest_Extension("my_class", ["ExtensionWith123Letters"]) == "my_class.ExtensionWith123Letters"
# def test_extension_with_spaces():
#     assert Strongest_Extension("my_class", ["Extension With Spaces"]) == "my_class.Extension With Spaces"
# def test_extension_with_special_chars():
#     assert Strongest_Extension("my_class", ["Extension!@#"]) == "my_class.Extension!@#"
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
# STEP 1: REASONING - The function needs to iterate through the extensions, calculate their strength, and find the one with the highest strength. If multiple extensions have the same strength, the first one encountered should be chosen. The return value should be in the specified format.
# STEP 2: PLAN -
# - Test case 1: Empty extensions list.
# - Test case 2: Single extension.
# - Test case 3: Multiple extensions with different strengths.
# - Test case 4: Multiple extensions with the same strength (first one should be chosen).
# - Test case 5: Extension with no uppercase letters.
# - Test case 6: Extension with no lowercase letters.
# - Test case 7: Extension with mixed case and special characters.
# - Test case 8: Class name is empty string.
# STEP 3: CODE -

def test_empty_extensions():
    assert Strongest_Extension("my_class", []) == "my_class."

def test_single_extension():
    assert Strongest_Extension("my_class", ["AA"]) == "my_class.AA"

def test_multiple_extensions_different_strengths():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_multiple_extensions_same_strength():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_extension_no_uppercase():
    assert Strongest_Extension("my_class", ["be", "de", "fe"]) == "my_class.be"

def test_extension_no_lowercase():
    assert Strongest_Extension("my_class", ["AA", "BB", "CC"]) == "my_class.AA"

def test_extension_mixed_case_special_chars():
    assert Strongest_Extension("my_class", ["aB1", "cDe2", "fG3"]) == "my_class.aB1"

def test_empty_class_name():
    assert Strongest_Extension("", ["AA", "BB"]) == ""

def test_class_name_with_spaces():
    assert Strongest_Extension("My Class", ["aa", "BB"]) == "My Class.aa"

def test_class_name_with_numbers():
    assert Strongest_Extension("Class123", ["aa", "BB"]) == "Class123.aa"
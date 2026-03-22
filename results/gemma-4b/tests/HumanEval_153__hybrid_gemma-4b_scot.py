import pytest

def strongest_extension(class_name, extensions):
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

    if not extensions:
        return f"{class_name}.None"  # Handle empty extension list

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def test_strongest_extension_basic():
    assert strongest_extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_strongest_extension_same_strength():
    assert strongest_extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

def test_strongest_extension_empty_extensions():
    assert strongest_extension("Class", []) == "Class.None"

def test_strongest_extension_mixed_case():
    assert strongest_extension("Mixed", ['aBc', 'DeF', 'GhI']) == "Mixed.aBc"

def test_strongest_extension_special_chars():
    assert strongest_extension("Special", ['!@#', 'abc', '123']) == "Special.!@#"

def test_strongest_extension_single_extension():
    assert strongest_extension("Single", ['Only']) == "Single.Only"

def test_strongest_extension_all_uppercase():
    assert strongest_extension("Upper", ['ABC', 'DEF', 'GHI']) == "Upper.ABC"

def test_strongest_extension_all_lowercase():
    assert strongest_extension("Lower", ['abc', 'def', 'ghi']) == "Lower.abc"
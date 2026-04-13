
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
    if not extensions:
        return class_name  # Handle empty extensions list

    strongest_extension = extensions[0]
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        
        try:
            strength = cap_count - sm_count
        except TypeError:
            strength = float('-inf') #Handle cases where extension is not a string

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

# Pytest tests
def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('Test', ['aA', 'Bb', 'Cc']) == 'my_class.AA'

def test_strongest_extension_empty_list():
    assert Strongest_Extension('MyClass', []) == 'MyClass'

def test_strongest_extension_same_strength():
    assert Strongest_Extension('Class', ['AB', 'Cd', 'EF']) == 'Class.AB'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('Class', ['abc', 'def', 'ghi']) == 'Class.abc'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('Class', ['ABC', 'DEF', 'GHI']) == 'Class.ABC'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Class', ['aBc', 'DeF', 'gHi']) == 'Class.aBc'

def test_strongest_extension_single_extension():
    assert Strongest_Extension('Class', ['Extension']) == 'Class.Extension'

def test_strongest_extension_with_numbers():
    assert Strongest_Extension('Class', ['Ext1', 'Ext2', 'Ext3']) == 'Class.Ext1'

def test_strongest_extension_with_special_characters():
    assert Strongest_Extension('Class', ['Ext!', 'Ext@', 'Ext#']) == 'Class.Ext!'

def test_strongest_extension_non_string_extension():
    assert Strongest_Extension('Class', [123, 'Ext']) == 'Class.Ext'
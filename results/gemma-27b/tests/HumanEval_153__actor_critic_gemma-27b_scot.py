
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
        return class_name

    strongest_extension = extensions[0]
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


def test_strongest_extension_basic():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass"

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension("Class", ['AA', 'BB', 'CC']) == 'Class.AA'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension("Class", ['aa', 'bb', 'cc']) == 'Class.aa'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("Class", ['Aa', 'bB', 'Cc']) == 'Class.bB'

def test_strongest_extension_same_strength():
    assert Strongest_Extension("Class", ['Aa', 'Aa', 'Bb']) == 'Class.Aa'

def test_strongest_extension_empty_class_name():
    assert Strongest_Extension("", ['AA', 'Be', 'CC']) == '.AA'

def test_strongest_extension_extensions_with_non_letters():
    assert Strongest_Extension("Class", ['A1', 'b2', 'C3']) == 'Class.A1'

def test_strongest_extension_negative_strength():
    # Extensions with more lowercase letters are chosen because of the negative strength.
    assert Strongest_Extension("Class", ['aA', 'bB', 'cC']) == 'Class.aA'

def test_strongest_extension_empty_string():
    assert Strongest_Extension("Class", ['', 'AA', 'BB']) == 'Class.AA'
    assert Strongest_Extension("Class", ['AA', '', 'BB']) == 'Class.AA'
    assert Strongest_Extension("Class", ['AA', 'BB', '']) == 'Class.AA'

def test_strongest_extension_leading_trailing_spaces():
    assert Strongest_Extension("  Class  ", ['AA', 'Be', 'CC']) == '  Class  .AA'

def test_strongest_extension_equal_strength_with_empty_string():
    assert Strongest_Extension("Class", ['', 'AA', 'BB']) == 'Class.AA'

def test_strongest_extension_all_same_strength():
    assert Strongest_Extension("Class", ['', '', '']) == 'Class.'

def test_strongest_extension_leading_trailing_spaces_confirm():
    assert Strongest_Extension("  Class  ", ['  AA  ', 'BB']) == '  Class  .  AA  '
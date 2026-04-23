
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
    """
    strongest_extension = None
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())

        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    if strongest_extension is None:
        raise ValueError("Extensions list is empty")

    return f"{class_name}.{strongest_extension}"

def test_basic_case():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_equal_strength_first_wins():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_empty_extensions_list():
    with pytest.raises(ValueError):
        Strongest_Extension('my_class', [])

def test_all_uppercase():
    assert Strongest_Extension('my_class', ['AAA', 'BBB', 'CCC']) == 'my_class.AAA'

def test_all_lowercase():
    assert Strongest_Extension('my_class', ['aaa', 'bbb', 'ccc']) == 'my_class.aaa'

def test_mixed_case():
    assert Strongest_Extension('my_class', ['aA', 'Bb', 'Cc']) == 'my_class.aA'

def test_extensions_with_non_alphabetic_characters():
    assert Strongest_Extension('my_class', ['Ext123!', 'Ext456@', 'Ext789#']) == 'my_class.Ext123!'

def test_extension_with_spaces():
    assert Strongest_Extension('my_class', ['Ext A', 'ExtB', 'Ext C']) == 'my_class.ExtB'

def test_negative_strength():
    assert Strongest_Extension('my_class', ['abc', 'def', 'ghi']) == 'my_class.abc'

def test_zero_strength():
    assert Strongest_Extension('my_class', ['aA', 'bB', 'cC']) == 'my_class.aA'

def test_long_extensions():
    assert Strongest_Extension('my_class', ['VeryLongExtensionWithManyUpperCaseLetters', 'AnotherVeryLongExtensionWithManyLowerCaseLetters']) == 'my_class.VeryLongExtensionWithManyUpperCaseLetters'

def test_class_name_with_special_characters():
    assert Strongest_Extension('my_class!', ['AA', 'Be', 'CC']) == 'my_class!.AA'

def test_extension_names_with_same_length():
    assert Strongest_Extension('my_class', ['AbCd', 'aBcD']) == 'my_class.AbCd'

def test_empty_extension_names():
    assert Strongest_Extension('my_class', ['', 'AA', 'BB']) == 'my_class.AA'

def test_large_number_of_extensions():
    extensions = ['A' * i for i in range(1000)]
    assert Strongest_Extension('my_class', extensions) == 'my_class.A' * 999

def test_extensions_with_only_non_alphabetic_characters():
    assert Strongest_Extension('my_class', ['123', '!', '#$']) == 'my_class.123'

def test_extensions_with_same_strength_and_length():
    assert Strongest_Extension('my_class', ['Aa', 'aA', 'Bb']) == 'my_class.Aa'
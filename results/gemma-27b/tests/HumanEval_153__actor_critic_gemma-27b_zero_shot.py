
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
        cap_count = 0
        sm_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap_count += 1
            elif 'a' <= char <= 'z':
                sm_count += 1

        strength = cap_count - sm_count  # Strength calculation: CAP - SM

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    if strongest_extension is None:
        return f"{class_name}."
    return f"{class_name}.{strongest_extension}"

def test_basic_case():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_equal_strength_first_wins():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_empty_list():
    assert Strongest_Extension('my_class', []) == 'my_class.'

def test_case_sensitivity():
    assert Strongest_Extension('my_class', ['aA', 'Bb', 'Cc', 'AA', 'bb', 'CC']) == 'my_class.AA'

def test_numbers_and_symbols():
    assert Strongest_Extension('my_class', ['123Abc!', 'Def456', 'Ghi789']) == 'my_class.Def456'

def test_empty_string():
    assert Strongest_Extension('my_class', ['', 'Abc', 'Def']) == 'my_class.Def'

def test_class_name_with_spaces():
    assert Strongest_Extension('my class', ['Abc', 'Def']) == 'my class.Def'

def test_extension_names_with_spaces():
    assert Strongest_Extension('my_class', ['Abc Def', 'Def Ghi']) == 'my_class.Abc Def'

def test_negative_strength():
    assert Strongest_Extension('my_class', ['abc', 'DEF', 'aBc']) == 'my_class.DEF'

def test_equal_strength_and_empty_string():
    assert Strongest_Extension('my_class', ['', 'AA']) == 'my_class.AA'

def test_unicode_characters():
    assert Strongest_Extension('my_class', ['ÄÄ', 'ää', '你好', '世界']) == 'my_class.ÄÄ'

def test_only_numbers_and_symbols():
    assert Strongest_Extension('my_class', ['123!', '#$%^']) == 'my_class.123!'

def test_very_similar_extensions():
    assert Strongest_Extension('my_class', ['AbC', 'aBC']) == 'my_class.AbC'

def test_all_zero_strength():
    assert Strongest_Extension('my_class', ['abc', 'def', 'ghi']) == 'my_class.abc'
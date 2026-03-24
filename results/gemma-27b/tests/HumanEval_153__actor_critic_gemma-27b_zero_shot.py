
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
    If the extensions list is empty, raise a ValueError.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    >>> Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
    'my_class.AA'
    """
    if not extensions:
        raise ValueError("Extensions list cannot be empty.")

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

        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def test_basic_case():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_equal_strength_first_wins():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_empty_extensions_list():
    with pytest.raises(ValueError):
        Strongest_Extension('my_class', [])

@pytest.mark.parametrize("extensions", [
    ['AAA', 'BBB', 'CCC'],
    ['aaa', 'bbb', 'ccc'],
    ['aA', 'Bb', 'Cc']
])
def test_case_variations(extensions):
    assert Strongest_Extension('my_class', extensions) == 'my_class.' + extensions[0]

def test_numbers_and_symbols():
    assert Strongest_Extension('my_class', ['123', 'abc', 'A1B2']) == 'my_class.A1B2'

def test_extension_with_spaces():
    assert Strongest_Extension('my_class', ['A B', 'a b', 'C D']) == 'my_class.A B'

def test_long_extensions():
    assert Strongest_Extension('my_class', ['VeryLongExtensionName', 'ShortExtension']) == 'my_class.VeryLongExtensionName'

def test_negative_strength():
    assert Strongest_Extension('my_class', ['abcDEF', 'AbCdEf']) == 'my_class.abcDEF'

def test_same_strength_multiple():
    assert Strongest_Extension('my_class', ['Aa', 'aA', 'Bb']) == 'my_class.Aa'

def test_class_name_spaces():
    assert Strongest_Extension('my class', ['AA', 'Be', 'CC']) == 'my class.AA'

def test_class_name_numbers():
    assert Strongest_Extension('my_class123', ['AA', 'Be', 'CC']) == 'my_class123.AA'

def test_extensions_non_alphabetic():
    assert Strongest_Extension('my_class', ['12345', '!!!@@@', '   ']) == 'my_class.12345'

def test_large_number_of_extensions():
    extensions = ['A' * i for i in range(1000)]
    assert Strongest_Extension('my_class', extensions) == 'my_class.A999'
    
def test_unicode_characters():
    assert Strongest_Extension('my_class', ['ÄÄ', 'ää', 'Áa']) == 'my_class.ÄÄ'

def test_empty_string_extension():
    assert Strongest_Extension('my_class', ['', 'AA']) == 'my_class.AA'

def test_strength_zero():
    assert Strongest_Extension('my_class', ['Aa', 'Bb']) == 'my_class.Aa'
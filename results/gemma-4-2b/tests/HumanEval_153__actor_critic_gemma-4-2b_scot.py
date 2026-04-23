
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
        return f"{class_name}.NoExtension"

    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


def test_empty_class_name():
    assert Strongest_Extension('', ['AA', 'Be', 'CC']) == '.AA'

def test_empty_extension_list():
    assert Strongest_Extension('my_class', []) == 'my_class.NoExtension'

def test_all_extensions_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'BB', 'CC']) == 'my_class.AA'

def test_extensions_with_no_uppercase_lowercase():
    assert Strongest_Extension('my_class', ['aaa', 'bbb', 'ccc']) == 'my_class.aaa'

def test_extensions_with_mixed_case():
    assert Strongest_Extension('my_class', ['aA', 'bB', 'cCc']) == 'my_class.aA'

def test_empty_extension_name():
    assert Strongest_Extension('my_class', ['']) == 'my_class.NoExtension'

def test_single_character_extension_name():
    assert Strongest_Extension('my_class', ['A']) == 'my_class.A'

def test_extension_name_is_number():
    assert Strongest_Extension('my_class', ['123']) == 'my_class.123'

def test_extension_name_is_special_character():
    assert Strongest_Extension('my_class', ['!@#']) == 'my_class.!@#'

def test_mixed_case_and_special_characters():
    assert Strongest_Extension('my_class', ['!aA#']) == 'my_class.!aA#'

def test_extension_with_only_uppercase():
    assert Strongest_Extension('my_class', ['AA']) == 'my_class.AA'

def test_extension_with_only_lowercase():
    assert Strongest_Extension('my_class', ['bb']) == 'my_class.bb'

def test_extension_with_mixed_case_and_special_characters_and_numbers():
    assert Strongest_Extension('my_class', ['!aA1#']) == 'my_class.!aA1#'

def test_extension_name_with_spaces():
    assert Strongest_Extension('my_class', ['Extension with spaces']) == 'my_class.Extension with spaces'

def test_extension_name_with_leading_trailing_spaces():
    assert Strongest_Extension('my_class', [' Extension with spaces']) == 'my_class. Extension with spaces'

def test_extension_name_with_unicode():
    assert Strongest_Extension('my_class', ['Extension with unicode']) == 'my_class.Extension with unicode'
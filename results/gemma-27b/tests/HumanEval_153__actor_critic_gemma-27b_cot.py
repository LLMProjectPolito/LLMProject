
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

def test_basic_case():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_equal_strength_first_wins():
    assert Strongest_Extension('Test', ['Aa', 'aA']) == 'Test.Aa'

def test_empty_extensions_list():
    assert Strongest_Extension('Class', []) == 'Class.'

def test_single_extension():
    assert Strongest_Extension('Class', ['Extension']) == 'Class.Extension'

def test_empty_string_extension():
    assert Strongest_Extension('Class', ['']) == 'Class.'

def test_class_name_with_numbers():
    assert Strongest_Extension('Class123', ['Extension']) == 'Class123.Extension'

def test_class_name_with_symbols():
    assert Strongest_Extension('Class!@#', ['Extension']) == 'Class!@#.Extension'

def test_long_extensions():
    assert Strongest_Extension('Class', ['VeryLongExtension1', 'VeryLongExtension2']) == 'Class.VeryLongExtension1'

def test_extensions_with_spaces():
    assert Strongest_Extension('Class', ['Extension With Spaces', 'AnotherExtension']) == 'Class.Extension With Spaces'

def test_all_zero_strength():
    assert Strongest_Extension('Class', ['ab', 'cd', 'ef']) == 'Class.ab'

def test_empty_class_name():
    assert Strongest_Extension('', ['Extension']) == '.Extension'

def test_extension_list_contains_none():
    with pytest.raises(TypeError):
        Strongest_Extension('Class', [None, 'Extension'])

def test_extension_list_contains_int():
    with pytest.raises(TypeError):
        Strongest_Extension('Class', [123, 'Extension'])

def test_extension_list_contains_float():
    with pytest.raises(TypeError):
        Strongest_Extension('Class', [1.23, 'Extension'])

def test_empty_class_and_empty_extensions():
    assert Strongest_Extension('', []) == '.'

def test_duplicate_extensions():
    assert Strongest_Extension('Class', ['Extension', 'Extension']) == 'Class.Extension'

@pytest.mark.parametrize("extensions", [
    (['EXTENSION1', 'EXTENSION2']),
    (['extension1', 'extension2']),
    (['ExTeNsIoN', 'extension'])
])
def test_case_insensitivity(extensions):
    assert Strongest_Extension('Class', extensions) == 'Class.' + extensions[0]

def test_same_strength():
    assert Strongest_Extension('Class', ['AB', 'cd']) == 'Class.AB'

def test_zero_strength():
    assert Strongest_Extension('Class', ['aB', 'Ab']) == 'Class.aB'
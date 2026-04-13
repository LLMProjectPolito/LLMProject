
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
    assert Strongest_Extension('MyClass', ['AA', 'BB', 'CC']) == 'MyClass.AA'

def test_empty_extensions_list():
    assert Strongest_Extension('MyClass', []) == 'MyClass.'

def test_single_extension():
    assert Strongest_Extension('MyClass', ['Extension']) == 'MyClass.Extension'

def test_empty_extension_in_list():
    assert Strongest_Extension('MyClass', ['', 'Extension']) == 'MyClass.'

def test_case_insensitive_extension_selection():
    assert Strongest_Extension('MyClass', ['extension', 'Extension']) == 'MyClass.Extension'

def test_long_extension_name():
    assert Strongest_Extension('MyClass', ['verylongextensionname', 'short']) == 'MyClass.verylongextensionname'

def test_numeric_class_name():
    assert Strongest_Extension('123', ['Extension']) == '123.Extension'

def test_numeric_extension_name():
    assert Strongest_Extension('MyClass', ['123', 'Extension']) == 'MyClass.123'

def test_mixed_case_class_and_extensions():
    assert Strongest_Extension('MyClAss', ['exTension', 'extension']) == 'MyClAss.exTension'

def test_none_class_name():
    assert Strongest_Extension(None, ['Extension']) == 'None.Extension'

def test_none_in_extensions_list():
    assert Strongest_Extension('MyClass', [None, 'Extension']) == 'MyClass.None'
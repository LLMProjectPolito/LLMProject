
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
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_empty_extensions_list():
    assert Strongest_Extension('my_class', []) == 'my_class.'

def test_comprehensive_case_sensitivity():
    assert Strongest_Extension('my_class', ['AAA', 'aaa', 'aA', 'Ab']) == 'my_class.AAA'

def test_single_extension():
    assert Strongest_Extension('my_class', ['Extension']) == 'my_class.Extension'

def test_extension_with_numbers():
    assert Strongest_Extension('my_class', ['Ext123', 'Extabc']) == 'my_class.Ext123'

def test_extension_with_special_characters():
    assert Strongest_Extension('my_class', ['Ext!@#', 'Extabc']) == 'my_class.Ext!@#'

def test_class_name_with_numbers():
    assert Strongest_Extension('Class123', ['ExtA', 'ExtB']) == 'Class123.ExtA'

def test_class_name_with_special_characters():
    assert Strongest_Extension('Class!@#', ['ExtA', 'ExtB']) == 'Class!@#.ExtA'

def test_empty_class_name():
    assert Strongest_Extension('', ['ExtA', 'ExtB']) == '.ExtA'

def test_long_extensions():
    assert Strongest_Extension('my_class', ['VeryLongExtensionWithManyCaps', 'short']) == 'my_class.VeryLongExtensionWithManyCaps'

# Consolidated tests for uppercase tie
def test_uppercase_tie():
    assert Strongest_Extension('my_class', ['Aa', 'aA']) == 'my_class.Aa'
    assert Strongest_Extension('my_class', ['abc', 'ABC']) == 'my_class.ABC'

# New test cases based on review
def test_equal_strength_empty_string():
    # Assuming first wins when empty string is present
    assert Strongest_Extension('my_class', ['', 'AA']) == 'my_class.AA'

def test_extensions_only_special_characters():
    assert Strongest_Extension('my_class', ['!@#', '%^&']) == 'my_class.!@#'

def test_class_name_only_special_characters():
    assert Strongest_Extension('!@#', ['ExtA', 'ExtB']) == '!@#.ExtA'

def test_large_number_of_extensions():
    extensions = ['Ext' + str(i) for i in range(1000)]
    assert Strongest_Extension('my_class', extensions) == 'my_class.Ext0'

def test_empty_string_extension_list():
    assert Strongest_Extension('my_class', ['']) == 'my_class.'

def test_multiple_extensions_same_strength():
    assert Strongest_Extension('my_class', ['Aa', 'aA', 'Bb', 'bB']) == 'my_class.Aa'

def test_lowercase_class_name():
    assert Strongest_Extension('myclass', ['ExtA', 'ExtB']) == 'myclass.ExtA'

def test_empty_and_valid_extensions():
    assert Strongest_Extension('my_class', ['', 'AA', 'bb']) == 'my_class.AA'

def test_only_empty_extensions():
    assert Strongest_Extension('my_class', ['', '', '']) == 'my_class.'
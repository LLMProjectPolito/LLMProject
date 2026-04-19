
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

def test_provided_example_1():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_provided_example_2():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_tie_breaking():
    # 'AA' strength: 2-0=2, 'BB' strength: 2-0=2. Should pick first.
    assert Strongest_Extension('Class', ['AA', 'BB']) == 'Class.AA'
    # 'aa' strength: 0-2=-2, 'bb' strength: 0-2=-2. Should pick first.
    assert Strongest_Extension('Class', ['aa', 'bb']) == 'Class.aa'

def test_all_uppercase():
    assert Strongest_Extension('Class', ['A', 'BB', 'CCC']) == 'Class.CCC'

def test_all_lowercase():
    # 'a' strength: -1, 'bb' strength: -2, 'ccc' strength: -3. Max is -1.
    assert Strongest_Extension('Class', ['a', 'bb', 'ccc']) == 'Class.a'

def test_mixed_strengths():
    # 'AbC' : 2-1 = 1
    # 'abc' : 0-3 = -3
    # 'ABC' : 3-0 = 3
    # 'aBc' : 1-2 = -1
    assert Strongest_Extension('MyClass', ['AbC', 'abc', 'ABC', 'aBc']) == 'MyClass.ABC'

def test_single_extension():
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_non_alphabetic_characters():
    # 'A1' : 1-0 = 1
    # 'a1' : 0-1 = -1
    # '123' : 0-0 = 0
    assert Strongest_Extension('Class', ['A1', 'a1', '123']) == 'Class.A1'
    assert Strongest_Extension('Class', ['123', '!!!']) == 'Class.123'

def test_empty_strings_in_list():
    # '' : 0-0 = 0
    # 'a' : 0-1 = -1
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'

def test_class_name_with_special_chars():
    assert Strongest_Extension('My_Class-123', ['ExtA', 'ExtB']) == 'My_Class-123.ExtA'
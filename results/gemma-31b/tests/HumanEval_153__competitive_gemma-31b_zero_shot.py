
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

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], 'Slices.SErviNGSliCes'),
    ("my_class", ['AA', 'Be', 'CC'], 'my_class.AA'),
    ("Test", ['abc', 'def'], 'Test.abc'),
    ("Test", ['ABC', 'DEF'], 'Test.ABC'),
    ("Test", ['a', 'B', 'CC'], 'Test.CC'),
    ("Test", ['a', 'B', 'A'], 'Test.B'),
    ("Test", ['lowercase', 'UPPERCASE'], 'Test.UPPERCASE'),
    ("Test", ['MixedCase', 'ALLCAPS', 'alllower'], 'Test.ALLCAPS'),
    ("Test", [''], 'Test.'),
    ("Test", ['A1b', 'A2B'], 'Test.A2B'),
    ("Test", ['!@#', '123'], 'Test.!@#'),
    ("Test", ['aB', 'Ab'], 'Test.aB'),
])
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_single_extension():
    assert Strongest_Extension("Class", ["OnlyOne"]) == "Class.OnlyOne"

def test_all_same_strength():
    # All have strength 0
    assert Strongest_Extension("Class", ["Ab", "Cd", "Ef"]) == "Class.Ab"

def test_negative_strengths():
    # 'a' = -1, 'aa' = -2, 'aaa' = -3
    assert Strongest_Extension("Class", ["aaa", "aa", "a"]) == "Class.a"
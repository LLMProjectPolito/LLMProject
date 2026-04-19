
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
    ("Test", ['a', 'B', 'C'], 'Test.B'),
    ("Test", ['abc', 'def'], 'Test.abc'),
    ("Test", ['ABC', 'DEF'], 'Test.ABC'),
    ("Test", ['aB', 'Ab'], 'Test.aB'),
    ("Test", ['A1', 'B2'], 'Test.A1'),
    ("Test", ['123', '456'], 'Test.123'),
    ("Class", ['lowercase', 'UPPERCASE', 'MixedCase'], 'Class.UPPERCASE'),
    ("Class", ['MixedCase', 'UPPERCASE', 'lowercase'], 'Class.UPPERCASE'),
    ("Class", ['MixedCase', 'AnotherMixed'], 'Class.MixedCase'),
    ("Class", [''], 'Class.'),
    ("Class", ['A', 'aa', 'AAA'], 'Class.AAA'),
])
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_single_extension():
    assert Strongest_Extension("Single", ["OnlyOne"]) == "Single.OnlyOne"

def test_all_lowercase():
    # strength: -3, -2, -4
    assert Strongest_Extension("Low", ["abc", "de", "fghi"]) == "Low.de"

def test_all_uppercase():
    # strength: 3, 2, 4
    assert Strongest_Extension("High", ["ABC", "DE", "FGHI"]) == "High.FGHI"

def test_non_alpha_characters():
    # 'A1!' -> CAP: 1, SM: 0 -> 1
    # 'b2!' -> CAP: 0, SM: 1 -> -1
    # 'C3!' -> CAP: 1, SM: 0 -> 1
    assert Strongest_Extension("Symbols", ["A1!", "b2!", "C3!"]) == "Symbols.A1!"
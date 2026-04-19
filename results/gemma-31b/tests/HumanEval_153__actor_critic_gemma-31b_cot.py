
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

def test_strongest_extension_basic():
    """Test the basic example provided in the problem description."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_all_uppercase():
    """Test extensions that are all uppercase."""
    # AAA: 3, BB: 2, C: 1
    assert Strongest_Extension('Class', ['AAA', 'BB', 'C']) == 'Class.AAA'

def test_strongest_extension_all_lowercase():
    """Test extensions that are all lowercase (negative strengths)."""
    # a: -1, ab: -2, abc: -3. Max is -1.
    assert Strongest_Extension('Class', ['a', 'ab', 'abc']) == 'Class.a'

def test_strongest_extension_mixed_strengths():
    """Test a variety of strengths including positive, zero, and negative."""
    # 'A': 1-0=1
    # 'Ab': 1-1=0
    # 'ab': 0-2=-2
    # 'ABC': 3-0=3
    assert Strongest_Extension('Test', ['A', 'Ab', 'ab', 'ABC']) == 'Test.ABC'

def test_strongest_extension_single_element():
    """Test when only one extension is provided."""
    assert Strongest_Extension('OnlyOne', ['Extension']) == 'OnlyOne.Extension'

def test_strongest_extension_empty_string_extension():
    """Test when an extension is an empty string (strength 0)."""
    # '': 0-0=0, 'a': 0-1=-1
    assert Strongest_Extension('Empty', ['', 'a']) == 'Empty.'
    # 'a': 0-1=-1, '': 0-0=0
    assert Strongest_Extension('Empty', ['a', '']) == 'Empty.'

def test_strongest_extension_non_alphabetic():
    """Test extensions containing numbers or symbols (should not count towards CAP or SM)."""
    # 'A1': 1-0=1
    # 'a1': 0-1=-1
    # '123': 0-0=0
    # 'A!a': 1-1=0
    assert Strongest_Extension('Symbols', ['A1', 'a1', '123', 'A!a']) == 'Symbols.A1'

def test_strongest_extension_empty_list():
    """Test when the extensions list is empty to ensure no ValueError is raised."""
    # Depending on implementation, this should return the class name or handle gracefully.
    assert Strongest_Extension('EmptyList', []) == 'EmptyList'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("MyClass", ["Strong", "Stronger"], "MyClass.Strong"), # Strong: 1-5=-4, Stronger: 1-7=-6
    ("MyClass", ["strong", "stronger"], "MyClass.strong"), # strong: 0-6=-6, stronger: 0-8=-8
    ("my_class", ["AA", "CC"], "my_class.AA"),             # Tie (2 vs 2): first wins
    ("Case", ["aB", "Ab"], "Case.aB"),                     # Tie (0 vs 0): first wins
    ("MyClass", ["", ""], "MyClass."),                     # Tie (0 vs 0): first wins
])
def test_strongest_extension_parametrized(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
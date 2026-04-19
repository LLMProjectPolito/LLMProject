
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
    """
    if not extensions:
        return class_name

    max_strength = -float('inf')
    best_ext = None

    for ext in extensions:
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        strength = cap - sm
        
        # Use strictly greater than to ensure the first occurrence is kept in case of a tie
        if strength > max_strength:
            max_strength = strength
            best_ext = ext
            
    return f"{class_name}.{best_ext}"

def test_strongest_extension_basic():
    """Test the basic functionality provided in the example."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_tie_breaker():
    """Test that the first extension is chosen when strengths are equal."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_uppercase():
    """Test cases where extensions are all uppercase (high strength)."""
    assert Strongest_Extension('Base', ['AAA', 'BB']) == 'Base.AAA'
    assert Strongest_Extension('Base', ['B', 'AAA']) == 'Base.AAA'

def test_strongest_extension_all_lowercase():
    """Test cases where extensions are all lowercase (low strength)."""
    # 'abc' = 0-3 = -3, 'de' = 0-2 = -2. -2 is stronger than -3.
    assert Strongest_Extension('Base', ['abc', 'de']) == 'Base.de'
    # 'abc' = 0-3 = -3, 'a' = 0-1 = -1. -1 is stronger than -3.
    assert Strongest_Extension('Base', ['abc', 'a']) == 'Base.a'

def test_strongest_extension_mixed_case():
    """Test extensions with varying mixed case strengths."""
    # 'AbC' = 2-1 = 1
    # 'abc' = 0-3 = -3
    # 'ABC' = 3-0 = 3
    assert Strongest_Extension('Class', ['AbC', 'abc', 'ABC']) == 'Class.ABC'

def test_strongest_extension_single_element():
    """Test when only one extension is provided."""
    assert Strongest_Extension('MyClass', ['OnlyOne']) == 'MyClass.OnlyOne'

def test_strongest_extension_non_alphabetic():
    """Test how the function handles non-alphabetic characters (should be ignored)."""
    # '123' = 0-0 = 0
    # '!!!' = 0-0 = 0
    # 'A1' = 1-0 = 1
    assert Strongest_Extension('Test', ['123', '!!!', 'A1']) == 'Test.A1'
    assert Strongest_Extension('Test', ['123', '!!!']) == 'Test.123'

def test_strongest_extension_empty_strings():
    """Test extensions that are empty strings."""
    # '' = 0-0 = 0
    # 'a' = 0-1 = -1
    assert Strongest_Extension('Test', ['', 'a']) == 'Test.'
    assert Strongest_Extension('Test', ['a', '']) == 'Test.'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
    ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
    ("Test", ['a', 'b', 'c'], "Test.a"),
    ("Test", ['Z', 'Y', 'X'], "Test.Z"),
    ("App", ['Low', 'HIGH', 'Medium'], "App.HIGH"),
])
def test_parameterized_cases(class_name, extensions, expected):
    """Run a set of parameterized test cases for efficiency."""
    assert Strongest_Extension(class_name, extensions) == expected
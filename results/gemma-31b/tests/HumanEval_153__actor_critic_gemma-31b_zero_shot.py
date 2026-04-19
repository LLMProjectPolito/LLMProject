
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
    """
    Finds the strongest extension based on the difference between 
    uppercase and lowercase letters.
    """
    if not extensions:
        return class_name

    def get_strength(ext):
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        return cap - sm

    # Use max with a key. Python's max() is stable, 
    # meaning it returns the first occurrence in case of ties.
    strongest = max(extensions, key=get_strength)
    return f"{class_name}.{strongest}"

# --- Pytest Suite ---

@pytest.mark.parametrize("class_name, extensions, expected", [
    # Provided Example 1
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], 'Slices.SErviNGSliCes'),
    # Provided Example 2
    ('my_class', ['AA', 'Be', 'CC'], 'my_class.AA'),
    # Tie-breaking: Should pick the first one in the list
    ('TestClass', ['ABC', 'DEF'], 'TestClass.ABC'),
    ('TestClass', ['abc', 'def'], 'TestClass.abc'),
    # All uppercase (Strength = length)
    ('Class', ['A', 'BB', 'CCC'], 'Class.CCC'),
    # All lowercase (Strength = -length)
    ('Class', ['a', 'bb', 'ccc'], 'Class.a'),
    # Mixed case with clear winner
    ('MyClass', ['aB', 'AB', 'ab'], 'MyClass.AB'),
    # Single extension in list
    ('Single', ['OnlyOne'], 'Single.OnlyOne'),
    # Extensions with non-alphabetic characters (should be ignored in counts)
    ('Special', ['A1b', 'A2b', 'A3b'], 'Special.A1b'),
    ('Special', ['A1B', 'a1b'], 'Special.A1B'),
    # Very long strings
    ('Long', ['A' * 100, 'a' * 100], 'Long.' + 'A' * 100),
])
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_empty_extensions_list():
    """
    Test behavior when the extensions list is empty.
    Expected behavior: Return only the class_name.
    """
    assert Strongest_Extension('MyClass', []) == 'MyClass'

def test_empty_extension_string():
    """Test behavior when an extension is an empty string."""
    # Empty string: CAP=0, SM=0, Strength=0
    # 'a' has strength -1. Empty string should win.
    assert Strongest_Extension('Test', ['', 'a']) == 'Test.'

def test_case_sensitivity_of_class_name():
    """Ensure the class_name is returned exactly as provided."""
    assert Strongest_Extension('my_CLASS_name', ['AA']) == 'my_CLASS_name.AA'

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
    Implementation of the function to be tested.
    """
    if not extensions:
        return ""
    
    max_strength = float('-inf')
    strongest_ext = ""

    for ext in extensions:
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        strength = cap - sm
        
        # We use '>' instead of '>=' to ensure that in case of a tie, 
        # the first occurrence in the list is preserved.
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
            
    return f"{class_name}.{strongest_ext}"

# --- Pytest Suite ---

def test_example_from_docstring():
    """Tests the specific example provided in the problem description."""
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_tie_breaking_rule():
    """Tests that if strengths are equal, the first one in the list is chosen."""
    # 'AA' strength: 2-0 = 2
    # 'Be' strength: 1-1 = 0
    # 'CC' strength: 2-0 = 2
    # 'AA' and 'CC' tie, 'AA' comes first.
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_all_negative_strengths():
    """Tests cases where all extensions have more lowercase than uppercase letters."""
    # 'abc' -> 0-3 = -3
    # 'def' -> 0-3 = -3
    # 'gh'  -> 0-2 = -2
    assert Strongest_Extension('Test', ['abc', 'def', 'gh']) == 'Test.gh'
    assert Strongest_Extension('Test', ['abc', 'def']) == 'Test.abc'

def test_zero_strength():
    """Tests cases where strength is exactly zero."""
    # 'Ab' -> 1-1 = 0
    # 'aB' -> 1-1 = 0
    assert Strongest_Extension('Test', ['Ab', 'aB']) == 'Test.Ab'
    # '123' -> 0-0 = 0
    assert Strongest_Extension('Test', ['123', 'a']) == 'Test.123'

def test_single_extension():
    """Tests the function with a list containing only one extension."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'
    assert Strongest_Extension('Class', ['onlyone']) == 'Class.onlyone'

def test_non_alphabetic_characters():
    """Tests that non-alphabetic characters do not contribute to CAP or SM."""
    # 'A1!' -> CAP=1, SM=0, Strength=1
    # 'a2@' -> CAP=0, SM=1, Strength=-1
    assert Strongest_Extension('Class', ['A1!', 'a2@']) == 'Class.A1!'
    # '!!!' -> CAP=0, SM=0, Strength=0
    assert Strongest_Extension('Class', ['!!!', 'a']) == 'Class.!!!'

def test_all_uppercase_and_all_lowercase():
    """Tests extreme cases of casing."""
    assert Strongest_Extension('Class', ['ABC', 'DEF']) == 'Class.ABC'
    assert Strongest_Extension('Class', ['abc', 'def']) == 'Class.abc'

def test_empty_string_extension():
    """
    Tests behavior when an extension is an empty string.
    Note: This returns 'Class.' which is distinct from the empty list return.
    """
    # '' -> CAP=0, SM=0, Strength=0
    # 'a' -> CAP=0, SM=1, Strength=-1
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'
    # 'a' -> -1
    # '' -> 0
    assert Strongest_Extension('Class', ['a', '']) == 'Class.'

def test_class_name_with_special_characters():
    """Tests that the class_name itself is handled correctly regardless of content."""
    assert Strongest_Extension('My-Class_123', ['Ext']) == 'My-Class_123.Ext'

def test_empty_extensions_list():
    """
    Tests the guard clause for an empty extensions list.
    Should return an empty string "".
    """
    assert Strongest_Extension("AnyClass", []) == ""

def test_empty_class_name():
    """Tests behavior when class_name is an empty string."""
    # Should return ".Extension"
    assert Strongest_Extension("", ["Ext"]) == ".Ext"

def test_unicode_characters():
    """Tests that Unicode/International characters are handled correctly by isupper/islower."""
    # 'É' is upper, 'ç' is lower.
    # 'É' strength: 1 - 0 = 1
    # 'ç' strength: 0 - 1 = -1
    assert Strongest_Extension("Class", ["É", "ç"]) == "Class.É"
    
    # 'Ä' (upper), 'ä' (lower)
    # 'Ää' strength: 1 - 1 = 0
    # 'B' strength: 1 - 0 = 1
    assert Strongest_Extension("Class", ["Ää", "B"]) == "Class.B"
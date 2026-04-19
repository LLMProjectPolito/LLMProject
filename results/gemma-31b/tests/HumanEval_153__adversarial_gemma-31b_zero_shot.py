
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
        return None
    
    def get_strength(ext):
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        return cap - sm

    max_strength = float('-inf')
    best_ext = None

    for ext in extensions:
        strength = get_strength(ext)
        if strength > max_strength:
            max_strength = strength
            best_ext = ext
            
    return f"{class_name}.{best_ext}"

# --- Pytest Suite ---

def test_provided_example_1():
    """Test the primary example provided in the docstring."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_provided_example_2():
    """Test the second example provided in the docstring (tie-breaking)."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_all_uppercase():
    """Test extensions that are entirely uppercase."""
    assert Strongest_Extension('Base', ['A', 'BB', 'CCC']) == 'Base.CCC'

def test_all_lowercase():
    """Test extensions that are entirely lowercase (negative strengths)."""
    # 'a' = -1, 'bb' = -2, 'ccc' = -3. Max is -1.
    assert Strongest_Extension('Base', ['a', 'bb', 'ccc']) == 'Base.a'

def test_mixed_case_tie():
    """Test that the first occurrence is chosen when strengths are equal."""
    # 'Ab' = 1-1 = 0
    # 'Cd' = 1-1 = 0
    # 'Ef' = 1-1 = 0
    assert Strongest_Extension('Class', ['Ab', 'Cd', 'Ef']) == 'Class.Ab'

def test_non_alphabetic_characters():
    """Test that numbers and symbols are ignored in strength calculation."""
    # 'A1' = 1-0 = 1
    # 'a2' = 0-1 = -1
    # '!!' = 0-0 = 0
    assert Strongest_Extension('Class', ['a2', '!!', 'A1']) == 'Class.A1'

def test_single_extension():
    """Test behavior with only one extension in the list."""
    assert Strongest_Extension('Class', ['OnlyOne']) == 'Class.OnlyOne'

def test_empty_extensions_list():
    """Test behavior when the extensions list is empty."""
    # Depending on requirements, this could return None or raise an error.
    # Based on the implementation provided above, it returns None.
    assert Strongest_Extension('Class', []) is None

def test_extreme_strength_difference():
    """Test with very high and very low strength values."""
    assert Strongest_Extension('Class', ['aaaaaaaaaa', 'AAAAAAAAAA']) == 'Class.AAAAAAAAAA'

def test_class_name_with_special_chars():
    """Test that the class name is preserved exactly as passed."""
    assert Strongest_Extension('My_Class-123', ['ExtA', 'ExtB']) == 'My_Class-123.ExtA'

def test_empty_strings_as_extensions():
    """Test extensions that are empty strings."""
    # Empty string: CAP=0, SM=0, Strength=0.
    # 'a' = -1. Empty string should win.
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'
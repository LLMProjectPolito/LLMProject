
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
    Finds the extension with the highest strength (Uppercase count - Lowercase count).
    In case of a tie, the first extension in the list is returned.
    
    Returns:
        str: Format "ClassName.StrongestExtensionName"
    """
    def get_strength(ext):
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        return cap - sm

    # max() in Python is stable; it returns the first occurrence in case of ties.
    strongest = max(extensions, key=get_strength)
    return f"{class_name}.{strongest}"

# --- Superior Pytest Suite ---

@pytest.mark.parametrize("class_name, extensions, expected", [
    # Basic case from prompt
    ('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'], 'Slices.SErviNGSliCes'),
    
    # Tie-breaking: AA (2-0=2) and CC (2-0=2). First one wins.
    ('my_class', ['AA', 'Be', 'CC'], 'my_class.AA'),
    
    # All lowercase: strengths are negative. 'a' (-1) is stronger than 'abc' (-3).
    ('Test', ['a', 'ab', 'abc'], 'Test.a'),
    
    # All uppercase: strengths are positive. 'ABC' (3) is strongest.
    ('Test', ['A', 'AB', 'ABC'], 'Test.ABC'),
    
    # Single element list
    ('Single', ['OnlyOne'], 'Single.OnlyOne'),
    
    # Non-alphabetic characters: ignored in strength calculation.
    # 'A1' (1-0=1), 'a1' (0-1=-1), '11' (0-0=0).
    ('Numbers', ['A1', 'a1', '11'], 'Numbers.A1'),
    
    # Empty strings: '' (0-0=0) is stronger than 'a' (0-1=-1).
    ('Empty', ['', 'a'], 'Empty.'),
    
    # Exact zero strength tie: 'Ab' (1-1=0) and 'Cd' (1-1=0).
    ('Zero', ['Ab', 'Cd'], 'Zero.Ab'),
    
    # Complex mix of lengths and cases
    # low: -3, HIGH: 4, MixedCase: 2-7=-5, A: 1
    ('Test', ['low', 'HIGH', 'MixedCase', 'A'], 'Test.HIGH'),
    
    # Edge case: empty class name
    ('', ['Extension'], '.Extension'),
])
def test_strongest_extension_scenarios(class_name, extensions, expected):
    """Tests various scenarios including ties, negative strengths, and non-alpha chars."""
    assert Strongest_Extension(class_name, extensions) == expected

def test_strongest_extension_empty_list():
    """Tests that the function raises a ValueError when provided an empty extensions list."""
    with pytest.raises(ValueError):
        Strongest_Extension('Class', [])
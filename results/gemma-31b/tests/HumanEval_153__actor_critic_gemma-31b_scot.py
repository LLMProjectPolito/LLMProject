
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

# The function Strongest_Extension is assumed to be defined in the environment.

def test_provided_examples():
    """Test the examples provided in the problem description."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_tie_breaking():
    """
    Verify that the first extension is chosen in case of a tie in strength.
    Covers positive, negative, and zero strength ties.
    """
    # Positive tie: 'AAA'(3), 'BBB'(3), 'CCC'(3) -> Pick first
    assert Strongest_Extension('Base', ['AAA', 'BBB', 'CCC']) == 'Base.AAA'
    
    # Negative tie: 'a'( -1), 'b'(-1), 'c'(-1) -> Pick first
    assert Strongest_Extension('Base', ['a', 'b', 'c']) == 'Base.a'
    
    # Zero tie (mixed case): 'aB'(0), 'Ab'(0) -> Pick first
    assert Strongest_Extension('Base', ['aB', 'Ab']) == 'Base.aB'
    
    # Zero tie (non-alphabetic): '123'(0), '!!!'(0), '456'(0) -> Pick first
    assert Strongest_Extension('Base', ['123', '!!!', '456']) == 'Base.123'

def test_non_alphabetic_characters():
    """Ensure that numbers and symbols do not count towards CAP or SM."""
    # 'A123' strength: 1-0 = 1; 'a123' strength: 0-1 = -1; '!!!' strength: 0-0 = 0
    assert Strongest_Extension('Class', ['a123', '!!!', 'A123']) == 'Class.A123'
    # 'A!a' strength: 1-1 = 0; 'B!!' strength: 1-0 = 1
    assert Strongest_Extension('Class', ['A!a', 'B!!']) == 'Class.B!!'

def test_all_uppercase_vs_all_lowercase():
    """Verify that all-caps strings are stronger than all-lowercase strings."""
    assert Strongest_Extension('Test', ['lowercase', 'UPPERCASE']) == 'Test.UPPERCASE'
    assert Strongest_Extension('Test', ['UPPERCASE', 'lowercase']) == 'Test.UPPERCASE'

def test_single_extension():
    """Verify behavior when only one extension is provided."""
    assert Strongest_Extension('Single', ['OnlyOne']) == 'Single.OnlyOne'

def test_negative_strengths():
    """Ensure the function correctly identifies the maximum even if all strengths are negative."""
    # 'abcde' strength: -5, 'abcdE' strength: -3, 'abcDE' strength: -1
    assert Strongest_Extension('Neg', ['abcde', 'abcdE', 'abcDE']) == 'Neg.abcDE'

def test_empty_strings_in_list():
    """
    Check behavior when extensions include empty strings.
    An empty string has strength 0.
    """
    # '' strength: 0, 'a' strength: -1 -> '' wins
    assert Strongest_Extension('Empty', ['', 'a']) == 'Empty.'
    # 'A' strength: 1, '' strength: 0 -> 'A' wins
    assert Strongest_Extension('Empty', ['A', '']) == 'Empty.A'

def test_empty_extensions_list():
    """
    Verify how the function handles an empty extensions list.
    Since no extension exists to append, it should return the class_name without a dot.
    """
    assert Strongest_Extension('Base', []) == 'Base'

def test_empty_class_name():
    """Verify that an empty class_name is handled correctly."""
    # Result should be '.Extension'
    assert Strongest_Extension('', ['A']) == '.A'
    assert Strongest_Extension('', ['a', 'B']) == '.B'

def test_whitespace_extensions():
    """Verify that whitespace is treated as non-alphabetic (strength 0)."""
    # ' ' strength: 0, 'a' strength: -1 -> ' ' wins
    assert Strongest_Extension('Base', [' ', 'a']) == 'Base. '
    # 'A' strength: 1, ' ' strength: 0 -> 'A' wins
    assert Strongest_Extension('Base', ['A', ' ']) == 'Base.A'
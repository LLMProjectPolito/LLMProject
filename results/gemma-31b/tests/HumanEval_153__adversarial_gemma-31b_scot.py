
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

# The function is provided in the problem description; 
# we are testing it as a Black Box.

def test_provided_examples():
    """Test the examples explicitly mentioned in the docstring."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_tie_breaking():
    """Verify that the first extension is chosen in case of a tie in strength."""
    # 'AAA' strength: 3-0 = 3
    # 'BBB' strength: 3-0 = 3
    # 'CCC' strength: 3-0 = 3
    assert Strongest_Extension('TestClass', ['AAA', 'BBB', 'CCC']) == 'TestClass.AAA'
    
    # 'Ab' strength: 1-1 = 0
    # 'Cd' strength: 1-1 = 0
    assert Strongest_Extension('TestClass', ['Ab', 'Cd']) == 'TestClass.Ab'

def test_all_uppercase_and_lowercase():
    """Test extensions consisting entirely of one case."""
    # 'UPPER' strength: 5-0 = 5
    # 'lower' strength: 0-5 = -5
    assert Strongest_Extension('CaseClass', ['lower', 'UPPER']) == 'CaseClass.UPPER'
    assert Strongest_Extension('CaseClass', ['lower', 'evenlower']) == 'CaseClass.lower' # -5 vs -8

def test_non_alphabetic_characters():
    """Verify that numbers and symbols are ignored in strength calculation."""
    # 'A123' strength: 1-0 = 1
    # 'a123' strength: 0-1 = -1
    # '!!!' strength: 0-0 = 0
    assert Strongest_Extension('SymClass', ['a123', '!!!', 'A123']) == 'SymClass.A123'
    # 'A!a' strength: 1-1 = 0
    # 'B!b' strength: 1-1 = 0
    assert Strongest_Extension('SymClass', ['A!a', 'B!b']) == 'SymClass.A!a'

def test_single_extension():
    """Test the function with only one extension provided."""
    assert Strongest_Extension('Single', ['OnlyOne']) == 'Single.OnlyOne'

def test_negative_strengths():
    """Ensure the logic works when all strengths are negative."""
    # 'abc' strength: 0-3 = -3
    # 'abcd' strength: 0-4 = -4
    # 'abce' strength: 0-4 = -4
    assert Strongest_Extension('NegClass', ['abc', 'abcd', 'abce']) == 'NegClass.abc'

def test_mixed_case_complex():
    """Test a more complex mix of cases."""
    # 'PyTest' -> 2-4 = -2
    # 'PYTEST' -> 6-0 = 6
    # 'pytest' -> 0-6 = -6
    # 'PyT' -> 2-1 = 1
    extensions = ['PyTest', 'PYTEST', 'pytest', 'PyT']
    assert Strongest_Extension('Complex', extensions) == 'Complex.PYTEST'

def test_empty_extensions_list():
    """
    Test behavior with an empty list. 
    Depending on implementation, this might raise a ValueError or return something else.
    We test to document the current behavior.
    """
    with pytest.raises((ValueError, IndexError)):
        Strongest_Extension('Empty', [])
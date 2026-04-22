
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

def test_provided_examples():
    """Tests the specific examples provided in the problem description."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_tie_breaking():
    """Tests that the first extension is chosen in case of a tie."""
    # All have strength 0: 'Ab' (1-1), 'Cd' (1-1), 'Ef' (1-1)
    assert Strongest_Extension('Test', ['Ab', 'Cd', 'Ef']) == 'Test.Ab'
    # All have strength 2: 'AA' (2-0), 'BB' (2-0)
    assert Strongest_Extension('Test', ['AA', 'BB']) == 'Test.AA'

def test_negative_strengths():
    """Tests scenarios where all extensions result in negative strength."""
    # 'abc' -> 0-3 = -3
    # 'aBc' -> 1-2 = -1
    # 'abC' -> 1-2 = -1
    # Strongest is -1. Tie between 'aBc' and 'abC', pick first.
    assert Strongest_Extension('Class', ['abc', 'aBc', 'abC']) == 'Class.aBc'
    
    # 'aaaa' -> -4
    # 'bb' -> -2
    # Strongest is -2
    assert Strongest_Extension('Class', ['aaaa', 'bb']) == 'Class.bb'

def test_all_uppercase_and_lowercase():
    """Tests extreme cases of character casing."""
    # All uppercase
    assert Strongest_Extension('Class', ['A', 'BBB', 'CC']) == 'Class.BBB'
    # All lowercase
    assert Strongest_Extension('Class', ['a', 'bbb', 'cc']) == 'Class.a'

def test_non_alphabetic_characters():
    """Tests that numbers and symbols are ignored in strength calculation."""
    # 'A1!' -> CAP=1, SM=0 -> Strength 1
    # 'B2@' -> CAP=1, SM=0 -> Strength 1
    # 'c3#' -> CAP=0, SM=1 -> Strength -1
    assert Strongest_Extension('Class', ['A1!', 'B2@', 'c3#']) == 'Class.A1!'
    
    # 'A_B_C' -> CAP=3, SM=0 -> Strength 3
    # 'abc' -> CAP=0, SM=3 -> Strength -3
    assert Strongest_Extension('Class', ['abc', 'A_B_C']) == 'Class.A_B_C'

def test_single_extension():
    """Tests the function with a list containing only one extension."""
    assert Strongest_Extension('Solo', ['OnlyOne']) == 'Solo.OnlyOne'
    assert Strongest_Extension('Solo', ['onlyone']) == 'Solo.onlyone'

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("User", ["Admin", "guest", "SUPER"], "User.SUPER"),
    ("Data", ["x", "Y", "z"], "Data.Y"),
    ("Empty", ["", "A", "b"], "Empty.A"),
])
def test_parameterized_scenarios(class_name, extensions, expected):
    """Parameterized test for various common scenarios."""
    assert Strongest_Extension(class_name, extensions) == expected
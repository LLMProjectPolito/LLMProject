
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

def test_strongest_extension_provided_example_1():
    """Tests the specific example provided in the docstring."""
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_provided_example_2():
    """Tests the tie-breaking example provided in the docstring."""
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_negative():
    """Tests when all extensions have negative strength (more lowercase than uppercase)."""
    # 'abc': 0-3 = -3
    # 'aB': 1-1 = 0
    # 'Abc': 1-2 = -1
    # Max is 0
    assert Strongest_Extension('Base', ['abc', 'aB', 'Abc']) == 'Base.aB'

def test_strongest_extension_zero_strength():
    """Tests when extensions have zero strength (equal upper and lower)."""
    # 'Ab': 1-1 = 0
    # 'Cd': 1-1 = 0
    # 'Ef': 1-1 = 0
    # Should return the first one
    assert Strongest_Extension('Test', ['Ab', 'Cd', 'Ef']) == 'Test.Ab'

def test_strongest_extension_single_element():
    """Tests a list containing only one extension."""
    assert Strongest_Extension('Single', ['OnlyOne']) == 'Single.OnlyOne'

def test_strongest_extension_with_non_alphabetic():
    """Tests that numbers and symbols do not affect the strength calculation."""
    # 'A1!': CAP=1, SM=0 -> Strength 1
    # 'a2@': CAP=0, SM=1 -> Strength -1
    assert Strongest_Extension('Class', ['A1!', 'a2@']) == 'Class.A1!'

def test_strongest_extension_class_name_formatting():
    """Ensures the class name is preserved exactly as provided, including underscores."""
    assert Strongest_Extension('my_complex_class_name', ['Ext']) == 'my_complex_class_name.Ext'

def test_strongest_extension_empty_base_name():
    """Tests behavior when the base_name is an empty string."""
    assert Strongest_Extension('', ['Ext']) == '.Ext'

def test_strongest_extension_empty_list():
    """Tests behavior when the extensions list is empty. 
    Expected to raise ValueError as per standard Python max() behavior on empty sequences.
    """
    with pytest.raises(ValueError):
        Strongest_Extension('Base', [])

def test_strongest_extension_empty_strings():
    """Tests behavior when extensions contain empty strings."""
    # '' : 0-0 = 0
    # 'a' : 0-1 = -1
    assert Strongest_Extension('Class', ['', 'a']) == 'Class.'

def test_strongest_extension_only_non_alphabetic():
    """Tests a list containing only non-alphabetic characters (all strength 0)."""
    # '123': 0-0 = 0
    # '!!!': 0-0 = 0
    # Should return the first one
    assert Strongest_Extension('Class', ['123', '!!!']) == 'Class.123'

def test_strongest_extension_invalid_inputs():
    """Tests behavior when input types are invalid."""
    # Testing invalid base_name types
    with pytest.raises(TypeError):
        Strongest_Extension(None, ['Ext'])
    with pytest.raises(TypeError):
        Strongest_Extension(123, ['Ext'])
    
    # Testing invalid extensions argument
    with pytest.raises(TypeError):
        Strongest_Extension('Class', None)
    
    # Testing non-string elements within the extensions list
    with pytest.raises(TypeError):
        Strongest_Extension('Class', [123, 'A'])
    
    # Testing None within the extensions list
    with pytest.raises(TypeError):
        Strongest_Extension('Class', ['A', None, 'B'])
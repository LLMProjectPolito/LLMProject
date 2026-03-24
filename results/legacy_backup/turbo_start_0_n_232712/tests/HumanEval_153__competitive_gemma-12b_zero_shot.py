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
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    strongest_extension = ""
    max_strength = float('-inf')
    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for char in extension:
            if char.isupper():
                cap_count += 1
            elif char.islower():
                sm_count += 1
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + "." + strongest_extension

def test_Strongest_Extension_basic():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_Strongest_Extension_example():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_Strongest_Extension_same_strength():
    assert Strongest_Extension('Test', ['AA', 'BB', 'CC']) == 'Test.AA'

def test_Strongest_Extension_empty_extensions():
    assert Strongest_Extension('Class', []) == 'Class.'

def test_Strongest_Extension_all_uppercase():
    assert Strongest_Extension('Class', ['AAAA', 'BBB', 'CCCC']) == 'Class.AAAA'

def test_Strongest_Extension_all_lowercase():
    assert Strongest_Extension('Class', ['aaaa', 'bbbb', 'cccc']) == 'Class.aaaa'

def test_Strongest_Extension_mixed_case():
    assert Strongest_Extension('Class', ['aA', 'bB', 'cC']) == 'Class.aA'

def test_Strongest_Extension_with_numbers():
    assert Strongest_Extension('Class', ['A1', 'B2', 'C3']) == 'Class.A1'

def test_Strongest_Extension_with_symbols():
    assert Strongest_Extension('Class', ['A!', 'B@', 'C#']) == 'Class.A!'

def test_Strongest_Extension_longer_extensions():
    assert Strongest_Extension('Class', ['LongExtension1', 'LongExtension2', 'LongExtension3']) == 'Class.LongExtension1'

def test_Strongest_Extension_negative_strength():
    assert Strongest_Extension('Class', ['aaaaA', 'bbbbb', 'ccccc']) == 'Class.bbbbb'

def test_Strongest_Extension_zero_strength():
    assert Strongest_Extension('Class', ['Aa', 'Bb', 'Cc']) == 'Class.Aa'
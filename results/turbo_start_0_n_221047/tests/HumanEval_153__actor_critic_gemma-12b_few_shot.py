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
    strongest_extension = None
    max_strength = float('-inf')

    if not extensions:
        return ""  # Handle empty list case - return empty string

    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap_count += 1
            elif 'a' <= char <= 'z':
                sm_count += 1
        
        strength = cap_count - sm_count
        
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


### Tests (Pytest):
def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_example():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_list():
    assert Strongest_Extension('my_class', []) == ""

def test_strongest_extension_tie():
    assert Strongest_Extension('my_class', ['AA', 'BB', 'CC']) == 'my_class.AA'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('my_class', ['AAAA', 'BBB', 'CCCC']) == 'my_class.AAAA'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('my_class', ['aaaa', 'bbbb', 'cccc']) == 'my_class.aaaa'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('my_class', ['aA', 'bB', 'cC']) == 'my_class.aA'

def test_strongest_extension_negative_strength():
    assert Strongest_Extension('my_class', ['abc', 'def', 'ghi']) == 'my_class.abc'

def test_strongest_extension_same_strength_different_lengths():
    assert Strongest_Extension('my_class', ['A', 'AA', 'AAA']) == 'my_class.A'

def test_strongest_extension_zero_strength():
    assert Strongest_Extension('my_class', ['aaaa', 'bbbb', 'cccc']) == 'my_class.aaaa'

def test_strongest_extension_numbers_special_chars():
    assert Strongest_Extension('my_class', ['A1', 'B2', 'C!']) == 'my_class.A1'

def test_strongest_extension_class_name_special_chars():
    assert Strongest_Extension('my class!', ['AA', 'Be', 'CC']) == 'my class!.AA'
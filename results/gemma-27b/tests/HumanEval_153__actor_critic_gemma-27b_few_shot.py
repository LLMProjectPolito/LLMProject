
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
    Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    strongest_extension = None
    max_strength = float('-inf')

    if not extensions:
        return f"{class_name}.None"

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

    return f"{class_name}.{strongest_extension}"

### Tests (Pytest):
import pytest

def test_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_tie():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_empty_extensions():
    assert Strongest_Extension('my_class', []) == 'my_class.None'

def test_none_class_name():
    assert Strongest_Extension(None, ['AA', 'Be', 'CC']) == 'None.AA'

def test_all_uppercase():
    assert Strongest_Extension('Class', ['AAA', 'BBB', 'CCC']) == 'Class.AAA'

def test_all_lowercase():
    assert Strongest_Extension('Class', ['aaa', 'bbb', 'ccc']) == 'Class.aaa'

def test_mixed_case():
    assert Strongest_Extension('Class', ['aA', 'Bb', 'Cc']) == 'Class.aA'

def test_with_non_alphabetic():
    assert Strongest_Extension('Class', ['A1', 'b2', 'C3']) == 'Class.A1'

def test_empty_string_extension():
    assert Strongest_Extension('Class', ['A', '', 'B']) == 'Class.A'

def test_same_strength_different_order():
    assert Strongest_Extension('Class', ['AB', 'BA']) == 'Class.AB'
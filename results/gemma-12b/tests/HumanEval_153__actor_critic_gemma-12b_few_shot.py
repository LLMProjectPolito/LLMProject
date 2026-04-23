
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
    if not isinstance(class_name, str):
        raise TypeError("class_name must be a string")
    if not isinstance(extensions, list):
        raise TypeError("extensions must be a list")
    for ext in extensions:
        if not isinstance(ext, str):
            raise TypeError("extensions must be a list of strings")

    if not extensions:
        raise ValueError("extensions list cannot be empty")  # Changed to ValueError

    strongest_extension = None
    max_strength = float('-inf')

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


def test_strongest_extension_basic():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_example():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_same_strength():
    assert Strongest_Extension('Test', ['AA', 'BB', 'CC']) == 'Test.AA'

def test_strongest_extension_negative_strength():
    assert Strongest_Extension('Class', ['abc', 'def', 'ghi']) == 'Class.abc'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Base', ['aA', 'bB', 'cC']) == 'Base.aA'

def test_strongest_extension_empty_list():
    with pytest.raises(ValueError) as excinfo:
        Strongest_Extension('Class', [])
    assert str(excinfo.value) == "extensions list cannot be empty"

def test_strongest_extension_invalid_class_name():
    with pytest.raises(TypeError) as excinfo:
        Strongest_Extension(123, ['AA'])
    assert str(excinfo.value) == "class_name must be a string"

def test_strongest_extension_invalid_extensions_list():
    with pytest.raises(TypeError) as excinfo:
        Strongest_Extension('Class', 123)
    assert str(excinfo.value) == "extensions must be a list"

def test_strongest_extension_invalid_extension_type():
    with pytest.raises(TypeError) as excinfo:
        Strongest_Extension('Class', ['AA', 123])
    assert str(excinfo.value) == "extensions must be a list of strings"
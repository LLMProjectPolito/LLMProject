
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

def strongest_extension(class_name, extensions):
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
    strongest_extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    if not extensions:
        return class_name  # Handle empty extensions list

    strongest_extension = extensions[0]
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

# Pytest tests
def test_strongest_extension_basic():
    assert strongest_extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert strongest_extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    assert strongest_extension('my_class', []) == 'my_class'

def test_strongest_extension_mixed_case_equal_strength():
    assert strongest_extension('Class', ['Ab', 'aB', 'Cd', 'dC']) == 'Class.Ab'

def test_strongest_extension_single_extension():
    assert strongest_extension('Class', ['Extension']) == 'Class.Extension'

def test_strongest_extension_numbers_and_symbols():
    assert strongest_extension('Class', ['123', 'A1B', 'a1b']) == 'Class.A1B'

def test_strongest_extension_long_names():
    assert strongest_extension('MyClass', ['VeryLongExtensionName', 'AnotherVeryLongExtensionName']) == 'MyClass.VeryLongExtensionName'

def test_strongest_extension_same_strength_first_in_list():
    assert strongest_extension('Class', ['AB', 'CD', 'ab', 'cd']) == 'Class.AB'

def test_strongest_extension_empty_string_extension():
    assert strongest_extension('Class', ["", "Extension"]) == 'Class.Extension'

def test_strongest_extension_non_string_input():
    with pytest.raises(TypeError):
        strongest_extension('Class', [123, 'Extension'])
    with pytest.raises(TypeError):
        strongest_extension(123, ['Extension'])

def test_strongest_extension_all_zero_strength():
    assert strongest_extension('Class', ['aa', 'bb', 'cc']) == 'Class.aa'

def test_strongest_extension_all_negative_strength():
    assert strongest_extension('Class', ['aA', 'bB', 'cC']) == 'Class.aA'

def test_strongest_extension_class_name_with_numbers_symbols():
    assert strongest_extension('Class123!', ['Extension', 'AnotherExtension']) == 'Class123!.Extension'
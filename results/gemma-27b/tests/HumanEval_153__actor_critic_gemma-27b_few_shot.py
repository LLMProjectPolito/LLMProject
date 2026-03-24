
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
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    if not isinstance(class_name, str):
        raise TypeError("class_name must be a string")
    if not isinstance(extensions, list):
        raise TypeError("extensions must be a list")
    for extension in extensions:
        if not isinstance(extension, str):
            raise TypeError("Each element in extensions must be a string")

    strongest_extension = None
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())

        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    if not extensions:
        return f"{class_name}.None"

    return f"{class_name}.{strongest_extension}"

### Tests (Pytest):
import pytest

def test_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_example():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_empty_extensions():
    assert Strongest_Extension('MyClass', []) == 'MyClass.None'

def test_none_class_name():
    assert Strongest_Extension(None, ['Extension1', 'Extension2']) == 'None.Extension1'

def test_tie():
    assert Strongest_Extension('Class', ['AB', 'Ba']) == 'Class.AB'

def test_all_lowercase():
    assert Strongest_Extension('Class', ['lowercase', 'anotherlowercase']) == 'Class.lowercase'

def test_all_uppercase():
    assert Strongest_Extension('Class', ['UPPERCASE', 'ANOTHERUPPERCASE']) == 'Class.UPPERCASE'

def test_mixed_case():
    assert Strongest_Extension('Class', ['MiXeD', 'CaSe']) == 'Class.MiXeD'

def test_type_error_class_name():
    with pytest.raises(TypeError):
        Strongest_Extension(123, ['Extension'])

def test_type_error_extensions():
    with pytest.raises(TypeError):
        Strongest_Extension('Class', 123)

def test_type_error_extension_element():
    with pytest.raises(TypeError):
        Strongest_Extension('Class', ['Extension', 123])

def test_empty_string_extension():
    assert Strongest_Extension('Class', ['']) == 'Class.'

def test_non_ascii_characters():
    assert Strongest_Extension('Class', ['éàçüö']) == 'Class.éàçüö'

def test_numbers_and_symbols():
    assert Strongest_Extension('Class', ['123!@#', 'abc']) == 'Class.abc'

def test_very_long_extension():
    long_extension = 'A' * 1000 + 'b' * 1000
    assert Strongest_Extension('Class', [long_extension, 'short']) == 'Class.short'
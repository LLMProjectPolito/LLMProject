import pytest
import math


# Focus: Boundary Values
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
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

@pytest.mark.parametrize("extensions", [
    [],  # Empty list of extensions
    ["A"],  # Single uppercase extension
    ["a"],  # Single lowercase extension
    ["Aa"],  # Mixed case extension
    ["AA", "aA", "aa"], # Multiple mixed case extensions
    ["AAAA", "aaaa"], # Extreme case of all uppercase/lowercase
    ["", "A", "a"] # Empty string extension
])
def test_boundary_empty_and_single_extensions(extensions):
    result = Strongest_Extension("TestClass", extensions)
    if not extensions:
        assert result == "TestClass."
    elif len(extensions) == 1:
        assert result == f"TestClass.{extensions[0]}"
    else:
        assert result == "TestClass.AAAA" if "AAAA" in extensions else "TestClass.A"

@pytest.mark.parametrize("extensions", [
    ["Extension1", "Extension2", "Extension3"],  # Multiple extensions with similar strength
    ["Extension1", "extension2", "Extension3"],  # Mixed case extensions
    ["Extension1", "Extension1", "Extension3"] # Duplicate extensions
])
def test_boundary_multiple_extensions(extensions):
    result = Strongest_Extension("TestClass", extensions)
    assert result == f"TestClass.{extensions[0]}"

# Focus: Equivalence Partitioning
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

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
        ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
        ("Test", ['aA', 'Bb', 'Cc'], "my_class.AA"),
        ("Example", ['UPPER', 'lower', 'MiXeD'], "Example.UPPER"),
        ("ClassA", ['Extension1', 'Extension2', 'Extension3'], "ClassA.Extension1"),
        ("Empty", [], "Empty.None"),
    ],
)
def test_equivalence_partitioning_valid_extensions(class_name, extensions, expected):
    """Tests with valid extensions, covering different strength scenarios."""
    if not extensions:
        assert Strongest_Extension(class_name, extensions) == f"{class_name}.None"
    else:
        assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("ClassB", ['sameStrength1', 'sameStrength2'], "ClassB.sameStrength1"),
        ("ClassC", ['equalCaps', 'equalCaps'], "ClassC.equalCaps"),
    ],
)
def test_equivalence_partitioning_equal_strength(class_name, extensions, expected):
    """Tests scenarios where multiple extensions have the same strength, verifying first-in-list selection."""
    assert Strongest_Extension(class_name, extensions) == expected

# Focus: Error Handling/Invalid Input
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

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def test_invalid_class_name():
    with pytest.raises(TypeError):
        Strongest_Extension(123, ['AA', 'Be', 'CC'])

def test_empty_extensions_list():
    assert Strongest_Extension("MyClass", []) == "MyClass.None"

def test_extensions_list_with_non_string():
    with pytest.raises(TypeError):
        Strongest_Extension("MyClass", ['AA', 123, 'CC'])
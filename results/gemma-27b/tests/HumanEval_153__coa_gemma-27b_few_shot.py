
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
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        try:
            strength = cap - sm
        except ZeroDivisionError:
            strength = 0  # Handle cases where there are no lowercase letters
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"

def test_empty_extensions_list():
    assert Strongest_Extension("TestClass", []) == "TestClass."

def test_single_extension():
    assert Strongest_Extension("TestClass", ["Extension"]) == "TestClass.Extension"

def test_all_uppercase():
    assert Strongest_Extension("TestClass", ["AAA", "BBB", "CCC"]) == "TestClass.AAA"

def test_all_lowercase():
    assert Strongest_Extension("TestClass", ["aaa", "bbb", "ccc"]) == "TestClass.aaa"

def test_mixed_case():
    assert Strongest_Extension("TestClass", ["Aa", "BB", "cC"]) == "TestClass.BB"

def test_equal_strength_first_in_list():
    assert Strongest_Extension("TestClass", ["AB", "Ba"]) == "TestClass.AB"

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
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        
        try:
            strength = cap_count - sm_count
        except ZeroDivisionError:
            strength = 0  # Handle cases where there are no lowercase letters

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def test_equivalence_partitioning_positive_strength():
    assert Strongest_Extension("ClassA", ["AA", "Be", "CC"]) == "ClassA.AA"

def test_equivalence_partitioning_negative_strength():
    assert Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "Slices.SErviNGSliCes"

def test_equivalence_partitioning_equal_strength():
    assert Strongest_Extension("Test", ["AB", "Cd", "EF"]) == "Test.AB"

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
    if not isinstance(class_name, str):
        raise TypeError("Class name must be a string.")
    if not isinstance(extensions, list):
        raise TypeError("Extensions must be a list.")
    for extension in extensions:
        if not isinstance(extension, str):
            raise TypeError("Each extension must be a string.")

    if not extensions:
        return class_name + ".None"

    strongest_extension = extensions[0]
    max_strength = float('-inf')

    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return class_name + "." + strongest_extension

def test_invalid_class_name_type():
    with pytest.raises(TypeError) as excinfo:
        Strongest_Extension(123, ['AA', 'Be'])
    assert "Class name must be a string." in str(excinfo.value)

def test_invalid_extensions_type():
    with pytest.raises(TypeError) as excinfo:
        Strongest_Extension('my_class', "not a list")
    assert "Extensions must be a list." in str(excinfo.value)

def test_invalid_extension_type():
    with pytest.raises(TypeError) as excinfo:
        Strongest_Extension('my_class', ['AA', 123])
    assert "Each extension must be a string." in str(excinfo.value)
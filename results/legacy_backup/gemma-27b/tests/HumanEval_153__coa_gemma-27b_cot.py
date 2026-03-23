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
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"

def test_empty_extensions_list():
    assert Strongest_Extension("Class", []) == "Class."

def test_single_extension():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_all_uppercase():
    assert Strongest_Extension("Class", ["AA", "BB", "CC"]) == "Class.AA"

def test_all_lowercase():
    assert Strongest_Extension("Class", ["aa", "bb", "cc"]) == "Class.aa"

def test_mixed_case():
    assert Strongest_Extension("Class", ["AA", "Be", "CC"]) == "Class.AA"

def test_equal_strength_first_in_list():
    assert Strongest_Extension("Class", ["AB", "Ba"]) == "Class.AB"

def test_negative_strength():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

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
            strength = 0  # Handle cases where SM is zero to avoid division by zero

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def test_equivalence_partitioning_1():
    """All uppercase extensions"""
    assert Strongest_Extension("ClassA", ["AA", "BB", "CC"]) == "ClassA.AA"

def test_equivalence_partitioning_2():
    """All lowercase extensions"""
    assert Strongest_Extension("ClassB", ["aa", "bb", "cc"]) == "ClassB.aa"

def test_equivalence_partitioning_3():
    """Mixed case extensions"""
    assert Strongest_Extension("ClassC", ["SErviNGSliCes", "Cheese", "StuFfed"]) == "ClassC.SErviNGSliCes"

# Focus: Error Handling/Invalid Input
import pytest

def test_empty_extensions_list():
    assert Strongest_Extension("Class", []) == "Class."

def test_invalid_class_name_type():
    with pytest.raises(TypeError):
        Strongest_Extension(123, ["Extension1"])

def test_invalid_extensions_list_type():
    with pytest.raises(TypeError):
        Strongest_Extension("Class", "Extension1")

def test_extensions_with_same_strength():
    assert Strongest_Extension("Class", ["AA", "BB"]) == "Class.AA"

def test_negative_strength():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_mixed_case_extensions():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
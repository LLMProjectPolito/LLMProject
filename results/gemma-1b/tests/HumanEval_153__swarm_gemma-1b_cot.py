
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

def strongest_extension():
    """
    Determines the strongest extension based on uppercase and lowercase counts.
    """
    rules = [
        "Output ONLY valid code. Ensure necessary imports (pytest, math) are at the top.",
        "DO NOT RE-DEFINE the function under test.",
        "DO NOT use placeholder imports. Assume function is in scope.",
    ]
    extensions = [
        "abc",
        "xyz",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqr",
        "stu",
        "vwx",
        "yza",
    ]

    for extension in extensions:
        uppercase_count = 0
        lowercase_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                uppercase_count += 1
            elif 'a' <= char <= 'z':
                lowercase_count += 1

        strength = uppercase_count - lowercase_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return strongest_extension

def test_strongest_extension():
    assert strongest_extension() == "xyz"
    assert strongest_extension() == "ghi"
    assert strongest_extension() == "jkl"
    assert strongest_extension() == "mno"
    assert strongest_extension() == "pqr"
    assert strongest_extension() == "stu"
    assert strongest_extension() == "vwx"
    assert strongest_extension() == "yza"

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
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    
    def calculate_strength(extension):
        cap = 0
        sm = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap += 1
            elif 'a' <= char <= 'z':
                sm += 1
        if sm == 0:
            return float('inf') if cap > 0 else 0
        return cap - sm

    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        strength = calculate_strength(extension)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"], "Slices.SErviNGSliCes"),
        ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
        ("AnotherClass", ["aA", "bB", "cC"], "AnotherClass.aA"),
        ("TestClass", ["", " ", "123"], "TestClass. "),
        ("Class1", ["UPPER", "lower", "MixedCase"], "Class1.MixedCase"),
        ("Class2", ["ALLCAPS", "alllower"], "Class2.ALLCAPS"),
        ("Class3", ["12345", "abcde"], "Class3.abcde"),
        ("Class4", ["A", "a"], "Class4.a"),
        ("Class5", [], "Class5."),
        ("Class6", ["A", "a", "AA", "aa"], "Class6.AA"),
        ("Class7", ["ABC", "abc", "AbC"], "Class7.AbC"),
        ("Class8", ["123", "abc", "ABC"], "Class8.ABC"),
        ("Class9", ["", " ", "  "], "Class9."),
    ],
)
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
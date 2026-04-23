
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
    strongest_extension = None
    max_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        
        if sm_count == 0:
            strength = float('inf') if cap_count > 0 else 0
        else:
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
        ("TestClass", ['ExtensionA', 'extensionB', 'ExtensionC'], "TestClass.ExtensionA"),
        ("Example", ['a', 'b', 'c'], "Example.a"),
        ("Class1", ['A', 'B', 'C'], "Class1.A"),
        ("Class2", ['abc', 'def', 'ghi'], "Class2.abc"),
        ("Class3", ['AbC', 'aBc', 'ABC'], "Class3.AbC"),
        ("Class4", ['Extension123', 'extension456', 'EXTENSION789'], "Class4.EXTENSION789"),
        ("Class5", [], "Class5.None"),
        ("Class6", [''], "Class6."),
        ("Class7", ['AAAA', 'bbbb', 'CCCC'], "Class7.AAAA"),
        ("Class8", ['AaBbCc', 'DdEeFf', 'GgHhIi'], "Class8.AaBbCc"),
        ("Class9", ['ExtensionWithNumbers123', 'AnotherExtension456'], "Class9.ExtensionWithNumbers123"),
        ("Class10", ['ExtensionWithSymbols!@#', 'AnotherExtension$%^'], "Class10.ExtensionWithSymbols!@#"),
        ("Class11", ['ExtensionWithSpaces ', 'AnotherExtension'], "Class11.ExtensionWithSpaces "),
        ("Class12", ['ExtensionWithMixedCase', 'extensionwithalllowercase'], "Class12.ExtensionWithMixedCase"),
        ("Class13", ['ExtensionWithMixedCase', 'ExtensionWithMixedCase'], "Class13.ExtensionWithMixedCase"),
        ("Class14", ['Extension1', 'Extension2', 'Extension3'], "Class14.Extension1"),
        ("Class15", ['ExtensionA', 'ExtensionA', 'ExtensionB'], "Class15.ExtensionA"),
        ("Class16", ['ExtensionA', 'ExtensionB', 'ExtensionA'], "Class16.ExtensionA"),
        ("Class17", ['ExtensionA', 'ExtensionB', 'ExtensionC', 'ExtensionA'], "Class17.ExtensionA"),
    ]
)
def test_strongest_extension(class_name, extensions, expected):
    if not extensions:
        assert Strongest_Extension(class_name, extensions) == f"{class_name}.None"
    else:
        assert Strongest_Extension(class_name, extensions) == expected
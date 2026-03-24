
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

@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
        ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
        ("TestClass", ['ExtensionA', 'extensionB', 'ExtensionC'], "TestClass.ExtensionA"),
        ("Example", ['abc', 'ABC', 'aBc'], "Example.ABC"),
        ("Class1", ['ext1', 'Ext2', 'eXt3'], "Class1.Ext2"),
        ("Empty", [], "Empty.None"),
        ("Single", ['OnlyExtension'], "Single.OnlyExtension"),
        ("MixedCase", ['MiXeDCase', 'mixedcase', 'MIXEDCASE'], "MixedCase.MIXEDCASE"),
        ("Numbers", ['123', 'A12', 'a12'], "Numbers.A12"),
        ("Symbols", ['!@#', 'A!@', 'a@#'], "Numbers.A!@"),
        ("ClassA", ['extA', 'extA'], "ClassA.extA"),
        ("ClassB", ['extB', 'extC', 'extB'], "ClassB.extB"),
        ("ClassC", ['extC', 'extB', 'extA'], "ClassC.extC"),
        ("Example", [], "Example.None"),
        ("Class1", ['a', 'b', 'c'], "Class1.a"),
        ("Class2", ['A', 'B', 'C'], "Class2.A"),
        ("Class3", ['Aa', 'Bb', 'Cc'], "Class3.Aa"),
        ("Class4", ['AAA', 'BBB', 'CCC'], "Class4.AAA"),
        ("Class5", ['aaa', 'bbb', 'ccc'], "Class5.aaa"),
        ("Class6", ['AbC', 'aBc', 'ABc'], "Class6.AbC"),
        ("Class7", ['Extension123', 'extension456', 'EXTENSION789'], "Class7.Extension123"),
        ("Class8", ['ExtensionWithNumbers1', 'extensionWithNumbers2'], "Class8.ExtensionWithNumbers1"),
        ("Class9", ['ExtensionWithSymbols!', 'extensionWithSymbols@'], "Class9.ExtensionWithSymbols!"),
        ("Class10", ['ExtensionWithSpaces ', 'extensionWithSpaces'], "Class10.ExtensionWithSpaces "),
    ],
)
def test_strongest_extension(class_name, extensions, expected):
    if not extensions:
        assert Strongest_Extension(class_name, extensions) == f"{class_name}.None"
    else:
        assert Strongest_Extension(class_name, extensions) == expected
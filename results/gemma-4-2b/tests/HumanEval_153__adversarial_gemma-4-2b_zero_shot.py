
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
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1
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
        ("AnotherClass", ["aB", "cD", "eF"], "AnotherClass.aB"),
        ("TestClass", ["test", "Test", "TEST"], "TestClass.test"),
        ("Class1", ["UpperCase", "LowerCase", "MixedCase"], "Class1.UpperCase"),
        ("Class2", [], "Class2. "),
        ("Class3", ["", "a"], "Class3.a"),
        ("Class4", ["A", "b", "C"], "Class4.A"),
        ("Class5", ["abc", "ABC", "aBC"], "Class5.abc"),
        ("Class6", ["123", "abc", "ABC"], "Class6.abc"),
        ("Class7", ["a1b", "AbC"], "Class7.a1b"),
        ("Class8", ["aB1", "aBc"], "Class8.aB1"),
        ("Class9", ["aB", "aBc", "aBC"], "Class9.aB"),
        ("Class10", ["aB", "aBc", "aBC"], "Class10.aB"),
        ("Class11", ["aB", "aBc", "aBC"], "Class11.aB"),
        ("Class12", ["aB", "aBc", "aBC"], "Class12.aB"),
        ("Class13", ["aB", "aBc", "aBC"], "Class13.aB"),
    ],
)
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"], "Slices.SErviNGSliCes"),
        ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
        ("AnotherClass", ["aB", "cD", "eF"], "AnotherClass.aB"),
        ("TestClass", ["test", "Test", "TEST"], "TestClass.test"),
        ("Class1", ["UpperCase", "LowerCase", "MixedCase"], "Class1.UpperCase"),
        ("Class2", [], "Class2. "),
        ("Class3", ["", "a"], "Class3.a"),
        ("Class4", ["A", "b", "C"], "Class4.A"),
        ("Class5", ["abc", "ABC", "aBC"], "Class5.abc"),
        ("Class6", ["123", "abc", "ABC"], "Class6.abc"),
        ("Class7", ["a1b", "aBc"], "Class7.a1b"),
        ("Class8", ["aB1", "aBc"], "Class8.aB1"),
        ("Class9", ["aB", "aBc", "aBC"], "Class9.aB"),
        ("Class10", ["aB", "aBc", "aBC"], "Class10.aB"),
        ("Class11", ["aB", "aBc", "aBC"], "Class11.aB"),
        ("Class12", ["aB", "aBc", "aBC"], "Class12.aB"),
        ("Class13", ["aB", "aBc", "aBC"], "Class13.aB"),
    ],
)
def test_empty_extensions(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Class1", ["aB", "aBc", "aBC"], "Class1.aB"),
        ("Class2", ["aB", "aBc", "aBC"], "Class2.aB"),
        ("Class3", ["aB", "aBc", "aBC"], "Class3.aB"),
        ("Class4", ["aB", "aBc", "aBC"], "Class4.aB"),
    ],
)
def test_tie_strength(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
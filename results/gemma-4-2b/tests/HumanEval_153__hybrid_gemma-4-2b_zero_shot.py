
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
        return cap - sm

    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        strength = calculate_strength(extension)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
        elif strength == max_strength and extensions.index(extension) < extensions.index(strongest_extension):
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"



@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"], "Slices.SErviNGSliCes"),
        ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
        ("AnotherClass", ["XML", "JSON", "YAML"], "AnotherClass.XML"),
        ("TestClass", ["test", "Test", "TEST"], "TestClass.Test"),
        ("EmptyClass", [], "EmptyClass."),
        ("ClassWithNumbers", ["A1", "B2", "C3"], "ClassWithNumbers.A1"),
        ("ClassWithSpecialChars", ["!@#", "%^&", "&*#"], "ClassWithSpecialChars.!@#"),
        ("ClassWithMixedCase", ["MixedCase", "mixedcase"], "ClassWithMixedCase.MixedCase"),
        ("ClassWithLongExtension", ["ExtremelyLongExtensionName123", "Short"], "ClassWithLongExtension.ExtremelyLongExtensionName123"),
        ("ClassWithSameStrength", ["AA", "BB", "CC"], "ClassWithSameStrength.AA"),
        ("ClassWithEmptyExtension", ["", "A", "B"], "ClassWithEmptyExtension.A"),
        ("ClassWithExtensionWithOnlyLowercase", ["lowercase", "UPPERCASE"], "ClassWithExtensionWithOnlyLowercase.lowercase"),
        ("ClassWithExtensionWithOnlyUppercase", ["UPPERCASE", "lowercase"], "ClassWithExtensionWithOnlyUppercase.UPPERCASE"),
        ("ClassWithExtensionContainingSpecialCharactersAndNumbers", ["!@#123", "abc"], "ClassWithExtensionContainingSpecialCharactersAndNumbers.!@#123"),
        ("ClassWithExtensionAndClass", ["ClassExtension", "Class"], "ClassWithExtensionAndClass.ClassExtension"),
    ],
)
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Class", ["a", "A", "b"], "Class.A"),
    ("Another", ["abc", "ABC"], "Another.ABC"),
    ("Test", ["test1", "Test2"], "Test.Test2")

])
def test_case_sensitivity(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

@pytest.mark.parametrize("class_name, extensions", [
    ("Class", []),
    ("Class", [""])
])
def test_empty_extensions(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == f"{class_name}.EmptyClass."

@pytest.mark.parametrize("class_name, extensions", [
    ("Class", ["a", "b", "c"]),
    ("Class", ["abc", "def", "ghi"]),
])
def test_same_strength_tie(class_name, extensions):
    assert Strongest_Extension(class_name, extensions) == extensions[0]
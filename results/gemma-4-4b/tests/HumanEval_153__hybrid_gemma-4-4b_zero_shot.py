
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
    strongest_extension = ""
    max_strength = float('-inf')

    for extension in extensions:
        cap = 0
        sm = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                cap += 1
            elif 'a' <= char <= 'z':
                sm += 1
        
        strength = cap - sm

        if strength > max_strength:
            max_strength = strength
            strongest_extension = f"{class_name}.{extension}"

    return strongest_extension

@pytest.mark.parametrize("class_name, extensions, expected", [
    ("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"], "Slices.SErviNGSliCes"),
    ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
    ("TestClass", ["test", "TEST", "tEst"], "TestClass.TEST"),
    ("AnotherClass", ["", " ", "123"], "AnotherClass. "),
    ("ClassX", ["ABCdef", "defABC", "AbCdEf"], "ClassX.AbCdEf"),
    ("Example", ["aBcDeF", "bCdEfA", "cDefAb"], "Example.bCdEfA"),
    ("Class1", ["123", "abc", "ABC"], "Class1.ABC"),
    ("Class2", ["aA", "AA", "aa"], "Class2.aa"),
    ("Class3", [], "Class3."),
    ("Class4", ["A"], "Class4.A"),
    ("Class5", ["a"], "Class5.a"),
    ("Class6", ["AB", "ba"], "Class6.ba"),
    ("Class7", ["xyz", "XYZ"], "Class7.XYZ"),
    ("Class8", ["aB", "Ab"], "Class8.Ab"),
    ("Class9", ["12345", "54321"], "Class9.54321"),
    ("Class10", ["!@#$%^", "#$%^&*"], "Class10.#%^&*"),
    ("Class11", ["aA", "bB", "cC"], "Class11.aA"),
    ("Class12", ["A", "a"], "Class12.a"),
])
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected
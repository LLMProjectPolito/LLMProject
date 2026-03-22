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
    return class_name + "." + strongest_extension

def test_strongest_extension_basic():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_strongest_extension_equal_strength():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension("Class", ['AAAA', 'BBB', 'CCCC']) == "Class.AAAA"

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension("Class", ['aaaa', 'bbbb', 'cccc']) == "Class.aaaa"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("Class", ['aA', 'Bb', 'Cc']) == "Class.aA"

def test_strongest_extension_numbers_and_symbols():
    assert Strongest_Extension("Class", ['123', 'abc', '!@#']) == "Class.123"

def test_strongest_extension_tiebreaker():
    assert Strongest_Extension("Class", ['AA', 'AA', 'BB']) == "Class.AA"

def test_strongest_extension_class_name_with_underscore():
    assert Strongest_Extension("my_class_name", ['AA', 'Be', 'CC']) == "my_class_name.AA"

def test_strongest_extension_extension_with_numbers():
    assert Strongest_Extension("Class", ['A123', 'b456', 'C789']) == "Class.A123"

def test_strongest_extension_extension_with_symbols():
    assert Strongest_Extension("Class", ['A!@#', 'b$%^', 'C&*()']) == "Class.A!@#"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Class", ['abc', 'ABC', 'def']) == "Class.abc"

def test_strongest_extension_only_numbers():
    assert Strongest_Extension("Class", ['12345', '67890']) == "Class.12345"

def test_strongest_extension_only_symbols():
    assert Strongest_Extension("Class", ['!@#$%^', '&*()_+']) == "Class.!@#$%^"

def test_strongest_extension_empty_string():
    assert Strongest_Extension("Class", [""]) == "Class."

def test_strongest_extension_long_extension_name():
    long_extension = "A" * 1000
    assert Strongest_Extension("Class", [long_extension, "BB"]) == "Class.BB"

def test_strongest_extension_extension_with_spaces():
    assert Strongest_Extension("Class", ["   ", "AA"]) == "Class."

def test_strongest_extension_special_characters():
    assert Strongest_Extension("Class", ["A!@#", "B$%", "C^&*"]) == "Class.A!@#"

def test_strongest_extension_same_strength_different_strings():
    assert Strongest_Extension("Class", ["AA", "BB", "CC"]) == "Class.AA"
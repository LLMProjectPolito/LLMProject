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

def test_empty_extensions():
    assert Strongest_Extension("Class", []) == "Class.None"

def test_single_extension():
    assert Strongest_Extension("Class", ["Extension"]) == "Class.Extension"

def test_multiple_extensions():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_equal_strength_first_wins():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_all_uppercase():
    assert Strongest_Extension("Class", ["AAA", "BBB", "CCC"]) == "Class.AAA"

def test_all_lowercase():
    assert Strongest_Extension("Class", ["aaa", "bbb", "ccc"]) == "Class.aaa"

def test_mixed_case():
    assert Strongest_Extension("Class", ["aA", "Bb", "Cc"]) == "Class.aA"

def test_extension_with_numbers():
    assert Strongest_Extension("Class", ["Ext1", "Ext2", "Ext3"]) == "Class.Ext1"

def test_extension_with_special_characters():
    assert Strongest_Extension("Class", ["Ext!", "Ext@", "Ext#"]) == "Class.Ext!"

def test_negative_strength():
    assert Strongest_Extension("Class", ["abc", "ABC", "aBc"]) == "Class.ABC"

def test_long_extensions():
    assert Strongest_Extension("Class", ["VeryLongExtension1", "VeryLongExtension2"]) == "Class.VeryLongExtension1"

def test_class_name_with_spaces():
    assert Strongest_Extension("My Class", ["Ext1", "Ext2"]) == "My Class.Ext1"

def test_extension_names_with_spaces():
    assert Strongest_Extension("Class", ["Ext 1", "Ext2"]) == "Class.Ext 1"

def test_empty_class_name():
    assert Strongest_Extension("", ["Ext1", "Ext2"]) == "".Ext1
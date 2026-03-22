# STEP 1: REASONING
# The function `Strongest_Extension` takes a class name and a list of extensions as input.
# It calculates the strength of each extension based on the difference between uppercase and lowercase letters.
# The function returns a string combining the class name and the strongest extension name.
# If multiple extensions have the same strength, the first one in the list is chosen.
# The tests should cover cases with different strengths, ties, empty extension lists, and edge cases with uppercase/lowercase letters.

# STEP 2: PLAN
# 1. Test case with a clear strongest extension (positive strength).
# 2. Test case with a clear strongest extension (negative strength).
# 3. Test case with multiple extensions having the same strength (tie-breaker).
# 4. Test case with an empty extension list (should return ClassName.).
# 5. Test case with extensions containing only uppercase letters.
# 6. Test case with extensions containing only lowercase letters.
# 7. Test case with extensions containing mixed case letters.
# 8. Test case with an empty class name.
# 9. Test case with extensions containing numbers and special characters.

# STEP 3: CODE
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
    if not extensions:
        return f"{class_name}."

    strongest_extension = extensions[0]
    max_strength = 0
    for extension in extensions:
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

def test_clear_strongest_positive():
    assert Strongest_Extension("ClassA", ["Ext1", "EXT2", "ext3"]) == "ClassA.EXT2"

def test_clear_strongest_negative():
    assert Strongest_Extension("ClassB", ["ext1", "Ext2", "eXt3"]) == "ClassB.Ext2"

def test_tie_breaker():
    assert Strongest_Extension("ClassC", ["Ext1", "EXT1", "ext2"]) == "ClassC.Ext1"

def test_empty_extensions():
    assert Strongest_Extension("ClassD", []) == "ClassD."

def test_only_uppercase():
    assert Strongest_Extension("ClassE", ["AAA", "BBB", "CCC"]) == "ClassE.AAA"

def test_only_lowercase():
    assert Strongest_Extension("ClassF", ["aaa", "bbb", "ccc"]) == "ClassF.aaa"

def test_mixed_case():
    assert Strongest_Extension("ClassG", ["ExT1", "eXt2", "EXT3"]) == "ClassG.EXT3"

def test_empty_class_name():
    assert Strongest_Extension("", ["Ext1", "EXT2"]) == ".EXT2"

def test_numbers_and_special_chars():
    assert Strongest_Extension("ClassH", ["Ext1!", "EXT2@", "ext3#"]) == "ClassH.EXT2@"
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
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

# STEP 2: PLAN - List test functions names and scenarios.
# Test cases:
# 1. Basic test case with a clear strongest extension.
# 2. Test case with multiple extensions having the same strength, check for first in list.
# 3. Test case with all lowercase extensions.
# 4. Test case with all uppercase extensions.
# 5. Test case with empty extension list.
# 6. Test case with a class name containing special characters.
# 7. Test case with extensions containing special characters.
# 8. Test case with mixed case extensions.
# 9. Test case with a long class name and long extensions.

@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
        ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
        ("Class", ['aaa', 'bbb', 'ccc'], "Class.aaa"),
        ("Class", ['AAA', 'BBB', 'CCC'], "Class.AAA"),
        ("Class", [], "Class.None"),
        ("Class!", ['Extension1', 'Extension2'], "Class!.Extension1"),
        ("Class", ['Ext@nsion1', 'Ext#nsion2'], "Class.Ext@nsion1"),
        ("Class", ['ExTeNsIoN1', 'ExTeNsIoN2'], "Class.ExTeNsIoN1"),
        ("VeryLongClassName", ['VeryLongExtension1', 'VeryLongExtension2'], "VeryLongClassName.VeryLongExtension1"),
        ("Class", ['aA', 'Bb', 'Cc'], "Class.aA"),
        ("Class", ['aA', 'aA'], "Class.aA"),
        ("Class", ['AA', 'aa'], "Class.AA"),
        ("Class", ['abcDEF', 'AbCdEf'], "Class.abcDEF")
    ],
)
def test_strongest_extension(class_name, extensions, expected):
    assert Strongest_Extension(class_name, extensions) == expected

def test_empty_extensions():
    assert Strongest_Extension("Class", []) == "Class.None"
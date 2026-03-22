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
        
        if len(extension) > 0:
            strength = cap_count - sm_count
        else:
            strength = float('-inf')

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

@pytest.mark.parametrize("class_name, extensions", [
    ("TestClass", ["ALLCAPS", "alllower", "MiXeDCase"])
])
def test_edge_case_all_same_strength(class_name, extensions):
    """Tests the case where multiple extensions have the same strength,
    ensuring the first one in the list is chosen."""
    assert Strongest_Extension(class_name, extensions) == "TestClass.ALLCAPS"

@pytest.mark.parametrize("class_name, extensions", [
    ("TestClass", ["", "Extension1", "Extension2"]),
])
def test_empty_extension_string(class_name, extensions):
    """Tests the scenario where an empty string is present in the extensions list.
    This is an edge case because the strength calculation might be undefined or lead to unexpected behavior.
    The function should handle this gracefully and select the next valid extension.
    """
    expected_result = "TestClass.Extension1"
    assert Strongest_Extension(class_name, extensions) == expected_result
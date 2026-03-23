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
        return class_name  # Handle empty extensions list

    strongest_extension = extensions[0]
    max_strength = float('-inf')

    for extension in extensions:
        if not isinstance(extension, str):
            continue  # Skip non-string extensions

        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"

# Pytest tests
def test_strongest_extension_basic():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('my_class', []) == 'my_class'

def test_strongest_extension_all_same_strength():
    assert Strongest_Extension('my_class', ['AA', 'BB', 'CC']) == 'my_class.AA'

def test_strongest_extension_negative_strength():
    assert Strongest_Extension('my_class', ['aa', 'bb', 'cc']) == 'my_class.aa'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('my_class', ['aA', 'Bb', 'Cc']) == 'my_class.aA'

def test_strongest_extension_single_extension():
    assert Strongest_Extension('my_class', ['Extension1']) == 'my_class.Extension1'

def test_strongest_extension_long_names():
    assert Strongest_Extension('my_class', ['VeryLongExtensionName', 'AnotherVeryLongExtensionName']) == 'my_class.VeryLongExtensionName'

def test_strongest_extension_equal_strength_different_length():
    assert Strongest_Extension('my_class', ['AB', 'A']) == 'my_class.AB'

def test_strongest_extension_empty_string_extension():
    assert Strongest_Extension('my_class', ['']) == 'my_class.'

def test_strongest_extension_with_non_string_characters():
    assert Strongest_Extension('my_class', ['123', 'abc']) == 'my_class.abc'
    assert Strongest_Extension('my_class', ['abc', 123]) == 'my_class.abc'
    assert Strongest_Extension('my_class', [123, 'abc']) == 'my_class.abc'
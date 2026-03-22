def test_strongest_extension_basic():
    assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"

def test_strongest_extension_same_strength():
    assert Strongest_Extension("my_class", ['AA', 'Be', 'CC']) == "my_class.AA"

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension("MyClass", []) == "MyClass."

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension("TestClass", ['AAAA', 'BBB', 'CCCC']) == "TestClass.AAAA"

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension("TestClass", ['aaaa', 'bbbb', 'cccc']) == "TestClass.aaaa"

def test_strongest_extension_mixed_case():
    assert Strongest_Extension("MyClass", ['aA', 'Bb', 'Cc']) == "MyClass.aA"

def test_strongest_extension_negative_strength():
    assert Strongest_Extension("Class", ['abc', 'DEF', 'ghi']) == "Class.DEF"

def test_strongest_extension_zero_strength():
    assert Strongest_Extension("Class", ['ab', 'CD', 'ef']) == "Class.CD"

def test_strongest_extension_class_with_underscore():
    assert Strongest_Extension("my_class_name", ['AA', 'Be', 'CC']) == "my_class_name.AA"

def test_strongest_extension_extension_with_underscore():
    assert Strongest_Extension("Class", ['A_A', 'Be', 'CC']) == "Class.A_A"

def test_strongest_extension_class_and_extension_with_underscore():
    assert Strongest_Extension("my_class_name", ['A_A', 'Be', 'CC']) == "my_class_name.A_A"
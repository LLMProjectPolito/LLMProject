
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

class TestStrongest_Extension:
    def test_empty_extensions(self):
        assert Strongest_Extension("my_class", []) == "my_class."

    def test_single_extension(self):
        assert Strongest_Extension("my_class", ["AA"]) == "my_class.AA"
        assert Strongest_Extension("my_class", ["Be"]) == "my_class.Be"
        assert Strongest_Extension("my_class", ["CC"]) == "my_class.CC"

    def test_multiple_extensions_same_strength(self):
        assert Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']) == "Slices.SErviNGSliCes"
        assert Strongest_Extension("Slices", ['AA', 'BB']) == "Slices.AA"
        assert Strongest_Extension("Slices", ['CC', 'DD']) == "Slices.CC"

    def test_mixed_case(self):
        assert Strongest_Extension("my_class", ['Aa', 'BB']) == "my_class.Aa"
        assert Strongest_Extension("my_class", ['aA', 'BB']) == "my_class.aA"

    def test_all_uppercase(self):
        assert Strongest_Extension("my_class", ['AAA']) == "my_class.AAA"
        assert Strongest_Extension("my_class", ['AAAA']) == "my_class.AAAA"

    def test_all_lowercase(self):
        assert Strongest_Extension("my_class", ['aaa']) == "my_class.aaa"
        assert Strongest_Extension("my_class", ['aaaa']) == "my_class.aaaa"
    
    def test_empty_extension_name(self):
        assert Strongest_Extension("my_class", [""]) == "my_class."

    def test_extension_with_numbers(self):
        assert Strongest_Extension("my_class", ["123", "abc"]) == "my_class.abc"
        assert Strongest_Extension("my_class", ["A1", "b2"]) == "my_class.A1"

    def test_extension_with_special_characters(self):
        assert Strongest_Extension("my_class", ["!@#", "$%^"]) == "my_class.!@#"
        assert Strongest_Extension("my_class", ["a!b", "c%d"]) == "my_class.a!b"
    
    def test_class_name_empty(self):
        assert Strongest_Extension("", ["AA", "BB"]) == ""
        assert Strongest_Extension("", ["A", "B"]) == ""

    def test_extension_with_mixed_characters(self):
        assert Strongest_Extension("my_class", ["MiXeD", "simple"]) == "my_class.MiXeD"
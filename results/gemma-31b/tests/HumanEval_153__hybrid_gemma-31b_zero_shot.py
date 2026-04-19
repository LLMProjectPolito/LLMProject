
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
    """
    Finds the strongest extension based on the difference between 
    the number of uppercase and lowercase letters (Uppercase - Lowercase).
    Returns 'ClassName.ExtensionName'. If extensions list is empty, returns 'ClassName'.
    """
    def calculate_strength(ext):
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        return cap - sm

    if not extensions:
        return class_name

    max_strength = float('-inf')
    strongest_ext = None

    for ext in extensions:
        strength = calculate_strength(ext)
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
            
    return f"{class_name}.{strongest_ext}"

class TestStrongestExtension:
    """Comprehensive test suite for Strongest_Extension function."""

    @pytest.mark.parametrize("class_name, extensions, expected", [
        # Basic example: Complex case with mixed strengths
        ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
        
        # Tie-breaking: First occurrence should win
        ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
        
        # All uppercase: Maximum possible strength
        ("Core", ['BASE', 'low', 'Mixed'], "Core.BASE"),
        
        # All lowercase: Minimum possible strength (first one wins)
        ("Core", ['base', 'low', 'mixed'], "Core.base"),
        
        # Special characters and numbers: Only letters should be counted
        ("System", ['Ext123', 'EXT_456', 'ext_789'], "System.EXT_456"),
        
        # Single extension in the list
        ("Base", ['OnlyOne'], "Base.OnlyOne"),
        
        # All extensions have negative strength (pick the least negative)
        ("Base", ['lowercase', 'morelowercase', 'low'], "Base.low"),
        
        # Strength of zero: Equal upper and lower (first one wins)
        ("Class", ['Aa', 'Bb', 'Cc'], "Class.Aa"),
        
        # No alphabetic characters: Strength 0 - 0 = 0 (first one wins)
        ("Void", ['123', '!!!', '   '], "Void.123"),
        
        # Class name with special characters/numbers
        ("My_Class_123", ['Alpha', 'Beta'], "My_Class_123.Alpha"),
        
        # Very long strings to test performance/stability
        ("Large", ['A' * 100 + 'a' * 50, 'A' * 50 + 'a' * 100], "Large." + 'A' * 100 + 'a' * 50),
    ])
    def test_standard_and_edge_cases(self, class_name, extensions, expected):
        """Tests various scenarios including provided examples, ties, and special characters."""
        assert Strongest_Extension(class_name, extensions) == expected

    def test_empty_extensions_list(self):
        """Tests behavior when the extensions list is completely empty."""
        assert Strongest_Extension("EmptyTest", []) == "EmptyTest"

    def test_empty_extension_string(self):
        """Tests behavior when the list contains an empty string."""
        # Strength for "" is 0. If it's the only element, it's the strongest.
        assert Strongest_Extension("Test", [""]) == "Test."

    def test_strength_calculation_logic(self):
        """Explicitly verifies the strength logic: 'A'(1), 'Aa'(0), 'a'(-1)."""
        # 'A' is strongest (1), 'Aa' is middle (0), 'a' is weakest (-1)
        assert Strongest_Extension("Test", ["a", "Aa", "A"]) == "Test.A"
        # 'a' is strongest if others are even weaker (e.g., 'aa')
        assert Strongest_Extension("Test", ["a", "aa"]) == "Test.a"

    def test_case_sensitivity_of_class_name(self):
        """Ensures the class name is preserved exactly as passed, regardless of case."""
        assert Strongest_Extension("cLaSsNaMe", ["EXT"]) == "cLaSsNaMe.EXT"
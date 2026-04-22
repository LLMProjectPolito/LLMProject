
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
    Implementation of the function to be tested.
    Calculates strength as (number of uppercase - number of lowercase).
    Returns the first extension with the maximum strength formatted as 'class_name.extension'.
    """
    if not extensions:
        return None

    def calculate_strength(ext):
        cap = sum(1 for char in ext if char.isupper())
        sm = sum(1 for char in ext if char.islower())
        return cap - sm

    # Python's max() is stable, returning the first occurrence in case of ties.
    strongest = max(extensions, key=calculate_strength)
    return f"{class_name}.{strongest}"


@pytest.mark.parametrize("class_name, extensions, expected", [
    # --- Original Docstring & Basic Examples ---
    ("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed'], "Slices.SErviNGSliCes"),
    ("my_class", ['AA', 'Be', 'CC'], "my_class.AA"),
    
    # --- Tie-Breaking Scenarios (Should pick the first in the list) ---
    ("TieBreak", ["Ab", "aB", "AB", "ab"], "TieBreak.Ab"),
    ("ZeroStrengthTie", ["aB", "Ab", "xy"], "ZeroStrengthTie.aB"),
    ("SymbolTie", ["123", "!!!", "456"], "SymbolTie.123"),
    
    # --- Strength Extremes (Negative, Positive, and Zero) ---
    ("AllNegative", ["abc", "def", "a"], "AllNegative.a"),
    ("AllPositive", ["AAA", "A", "BB"], "PosTest.AAA"),
    ("MixedStrengths", ["aB", "cDe", "F", "GHI"], "MixedStrengths.GHI"),
    ("NegativeVsPositive", ["abc", "def", "aB"], "NegVsPos.aB"),
    ("ExtremeDifference", ["ZZZZZ", "aaaaa", "ZzZzZ"], "Extreme.ZZZZZ"),
    ("LargeNegative", ["aaaaaaaaaa", "a"], "BigNeg.a"),
    
    # --- Character Type Edge Cases ---
    ("OnlyUppercase", ["A", "BB", "CCC"], "Upper.A"),
    ("OnlyLowercase", ["a", "bb", "ccc"], "Lower.a"),
    ("SpecialChars", ["A1b", "C2D", "E!F"], "SpecialChars.C2D"),
    ("Symbols", ["A1!", "a2?", "B#"], "Symbols.A1!"),
    ("CaseSensitivity", ["a", "A"], "CaseSens.A"),
    ("ComplexStrings", ["A B", "a b", "A1", "a2"], "ComplexStrings.A B"),
    
    # --- Structural Edge Cases ---
    ("SingleExtension", ["OnlyOne"], "Single.OnlyOne"),
    ("EmptyClassName", "", ["Ext"], ".Ext"),
])
def test_strongest_extension_logic(class_name, extensions, expected):
    """
    Comprehensive test covering strength calculation, tie-breaking, 
    case sensitivity, non-alphabetic characters, and various string compositions.
    """
    assert Strongest_Extension(class_name, extensions) == expected


def test_empty_extensions_list():
    """
    Tests behavior when the extensions list is empty.
    The implementation returns None for empty lists.
    """
    assert Strongest_Extension("EmptyClass", []) is None
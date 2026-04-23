
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

# --- Implementation (Included for completeness of the test run) ---

def Strongest_Extension(class_name, extensions):
    if not extensions:
        return None
    
    def calculate_strength(ext):
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        return cap - sm

    # Python's max() is stable; it returns the first occurrence in case of ties.
    strongest = max(extensions, key=calculate_strength)
    return f"{class_name}.{strongest}"

# --- Superior Pytest Suite ---

@pytest.mark.parametrize("class_name, extensions, expected", [
    # 1. Mathematical Correctness (Cap - Small)
    ("Base", ["ABC", "Abc", "abc"], "Base.ABC"),      # 3, 1, -3 -> ABC
    ("Base", ["abc", "aBc", "abC"], "Base.aBc"),      # -3, -1, -1 -> aBc (tie-break)
    ("Base", ["a", "A", "!"], "Base.A"),              # -1, 1, 0 -> A
    ("Data", ["A", "aa", "AAA"], "Data.AAA"),         # 1, -2, 3 -> AAA
    ("Mix", ["aB", "Ba", "BB"], "Mix.BB"),            # 0, 0, 2 -> BB
    
    # 2. Tie-Breaking (First occurrence wins)
    ("Tie", ["Ab", "Cd", "Ef"], "Tie.Ab"),            # 0, 0, 0 -> Ab
    ("TiePos", ["AA", "BB", "CC"], "TiePos.AA"),      # 2, 2, 2 -> AA
    ("TieNeg", ["aa", "bb", "cc"], "TieNeg.aa"),      # -2, -2, -2 -> aa
    ("TieMixed", ["A1", "B2", "123"], "TieMixed.A1"), # 1, 1, 0 -> A1
    
    # 3. Non-Alphabetic Characters (Should contribute 0 to strength)
    ("Sym", ["!!!", "@@@", "###"], "Sym.!!!"),        # 0, 0, 0 -> !!!
    ("AlphaNum", ["A1!", "a2@", "123"], "AlphaNum.A1!"), # 1, -1, 0 -> A1!
    
    # 4. All Negative Strengths
    ("Neg", ["abc", "ab", "a"], "Neg.a"),             # -3, -2, -1 -> a
    
    # 5. Extreme Case Sensitivity
    ("Edge", ["aaaaa", "AAAAA"], "Edge.AAAAA"),       # -5 vs 5
    ("Edge2", ["aAaAa", "AaAaA"], "Edge2.AaAaA"),     # -1 vs 1
])
def test_core_logic_and_ties(class_name, extensions, expected):
    """Tests the mathematical strength calculation and the tie-breaking rule."""
    assert Strongest_Extension(class_name, extensions) == expected


@pytest.mark.parametrize("class_name, extensions, expected", [
    # 6. Class Name Edge Cases
    ("", ["Ext"], ".Ext"),                            # Empty class name
    (" ", ["Ext"], " .Ext"),                          # Whitespace class name
    ("Class_123", ["Ext"], "Class_123.Ext"),          # Alphanumeric class name
    
    # 7. List Size/Content Edge Cases
    ("Solo", ["OnlyOne"], "Solo.OnlyOne"),            # Single element list
    ("EmptyList", [], None),                          # Empty extensions list
])
def test_edge_cases(class_name, extensions, expected):
    """Tests boundary conditions like empty strings, single items, and empty lists."""
    assert Strongest_Extension(class_name, extensions) == expected


def test_provided_examples():
    """Explicitly verifies the examples provided in the original problem description."""
    # Example 1: SErviNGSliCes strength is -1, Cheese is -4, StuFfed is -3.
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    
    # Example 2: AA is 2, Be is 0, CC is 2. AA comes first.
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
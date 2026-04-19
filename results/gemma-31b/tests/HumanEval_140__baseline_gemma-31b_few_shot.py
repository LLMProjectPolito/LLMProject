
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Pytest") == "Pytest"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Hello") == "_Hello"
    assert fix_spaces("World ") == "World_"

def test_fix_spaces_two_spaces():
    # Rule: Replace all spaces with underscores unless there are MORE than 2
    assert fix_spaces("Example  2") == "Example__2"
    assert fix_spaces("  ") == "__"

def test_fix_spaces_three_or_more_spaces():
    # Rule: More than 2 consecutive spaces are replaced by a single '-'
    assert fix_spaces("Example   3") == "Example-3"
    assert fix_spaces("Example    4") == "Example-4"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("Example     5") == "Example-5"

def test_fix_spaces_mixed_spacing():
    # Mix of single, double, and triple+ spaces
    # " a" (1) -> "_a"
    # "a  b" (2) -> "a__b"
    # "b   c" (3) -> "b-c"
    # "c    d" (4) -> "c-d"
    # "d " (1) -> "d_"
    assert fix_spaces(" a  b   c    d ") == "_a__b-c-d_"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_only_spaces():
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "__"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"
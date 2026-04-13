
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
    assert fix_spaces("Hello World") == "Hello_World"

def test_fix_spaces_leading_trailing():
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces("Example 2 ") == "Example_2_"
    assert fix_spaces(" Example ") == "_Example_"

def test_fix_spaces_two_consecutive():
    # "more than 2" means 3 or more. 2 spaces should be replaced by underscores.
    assert fix_spaces("Example  2") == "Example__2"

def test_fix_spaces_more_than_two_consecutive():
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("Example    4") == "Example-4"
    assert fix_spaces("Example     5") == "Example-5"

def test_fix_spaces_mixed_patterns():
    # 1 space -> _, 2 spaces -> __, 3+ spaces -> -
    assert fix_spaces(" a  b   c    d ") == "_a__b-c-d_"
    assert fix_spaces("  hello   world  ") == "__hello-world__"

def test_fix_spaces_empty_and_whitespace_only():
    assert fix_spaces("") == ""
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "__"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("This  is   a    test") == "This_is-a-test"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  Hello  World  ") == "-Hello_World-"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_fix_spaces_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_fix_spaces_string_with_mixed_whitespace():
    assert fix_spaces("Example \t 1 \n 2") == "Example_1_2"
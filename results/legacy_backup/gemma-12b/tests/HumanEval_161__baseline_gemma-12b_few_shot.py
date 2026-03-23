def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_all_letters_lower():
    assert solve("ab") == "AB"

def test_solve_mixed_letters_and_symbols():
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_single_letter():
    assert solve("a") == "A"

def test_solve_single_number():
    assert solve("1") == "1"

def test_solve_single_symbol():
    assert solve("#") == "#"

def test_solve_complex_string():
    assert solve("aBc12#dE") == "AbC12#D"

def test_solve_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_solve_string_with_unicode():
    assert solve("你好世界") == "你好世界"

def test_solve_string_with_mixed_unicode_and_letters():
    assert solve("你好a世界") == "你好A世界"
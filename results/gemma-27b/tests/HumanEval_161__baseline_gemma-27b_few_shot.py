def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_all_letters():
    assert solve("ab") == "AB"

def test_solve_mixed_case_and_symbols():
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_only_symbols():
    assert solve("!@#$") == "$#@!"

def test_solve_letters_and_numbers():
    assert solve("a1b2c") == "A1B2C"

def test_solve_complex_string():
    assert solve("HeLlO wOrLd 123!") == "hElLo WoRlD 123!"

def test_solve_with_spaces():
    assert solve("  a b  ") == "  A B  "

def test_solve_single_letter():
    assert solve("a") == "A"

def test_solve_single_number():
    assert solve("1") == "1"
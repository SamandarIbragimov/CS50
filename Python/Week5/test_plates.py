from plates import is_valid

def test_is_valid():
    assert is_valid("a") == False
    assert is_valid("ab1#$") == False
    assert is_valid("Abcdefg") == False
    assert is_valid("aB0234") == False
    assert is_valid("ab1ef") == False
    assert is_valid("1ABcDe") == False
    assert is_valid("12BcDe") == False
    assert is_valid("A2BcDe") == False
    assert is_valid("12") == False
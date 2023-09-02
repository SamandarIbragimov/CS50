from numb3rs import validate

def test_validate():
    assert validate("256.0.0.1") == False
    assert validate("25.500.0.1") == False
    assert validate("25.0.500.1") == False
    assert validate("25.0.0.501") == False
    assert validate("25.0.0.-1") == False
    assert validate("cat") == False
    assert validate("cat.0.0.1") == False
    assert validate("1.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("2555.255555.255555.25555") == False
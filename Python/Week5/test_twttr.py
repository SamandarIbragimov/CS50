from twttr import shorten

def test_shorten_lower():
    assert shorten("Hello") == "Hll"

def test_shorten_upper():
    assert shorten("HEllO") == "Hll"

def test_shorten_num():
    assert shorten("Hello12345") == "Hll12345"

def test_shorten_punc():
    assert shorten("#HEllO$ %@!") == "#Hll$ %@!"


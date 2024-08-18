from  test_vowel import shorten
import pytest

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("CS") == "CS"
    assert shorten("Test") == "Tst"
    assert shorten("Computer Science") == "Cmptr Scnc"
    assert shorten("Programming is fun") == "Prgrmmng s fn"
    assert shorten("I love coding") == " lv cdng"

def test_punctuation():
    assert shorten("!?.,") == "!?.,"

def test_numbers():
    assert shorten("1234567890") == "1234567890"

if __name__ == "__main__":
    pytest.main()


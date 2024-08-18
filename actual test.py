from  test_vowel import shorten
import pytest

def test_twttr():
    assert shorten("Hello") =="Hll"
    assert shorten("CS") == "CS"
    assert shorten("Test") == "Tst"
    assert shorten("Computer Science") == "Cmptr Scnc"
    assert shorten("Programming is fun") == "Prgrmmng s fn"
    assert shorten("I love coding") == " lv cdng"
    assert shorten("This is a longer test phrase") == "Ths s lngr tst phrs"
    assert shorten("How are you today?") == "Hw r y tdy?"
    assert shorten("Debugging is essential") == "Dbggrng s ssntl"
    assert shorten("Learning to code is a valuable skill") == "Lrnng t cd s vlbl skll"
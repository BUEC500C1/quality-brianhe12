from arabic_to_roman import arabic2roman

def test_answer():
    assert arabic2roman(1) == "I"
    assert arabic2roman(3) == "III"
    assert arabic2roman(4) == "IV"
    assert arabic2roman(28) == "XXVIII"
    assert arabic2roman(49) == "XLIX"
    assert arabic2roman(571) == "DLXXI"
    assert arabic2roman(700) == "DCC"
    assert arabic2roman(821) == "DCCCXXI"
    assert arabic2roman(999) == "CMXCIX"
    assert arabic2roman(1000) == "M"
    assert arabic2roman(1999) == "MCMXCIX"
    assert arabic2roman(3999) == "MMMCMXCIX"


    #Edge Cases
    assert arabic2roman(3999999) == ''
    assert arabic2roman(999999999999999999999999) == ''
    assert arabic2roman(-1928) == ''
    assert arabic2roman('a') == ''
    assert arabic2roman(']') == ''
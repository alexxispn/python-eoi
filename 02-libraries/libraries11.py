import re

pat = re.compile(r"anaconda\w")
pat_variable = re.compile(r"[A-Za-z_]\w*")
pat_tortilla = re.compile(r"tortilla, re.IGNORECASE")
word = "123anaconda_"
print(pat.search(word))
print(pat.findall(word))

phone_number = re.compile(r"[0-9]{3}-[0-9]{3}-[0-9]{3}")
phone_number2 = re.compile(r"\d{3}-\d{3}-\d{3}")
matricula_coche = re.compile(r"[0-9]{4}[A-Z]{3}")


def is_phone(number):
    return (len(number) == 11) and (phone_number.match(number) is not None)


def test_ok():
    assert is_phone("603-188-992") is True
    assert is_phone("603-188-9922") is False
    assert is_phone("603-188-99a") is False
    assert is_phone("603-188--99") is False


test_ok()

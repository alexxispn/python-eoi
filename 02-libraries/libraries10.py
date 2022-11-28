def is_phone(number):
    if len(number) != 11 or number[3] != "-" or number[7] != "-":
        return False
    number = number.replace("-", "")
    for char in number:
        if not char.isdigit():
            return False
    return True


def test_ok():
    assert is_phone("603-188-992") is True
    assert is_phone("603-188-9922") is False
    assert is_phone("603-188-99a") is False


test_ok()

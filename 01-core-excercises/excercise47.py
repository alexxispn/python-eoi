def get_int_iterative():
    while True:
        try:
            num = int(input("Give me an integer number: "))
            return num
        except ValueError:
            print("Not a valid integer. Try it again!")


def get_int_recursive():
    try:
        num = int(input("Give me an integer number: "))
        return num
    except ValueError:
        print("Not a valid integer. Try it again!")
        get_int_recursive()


def get_int():
    while value := input("Give me an integer number: "):
        try:
            return int(value)
        except ValueError:
            print("Not a valid integer. Try it again!")


# get_int_iterative()
# get_int_recursive()
get_int()

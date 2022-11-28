entry = int(input("Enter a number: "))


# def _factorial(x):
#     return 1 if x == 0 else x * _factorial(x - 1)


def _factorial(x):
    factorial = 1
    for i in range(2, x + 1):
        factorial *= i
    return factorial


print(_factorial(entry))

from icecream import ic


def equation(a, b, c):
    ic(a, b, c)
    return a + b + c


def main():
    ic(equation(1, 2, 3))
    ic(equation(4, 5, 6))


if __name__ == '__main__':
    main()

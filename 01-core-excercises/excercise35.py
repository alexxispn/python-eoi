entry = int(input("Introduce un número: "))


# 8128


def perfect_number(number: int) -> bool:
    divisors = [divisor for divisor in range(1, number // 2 + 1) if
                number % divisor == 0]
    return sum(divisors) == number


print(perfect_number(entry))

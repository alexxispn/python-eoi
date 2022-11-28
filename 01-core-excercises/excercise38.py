def gen_squared(limit: int) -> iter:
    for number in range(1, limit + 1):
        yield number ** 2


gen_squared = gen_squared(100)

# gen_squared = (i ** 2 for i in range(1, 101))


for index, squared in enumerate(start=1, iterable=gen_squared):
    print(f"{index}^2 = {squared}")

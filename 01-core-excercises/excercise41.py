def plus5(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 5

    return wrapper


def div2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result // 2

    return wrapper


@plus5
@div2
def prod(a, b):
    return a * b


print(prod(4, 3))

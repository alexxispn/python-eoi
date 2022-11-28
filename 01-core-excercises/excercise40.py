entry = -3, 7.6, "hola"


def filter_numeric(func):
    def wrapper(*args, **kwargs):
        args = [round(arg) for arg in args if type(arg) in (int, float)]
        kwargs = {k: round(v) for k, v in kwargs.items() if
                  type(v) in (int, float)}
        return func(*args, **kwargs)

    return wrapper


def transform_abs(func):
    def wrapper(*args, **kwargs):
        args = [abs(arg) for arg in args]
        kwargs = {k: abs(v) for k, v in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper


@filter_numeric
@transform_abs
def fprod(*args, **kwargs):
    prod = 1
    for arg in args:
        prod *= arg
    for kwarg in kwargs.values():
        prod *= kwarg
    return prod


print(fprod(*entry))

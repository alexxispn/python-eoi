def sin(x):
    a = x * (180 - x)
    return 4 * a / (40500 - a)


print('sin():', sin(90))
print('sin():', sin(45))
print('sin():', sin(50))

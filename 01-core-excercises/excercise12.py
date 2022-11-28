value1 = float(input("Introduce el valor 1: "))
value2 = float(input("Introduce el valor 2: "))
value3 = float(input("Introduce el valor 3: "))

if value1 == value2 == value3:
    print("Los tres valores son iguales")
elif (value1 < value2) and (value1 < value3):
    print("El valor 1 es el menor")
elif (value2 < value1) and (value2 < value3):
    print("El valor 2 es el menor")
elif (value3 < value1) and (value3 < value2):
    print("El valor 3 es el menor")
elif (value1 == value2) and (value1 < value3):
    print("Los valores 1 y 2 son los menores")
elif value1 == value3 and value1 < value2:
    print("Los valores 1 y 3 son los menores")
else:
    print("Los valores 2 y 3 son los menores")

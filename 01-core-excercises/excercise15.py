entry = int(input("Introduce un número entero: "))

if entry <= 1:
    print(f'{entry} no es un número primo')
else:
    for num in range(2, entry // 2 + 1):
        if entry % num == 0:
            print(f'{entry} no es un número primo')
            break
    else:
        print(f'{entry} es un número primo')

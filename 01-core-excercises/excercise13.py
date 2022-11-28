entry = input("Introduce un string de 8 caracteres: ")
entry2 = input("Introduce un string de 8 caracteres: ")
entry_length = 8

if len(entry) == entry_length and len(entry2) == entry_length:
    hamming = 0
    i = 0
    while i < entry_length:
        if entry[i] != entry2[i]:
            hamming += 1
        i += 1
    print(f"El número de cambios de Hamming es: {hamming}")
else:
    print("Alguno de los strings no tiene 8 caracteres")

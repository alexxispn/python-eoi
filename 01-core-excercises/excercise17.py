ALPHABET = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
entry = input("Introduce una cadena de texto: ").lower()

for letter in entry:
    if letter not in ALPHABET:
        print("Se han encontrado caracteres no alfabéticos")
        break
else:
    print("La cadena es alfabética")

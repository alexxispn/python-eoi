entry = input("Introduce una cadena de texto: ")
for letter in entry:
    if not letter.isalpha():
        entry = entry.replace(letter, "")

for letter in entry:
    if entry.count(letter) > 1:
        print("No es un isograma")
        break
else:
    print("Es un isograma")

VOWELS = 'aeiouáéíóúü'
entry = input('Introduce un String: ').lower()
vowels_count = 0

for letter in entry:
    if letter in VOWELS:
        vowels_count += 1

print(f'El número de vocales es: {vowels_count}')

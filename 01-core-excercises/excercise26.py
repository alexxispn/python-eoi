entry = input('Introduce una palabra: ').lower()
entry = entry.replace('á', 'a').replace('é', 'e').replace('í', 'i') \
    .replace('ó', 'o').replace('ú', 'u').replace('ü', 'u')

enum_characters = {}
for character in entry:
    if character in enum_characters:
        enum_characters[character] += 1
    else:
        enum_characters[character] = 1

print(enum_characters)
